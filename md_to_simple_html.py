#!/usr/bin/env python3
"""
Markdown to Simple HTML Converter

Converts markdown files with ordered lists and footnotes into HTML with consistent styling.
Designed for supplementary pages (summary, FAQ) that match the main bill annotation style.

Usage:
    python md_to_simple_html.py input.md output.html
"""

import re
import sys
from pathlib import Path


def parse_markdown(content):
    """Parse markdown content and extract structure."""
    
    # Extract title (first # heading)
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else "Document"
    
    # Remove title from content
    if title_match:
        content = content[title_match.end():].strip()
    
    # Extract and process footnotes
    footnotes = {}
    footnote_pattern = r'\[\^(\d+)\]:\s*(.+?)(?=\n\[\^|\n\n|\Z)'
    for match in re.finditer(footnote_pattern, content, re.DOTALL):
        footnote_id = match.group(1)
        footnote_text = match.group(2).strip()
        footnotes[footnote_id] = footnote_text
    
    # Remove footnote definitions from content
    content = re.sub(footnote_pattern, '', content, flags=re.DOTALL).strip()
    
    return {
        'title': title,
        'content': content,
        'footnotes': footnotes
    }


def process_content(text, footnotes):
    """Convert markdown to HTML."""
    
    # Convert footnote references
    def replace_footnote_ref(match):
        footnote_id = match.group(1)
        return f'<sup><a href="#fn{footnote_id}" id="ref{footnote_id}" class="footnote-ref">{footnote_id}</a></sup>'
    
    text = re.sub(r'\[\^(\d+)\]', replace_footnote_ref, text)
    
    # Convert headers (##, ###, ####)
    text = re.sub(r'^####\s+(.+)$', r'<h4>\1</h4>', text, flags=re.MULTILINE)
    text = re.sub(r'^###\s+(.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^##\s+(.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    
    # Convert bold text (**text** or __text__)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'__([^_]+)__', r'<strong>\1</strong>', text)
    
    # Convert italic text (*text* or _text_)
    text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)
    text = re.sub(r'_([^_]+)_', r'<em>\1</em>', text)
    
    # Convert links [text](url)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    
    # Process lists
    lines = text.split('\n')
    processed_lines = []
    in_ordered_list = False
    in_unordered_list = False
    
    for i, line in enumerate(lines):
        # Check for ordered list items
        ordered_match = re.match(r'^(\d+)\.\s+(.+)$', line)
        unordered_match = re.match(r'^[*\-+]\s+(.+)$', line)
        
        if ordered_match:
            if not in_ordered_list:
                processed_lines.append('<ol>')
                in_ordered_list = True
                if in_unordered_list:
                    processed_lines.insert(-1, '</ul>')
                    in_unordered_list = False
            
            list_content = ordered_match.group(2)
            processed_lines.append(f'<li>{list_content}</li>')
            
        elif unordered_match:
            if not in_unordered_list:
                processed_lines.append('<ul>')
                in_unordered_list = True
                if in_ordered_list:
                    processed_lines.insert(-1, '</ol>')
                    in_ordered_list = False
            
            list_content = unordered_match.group(1)
            processed_lines.append(f'<li>{list_content}</li>')
            
        else:
            # Not a list item
            if in_ordered_list:
                processed_lines.append('</ol>')
                in_ordered_list = False
            if in_unordered_list:
                processed_lines.append('</ul>')
                in_unordered_list = False
            
            processed_lines.append(line)
    
    # Close any open lists
    if in_ordered_list:
        processed_lines.append('</ol>')
    if in_unordered_list:
        processed_lines.append('</ul>')
    
    text = '\n'.join(processed_lines)
    
    # Convert paragraphs
    paragraphs = text.split('\n\n')
    processed_paragraphs = []
    
    for para in paragraphs:
        para = para.strip()
        if para:
            # Don't wrap headers, lists, or already wrapped content in <p>
            if (not para.startswith('<h') and 
                not para.startswith('<ol') and 
                not para.startswith('<ul') and
                not '<ol>' in para and
                not '<ul>' in para):
                para = f'<p>{para}</p>'
            processed_paragraphs.append(para)
    
    return '\n\n'.join(processed_paragraphs)


