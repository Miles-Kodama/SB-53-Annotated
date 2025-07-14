#!/usr/bin/env python3
"""
Markdown to Annotated HTML Converter

Converts specially-formatted markdown files into HTML with expandable inline annotations.

Usage:
    python md_to_annotated_html.py input.md output.html
"""

import re
import sys
from pathlib import Path

def parse_markdown(content):
    """Parse the markdown content and extract structure."""
    
    # Extract title (first # heading)
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else "Document"
    
    # Find where the first section starts
    first_section_match = re.search(r'^##\s+', content, re.MULTILINE)
    
    # Extract instructions (text between title and first section)
    instructions = None
    if title_match and first_section_match:
        # Get text between title and first section
        title_end = title_match.end()
        section_start = first_section_match.start()
        instructions_text = content[title_end:section_start].strip()
        
        # Only use as instructions if there's actual content
        if instructions_text:
            instructions = instructions_text
    
    # Extract sections more carefully
    sections = []
    
    # Split content by section headers (lines starting with ##)
    parts = re.split(r'^(##\s+.+)$', content, flags=re.MULTILINE)
    
    # Process the parts - they alternate between content and headers
    i = 1  # Skip the first part (content before first ##)
    while i < len(parts) - 1:
        if parts[i].startswith('##'):
            # Extract section title (remove ## and whitespace)
            section_title = parts[i][2:].strip()
            
            # Get the content that follows this header
            section_content = parts[i + 1].strip() if i + 1 < len(parts) else ""
            
            sections.append({
                'title': section_title,
                'content': section_content
            })
            
            i += 2
        else:
            i += 1
    
    return {
        'title': title,
        'instructions': instructions,
        'sections': sections
    }

def process_annotations(text):
    """Convert markdown annotation syntax to HTML."""
    
    # Convert markdown italicized text (_text_ or *text*) to <em>text</em>
    text = re.sub(r'_(.*?)_', r'<em>\1</em>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    
    # Convert standard markdown links to HTML links (but not in annotations)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank">\1</a>', text)
    
    # Convert markdown headings (###) to <h3>
    text = re.sub(r'^###\s+(.*)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    
    # Pattern to match [annotated text]{annotation content}
    # The pattern needs to be improved to handle nested braces
    pattern = r'\[([^\]]+)\]\{([^}]+(?:\{[^}]*\}[^}]*)*)\}'
    
    def replace_annotation(match):
        annotated_text = match.group(1)
        annotation_content = match.group(2).strip()
        
        # Check if annotation has a header (indicated by first line ending with :)
        lines = annotation_content.split('\n', 1)
        if len(lines) > 0 and lines[0].endswith(':'):
            header = lines[0][:-1]  # Remove the colon
            body = lines[1].strip() if len(lines) > 1 else ""
        else:
            # Use a generic header
            header = "Note"
            body = annotation_content
        
        # Process links in the annotation body
        body = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank">\1</a>', body)
        
        # Build HTML
        html = f'<span class="annotated">{annotated_text}</span>'
        html += f'<span class="annotation-inline">'
        html += f'<div class="annotation-header">{header}</div>'
        html += f'{body}'
        html += f'</span>'
        
        return html
    
    # Process all annotations
    processed = re.sub(pattern, replace_annotation, text)
    
    # Convert line breaks to <br> tags within paragraphs
    # But first mark real paragraphs
    processed = re.sub(r'\n\n', '<!--PARA-->', processed)
    processed = re.sub(r'\n', '<br>', processed)
    processed = re.sub(r'<!--PARA-->', '\n\n', processed)
    
    return processed

def generate_html(parsed_data):
    """Generate the complete HTML document."""
    
    html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
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
        
        .bill-section {{
            margin-bottom: 2rem;
        }}
        
        .section-heading {{
            font-size: 1.1em;
            margin-bottom: 1rem;
            color: #333;
            font-weight: normal;
        }}
        
        .section-number {{
            font-weight: bold;
            color: #555;
        }}
        
        .annotated {{
            position: relative;
            background-color: #e3f2fd;
            padding: 2px 4px;
            border-radius: 3px;
            cursor: pointer;
            transition: background-color 0.2s ease;
            border-bottom: 2px dotted #1976d2;
        }}
        
        .annotated:hover {{
            background-color: #bbdefb;
        }}
        
        .annotated.expanded {{
            background-color: #1976d2;
            color: white;
        }}
        
        .annotation-inline {{
            display: block;
            margin: 0.5rem 0 0.5rem 2rem;
            padding: 1rem;
            background-color: #f5f5f5;
            border-left: 4px solid #1976d2;
            font-size: 0.9em;
            line-height: 1.6;
            border-radius: 0 4px 4px 0;
            max-height: 0;
            overflow: hidden;
            opacity: 0;
            transition: all 0.3s ease;
        }}
        
        .annotation-inline.show {{
            max-height: 500px;
            opacity: 1;
            margin: 0.5rem 0 0.5rem 2rem;
        }}
        
        .annotation-header {{
            font-weight: bold;
            color: #1976d2;
            margin-bottom: 0.5rem;
        }}
        
        .instructions {{
            background-color: #fff3cd;
            padding: 1rem;
            border-radius: 4px;
            margin-bottom: 2rem;
            font-size: 0.9em;
            text-align: center;
            color: #856404;
        }}
        
        /* Small indicator for annotated text */
        .annotated::after {{
            content: "↓";
            font-size: 0.7em;
            margin-left: 2px;
            opacity: 0.6;
        }}
        
        .annotated.expanded::after {{
            content: "↑";
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{title}</h1>
        
        {instructions_html}
        
        {sections_html}
    </div>
    
    <script>
        document.querySelectorAll('.annotated').forEach(element => {{
            element.addEventListener('click', function(e) {{
                e.stopPropagation();
                
                // Find the annotation that follows this element
                const annotation = this.nextElementSibling;
                
                if (annotation && annotation.classList.contains('annotation-inline')) {{
                    // Toggle the annotation
                    annotation.classList.toggle('show');
                    this.classList.toggle('expanded');
                    
                    // Close other annotations
                    document.querySelectorAll('.annotation-inline.show').forEach(other => {{
                        if (other !== annotation) {{
                            other.classList.remove('show');
                            other.previousElementSibling.classList.remove('expanded');
                        }}
                    }});
                }}
            }});
        }});
        
        // Click anywhere else to close annotations
        document.addEventListener('click', function() {{
            document.querySelectorAll('.annotation-inline.show').forEach(annotation => {{
                annotation.classList.remove('show');
                annotation.previousElementSibling.classList.remove('expanded');
            }});
        }});
    </script>
</body>
</html>'''
    
    # Generate instructions HTML if present
    instructions_html = ''
    if parsed_data['instructions']:
        instructions_html = f'<div class="instructions">{parsed_data["instructions"]}</div>'
    
    # Generate sections HTML
    sections_html = ''
    for section in parsed_data['sections']:
        section_html = f'<div class="bill-section">\n'
        
        # Add section title as a heading
        section_html += f'<h2 class="section-heading"><span class="section-number">{section["title"]}</span></h2>\n'
        
        # Process the content
        paragraphs = section['content'].split('\n\n')
        for para in paragraphs:
            if para.strip():
                processed_para = process_annotations(para)
                section_html += f'<p>{processed_para}</p>\n'
        
        section_html += '</div>\n'
        sections_html += section_html
    
    return html_template.format(
        title=parsed_data['title'],
        instructions_html=instructions_html,
        sections_html=sections_html
    )

def main():
    if len(sys.argv) != 3:
        print("Usage: python md_to_annotated_html.py input.md output.html")
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