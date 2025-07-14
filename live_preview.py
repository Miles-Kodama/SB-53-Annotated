#!/usr/bin/env python3
"""
Live Preview Server for Annotated Markdown

Watches for changes to markdown files and automatically rebuilds HTML with live reload.
"""

import http.server
import socketserver
import os
import sys
import time
import threading
import subprocess
from pathlib import Path
import json

# Import the converter functions from md_to_annotated_html.py
from md_to_annotated_html import parse_markdown, generate_html

class LiveReloadHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP handler with live reload support."""
    
    def __init__(self, *args, last_modified=None, **kwargs):
        self.last_modified = last_modified
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        if self.path == '/livereload':
            # Send last modified time as JSON
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Cache-Control', 'no-cache')
            self.end_headers()
            response = {'last_modified': self.server.last_modified}
            self.wfile.write(json.dumps(response).encode())
        else:
            # Inject live reload script into HTML files
            if self.path.endswith('.html') or self.path == '/':
                file_path = self.path[1:] if self.path != '/' else 'index.html'
                if os.path.exists(file_path):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Inject live reload script before </body>
                    live_reload_script = '''
    <script>
        (function() {
            let lastModified = null;
            
            async function checkForUpdates() {
                try {
                    const response = await fetch('/livereload');
                    const data = await response.json();
                    
                    if (lastModified === null) {
                        lastModified = data.last_modified;
                    } else if (lastModified !== data.last_modified) {
                        location.reload();
                    }
                } catch (e) {
                    console.error('Live reload error:', e);
                }
            }
            
            // Check every 500ms
            setInterval(checkForUpdates, 500);
            
            // Also log that live reload is active
            console.log('Live reload is active - page will refresh when markdown is saved');
        })();
    </script>
</body>'''
                    content = content.replace('</body>', live_reload_script)
                    
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Content-Length', str(len(content.encode())))
                    self.end_headers()
                    self.wfile.write(content.encode())
                    return
            
            # Default behavior for other files
            super().do_GET()

class LiveReloadServer(socketserver.TCPServer):
    """TCP Server with last_modified tracking."""
    allow_reuse_address = True
    
    def __init__(self, *args, **kwargs):
        self.last_modified = time.time()
        super().__init__(*args, **kwargs)

def watch_and_rebuild(md_file, html_file, server):
    """Watch markdown file and rebuild HTML on changes."""
    last_mtime = 0
    
    print(f"\n📝 Watching '{md_file}' for changes...")
    print(f"🔄 Output will be written to '{html_file}'")
    
    while True:
        try:
            current_mtime = os.path.getmtime(md_file)
            
            if current_mtime > last_mtime:
                last_mtime = current_mtime
                
                print(f"\n🔄 Change detected in '{md_file}', rebuilding...")
                
                # Read and convert
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                parsed_data = parse_markdown(content)
                html_content = generate_html(parsed_data)
                
                # Write output
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(html_content)
                
                # Update server's last modified time
                server.last_modified = time.time()
                
                print(f"✅ HTML rebuilt successfully!")
                
        except Exception as e:
            print(f"❌ Error during rebuild: {e}")
        
        time.sleep(0.5)  # Check twice per second

def main():
    # Parse arguments
    if len(sys.argv) < 2:
        print("Usage: python live_preview.py input.md [output.html] [--port 8000]")
        sys.exit(1)
    
    md_file = sys.argv[1]
    html_file = 'index.html'  # Default output
    port = 8000  # Default port
    
    # Parse optional arguments
    for i in range(2, len(sys.argv)):
        if sys.argv[i] == '--port' and i + 1 < len(sys.argv):
            port = int(sys.argv[i + 1])
        elif not sys.argv[i].startswith('--'):
            html_file = sys.argv[i]
    
    # Check if markdown file exists
    if not os.path.exists(md_file):
        print(f"❌ Error: Markdown file '{md_file}' not found.")
        sys.exit(1)
    
    # Initial build
    print(f"🚀 Starting live preview server...")
    print(f"📄 Input: {md_file}")
    print(f"📄 Output: {html_file}")
    
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        parsed_data = parse_markdown(content)
        html_content = generate_html(parsed_data)
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Initial HTML build complete!")
        
    except Exception as e:
        print(f"❌ Error during initial build: {e}")
        sys.exit(1)
    
    # Start server
    Handler = lambda *args, **kwargs: LiveReloadHandler(*args, **kwargs)
    
    with LiveReloadServer(("", port), Handler) as httpd:
        # Start file watcher in background thread
        watcher_thread = threading.Thread(
            target=watch_and_rebuild,
            args=(md_file, html_file, httpd),
            daemon=True
        )
        watcher_thread.start()
        
        print(f"\n🌐 Server running at http://localhost:{port}")
        print(f"👀 Viewing: http://localhost:{port}/{html_file}")
        print(f"\n💡 Tip: Open the URL in your browser. The page will auto-refresh when you save changes to '{md_file}'")
        print(f"🛑 Press Ctrl+C to stop the server\n")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Shutting down server...")
            httpd.shutdown()

if __name__ == "__main__":
    main()