def generate_footnotes_html(footnotes):
    """Generate HTML for footnotes section."""
    if not footnotes:
        return ''
    
    html = '<div class="footnotes">\n<hr>\n<ol>\n'
    for fn_id, fn_text in sorted(footnotes.items(), key=lambda x: int(x[0])):
        html += f'<li id="fn{fn_id}">{fn_text} <a href="#ref{fn_id}" class="footnote-backref">↩</a></li>\n'
    html += '</ol>\n</div>'
    return html


def generate_html(parsed_data):
    """Generate the complete HTML document."""
    
    # Process the main content
    processed_content = process_content(parsed_data['content'], parsed_data['footnotes'])
    
    # Generate footnotes HTML
    footnotes_html = generate_footnotes_html(parsed_data['footnotes'])
    
    html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="icon" type="image/png" href="/53favicon.png">
    <style>
        body {{
            font-family: Georgia, serif;
            line-height: 1.8;
            margin: 0;
            padding: 20px;
            background-color: #fafafa;
            color: #333;
        }}
        
        .container {{
            max-width: 700px;
            margin: 0 auto;
            background: white;
            padding: 3rem;
            border-radius: 4px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        h1 {{
            text-align: center;
            color: #333;
            margin-bottom: 2rem;
        }}
        
        h2 {{
            color: #333;
            margin-top: 2rem;
            margin-bottom: 1rem;
            font-size: 1.3em;
        }}
        
        h3 {{
            color: #555;
            margin-top: 1.5rem;
            margin-bottom: 0.75rem;
            font-size: 1.1em;
        }}
        
        h4 {{
            color: #666;
            margin-top: 1rem;
            margin-bottom: 0.5rem;
            font-size: 1em;
        }}
        
        p {{
            margin-bottom: 1rem;
        }}
        
        a {{
            color: #1976d2;
            text-decoration: none;
        }}
        
        a:hover {{
            text-decoration: underline;
        }}
        
        /* List styling */
        ul, ol {{
            margin: 1rem 0;
            padding-left: 2rem;
        }}
        
        li {{
            margin-bottom: 0.5rem;
        }}
        
        /* Footnote styling */
        .footnote-ref {{
            font-weight: bold;
            padding: 0 2px;
        }}
        
        .footnotes {{
            margin-top: 3rem;
            font-size: 0.9em;
        }}
        
        .footnotes hr {{
            border: none;
            border-top: 1px solid #e0e0e0;
            margin-bottom: 1rem;
        }}
        
        .footnotes ol {{
            padding-left: 1.5rem;
        }}
        
        .footnotes li {{
            margin-bottom: 0.5rem;
            color: #666;
        }}
        
        .footnote-backref {{
            margin-left: 0.5rem;
            font-size: 0.85em;
        }}
        
        /* Navigation */
        .nav-bar {{
            text-align: center;
            margin-bottom: 2rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid #e0e0e0;
        }}
        
        .nav-link {{
            display: inline-block;
            margin: 0 1rem;
            color: #666;
            font-size: 0.9em;
        }}
        
        .nav-link:hover {{
            color: #1976d2;
        }}
        
        .nav-link.back {{
            font-weight: bold;
        }}
        
        /* Emphasis */
        strong {{
            color: #333;
        }}
        
        em {{
            font-style: italic;
        }}
        
        /* Mobile responsive */
        @media (max-width: 600px) {{
            .container {{
                padding: 2rem 1.5rem;
            }}
            
            h1 {{
                font-size: 1.5em;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <nav class="nav-bar">
            <a href="index" class="nav-link back">← Back to Bill Text</a>
            <a href="summary" class="nav-link">Summary</a>
            <a href="faq" class="nav-link">FAQs</a>
        </nav>
        
        <h1>{title}</h1>
        
        {content}
        
        {footnotes}
    </div>
</body>
</html>'''
    
    return html_template.format(
        title=parsed_data['title'],
        content=processed_content,
        footnotes=footnotes_html
    )


def main():
    if len(sys.argv) != 3:
        print("Usage: python md_to_simple_html.py input.md output.html")
        sys.exit(1)
    
    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2])
    
    if not input_file.exists():
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    
    # Read input
    content = input_file.read_text(encoding='utf-8')
    
    # Parse and generate HTML
    parsed_data = parse_markdown(content)
    html_content = generate_html(parsed_data)
    
    # Write output
    output_file.write_text(html_content, encoding='utf-8')
    print(f"Successfully converted '{input_file}' to '{output_file}'")


if __name__ == "__main__":
    main()