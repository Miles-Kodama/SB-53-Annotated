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
import uuid


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
            section_content = parts[i + 1].strip() if i + \
                1 < len(parts) else ""

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

    # Convert \\ to create blank lines
    text = re.sub(r'\\\\', '<br>', text)

    # Convert markdown italicized text (_text_ or *text*) to <em>text</em>
    text = re.sub(r'_(.*?)_', r'<em>\1</em>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)

    # Store annotations to be placed at paragraph end
    paragraph_annotations = []

    # Pattern to match [annotated text]{annotation content}
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
            header = "Note"
            body = annotation_content

        # Process markdown in the body content
        body = re.sub(r'\[([^\]]+)\]\(([^)]+)\)',
                      r'<a href="\2" target="_blank">\1</a>', body)

        # Process lists within annotations
        body_lines = body.split('\n')
        in_list = False
        list_buffer = []
        result_lines = []

        for line in body_lines:
            list_match = re.match(r'^[*\-+]\s+(.*)$', line)

            if list_match:
                if not in_list:
                    in_list = True
                    list_buffer = ['<ul>']

                list_item_content = list_match.group(1)
                list_buffer.append(f'<li>{list_item_content}</li>')
            else:
                if in_list:
                    list_buffer.append('</ul>')
                    result_lines.append('\n'.join(list_buffer))
                    in_list = False

                result_lines.append(line)

        if in_list:
            list_buffer.append('</ul>')
            result_lines.append('\n'.join(list_buffer))

        body = '\n'.join(result_lines)

        # Create a unique ID for this annotation
        annotation_id = f"annotation_{uuid.uuid4().hex[:8]}"

        # Add to list of annotations for this paragraph
        annotation_html = f'<div id="{annotation_id}" class="annotation-content">'
        # annotation_html += f'<div class="annotation-header">{header}</div>'
        annotation_html += f'<div class="annotation-body">{body}</div>'
        annotation_html += f'</div>'
        paragraph_annotations.append(annotation_html)

        # Return only the highlighted text with its data attribute
        html = f'<span class="annotated" data-annotation-id="{annotation_id}">{annotated_text}</span>'
        return html

    # Process all annotations
    processed = re.sub(pattern, replace_annotation, text)

    # Now convert regular markdown links (after processing annotations)
    processed = re.sub(r'\[([^\]]+)\]\(([^)]+)\)',
                       r'<a href="\2" target="_blank">\1</a>', processed)

    # Convert markdown headings (###) to <h3>
    processed = re.sub(r'^###\s+(.*)$', r'<h3>\1</h3>',
                       processed, flags=re.MULTILINE)

    # Process unordered lists
    lines = processed.split('\n')
    in_list = False
    list_buffer = []
    result_lines = []

    for line in lines:
        # Check if line is a list item (starts with *, -, or + followed by space)
        list_match = re.match(r'^[*\-+]\s+(.*)$', line)

        if list_match:
            if not in_list:
                # Start a new list
                in_list = True
                list_buffer = ['<ul>']

            # Add the list item
            list_item_content = list_match.group(1)
            list_buffer.append(f'<li>{list_item_content}</li>')
        else:
            # Not a list item
            if in_list:
                # End the current list
                list_buffer.append('</ul>')
                result_lines.append('\n'.join(list_buffer))
                in_list = False

            # Add the regular line
            result_lines.append(line)

    # If we're still in a list at the end, close it
    if in_list:
        list_buffer.append('</ul>')
        result_lines.append('\n'.join(list_buffer))

    processed = '\n'.join(result_lines)

    # Add the annotations at the end of the paragraph
    if paragraph_annotations:
        processed += '\n<div class="paragraph-annotations">'
        for annotation in paragraph_annotations:
            processed += annotation
        processed += '</div>'

    # Convert line breaks to <br> tags within paragraphs
    processed = re.sub(r'\n\n', '<!--PARA-->', processed)
    processed = re.sub(r'\n', '<br>', processed)
    processed = re.sub(r'<!--PARA-->', '\n\n', processed)

    return processed


def generate_html(parsed_data):
    """Generate the complete HTML document."""

    # Double the curly braces in the template to escape them for Python's string formatting
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

        ul {{
            margin-top: 0rem;
            margin-bottom: 0rem;
            padding-left: 1.5rem;
        }}
        
        li {{
            margin-bottom: 0rem;
        }}
        
        p + ul {{
            margin-top: -0.5rem;  /* Reduce space between a paragraph and the list that follows it */
        }}
        
        ul + p {{
            margin-top: 0.8rem;  /* Adjust space between a list and the paragraph that follows */
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
        
        .paragraph-annotations {{
            margin-top: 1rem;
            padding-top: 1rem;
        }}
        
        .annotation-content {{
            display: none;
            margin: 0.5rem 0;
            padding: 1rem;
            background-color: #f5f5f5;
            border-left: 4px solid #1976d2;
            font-size: 0.9em;
            line-height: 1.6;
            border-radius: 0 4px 4px 0;
        }}
        
        .annotation-content.show {{
            display: block;
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
            text-align: left;
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
        
        .annotation-wrapper {{
            display: inline-block;
            position: relative;
        }}

        /* Byline styles */
        .byline {{
            text-align: center;
            margin: -1rem 0 2rem 0;
            font-size: 0.9em;
            color: #666;
            font-style: italic;
        }}
        
        .byline-expanded {{
            display: inline-block;
            position: relative;
        }}
        
        .byline-expanded .details {{
            position: absolute;
            top: 100%;
            left: 50%;
            transform: translateX(-50%);
            margin-top: 0.2rem;
            padding: 1rem;
            background: white;
            border: 1px solid #e0e0e0;
            border-radius: 4px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            width: 300px;
            opacity: 0;
            visibility: hidden;
            transition: opacity 0.2s;
            z-index: 10;
            font-style: normal;
            text-align: left;
            line-height: 1.4;
        }}
        
        .byline-expanded:hover .details {{
            opacity: 1;
            visibility: visible;
        }}

        /* This creates the invisible bridge */
        .byline-expanded::before {{
            content: '';
            position: absolute;
            top: 100%;
            left: 50%;
            transform: translateX(-50%);
            width: 320px;
            height: 20px;
            z-index: 9;
        }}

        /* And these transition delays help with timing */
        .byline-expanded .details {{
            transition-delay: 0.3s;  /* Delay before hiding */
        }}

        .byline-expanded:hover .details {{
            transition-delay: 0s;  /* No delay when showing */
        }}
        
        .byline-link {{
            color: #666;
            text-decoration: none;
            border-bottom: 1px dotted #999;
            cursor: pointer;
        }}
        
        .byline-link:hover {{
            color: #1976d2;
            border-bottom-color: #1976d2;
        }}

        .instructions details {{
            margin-top: 0.5rem;
            background: rgba(255, 255, 255, 0.4);
            padding: 0.75rem 1rem;
            border-radius: 4px;
        }}
        
        .instructions summary {{
            cursor: pointer;
            font-weight: bold;
            color: #704300;
            list-style: none;
            position: relative;
            padding-left: 1.5rem;
            user-select: none;
        }}
        
        .instructions summary::-webkit-details-marker {{
            display: none;
        }}
        
        .instructions summary::before {{
            content: '▶';
            position: absolute;
            left: 0;
            transition: transform 0.2s;
            font-size: 0.8em;
        }}
        
        .instructions details[open] summary::before {{
            transform: rotate(90deg);
        }}
        
        .instructions details[open] summary {{
            margin-bottom: 0.5rem;
        }}
        
        .instructions details p {{
            margin: 0.5rem 0;
            text-align: left;
            line-height: 1.6;
        }}
        
        .instructions details p:first-of-type {{
            margin-top: 0;
        }}

        .instruction-links {{
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            margin-top: 0.5rem;
        }}
        
        .instruction-link {{
            display: inline-block;
            padding: 0.5rem 1.25rem;
            background: rgba(255, 255, 255, 0.6);
            color: #704300;
            text-decoration: none;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: 500;
            transition: all 0.2s ease;
            border: 1px solid rgba(133, 100, 4, 0.2);
        }}
        
        .instruction-link:hover {{
            background: rgba(255, 255, 255, 0.9);
            transform: translateY(-1px);
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            color: #5a3600;
            border-color: rgba(133, 100, 4, 0.3);
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{title}</h1>
        
        <div class="byline">
            <span class="byline-expanded">
                annotated by <span class="byline-link">Miles Kodama</span>
                <div class="details">
                    I'm <a href="https://www.mkodama.org">Miles</a>, I research AI policy, and I created this site to help the public understand SB 53.<br><br>
                    If you find an error or have a suggestion, you can <a href="mailto:milesmkodama@gmail.com">send me an email</a> or message me on Signal @mileskodama.21
                </div>
            </span>
        </div>
        
        {instructions_html}
        
        {sections_html}
    </div>
    
    <script>
        document.querySelectorAll('.annotated').forEach(element => {{
            element.addEventListener('click', function(e) {{
                e.stopPropagation();
                
                // Get the annotation ID from the data attribute
                const annotationId = this.getAttribute('data-annotation-id');
                const annotation = document.getElementById(annotationId);
                
                if (annotation) {{
                    // Toggle visibility with class for styling
                    annotation.classList.toggle('show');
                    this.classList.toggle('expanded');
                    
                    // Scroll to the annotation if it's not in view
                    if (annotation.classList.contains('show')) {{
                        const rect = annotation.getBoundingClientRect();
                        const isInViewport = 
                            rect.top >= 0 &&
                            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight);
                            
                        if (!isInViewport) {{
                            annotation.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                        }}
                    }}
                    
                    // Close other annotations
                    document.querySelectorAll('.annotation-content.show').forEach(other => {{
                        if (other.id !== annotationId) {{
                            other.classList.remove('show');
                            // Find and remove expanded class from the triggering element
                            const otherTrigger = document.querySelector('[data-annotation-id="' + other.id + '"]');
                            if (otherTrigger) otherTrigger.classList.remove('expanded');
                        }}
                    }});
                }}
            }});
        }});
        
        // Click anywhere else to close annotations
        document.addEventListener('click', function(e) {{
            // Only close annotations if the click is not on an annotation content or annotated text
            if (!e.target.closest('.annotation-content') && !e.target.closest('.annotated')) {{
                document.querySelectorAll('.annotation-content.show').forEach(annotation => {{
                    annotation.classList.remove('show');
                    const trigger = document.querySelector('[data-annotation-id="' + annotation.id + '"]');
                    if (trigger) trigger.classList.remove('expanded');
                }});
            }}
        }});
        
        // Add event listeners to prevent clicks inside annotations from bubbling up
        document.querySelectorAll('.annotation-content').forEach(annotation => {{
            annotation.addEventListener('click', function(e) {{
                e.stopPropagation();
            }});
        }});
    </script>
</body>
</html>'''

    # Generate instructions HTML if present
    instructions_html = ''
    if parsed_data['instructions']:
        instructions_html = f'''<div class="instructions">
        <p style="text-align: center; margin: 0 0 1rem 0;">{parsed_data["instructions"]}</p>
        <div class="instruction-links">
            <a href="summary" class="instruction-link">Summary</a>
            <a href="faq" class="instruction-link">FAQs</a>
        </div>
    </div>'''

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
