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
        # Hardcoded summary content
        summary_details = '''
            <details>
                <summary>SB 53 in a nutshell</summary>
                <p>In a nutshell, SB 53 says seven things. These are the four I consider most important:</p>
                <ul>
                    <li>Every large AI developer must write, publish, and follow a safety policy (§&nbsp;22757.12.a).</li>
                    <li>Every year starting in 2030, a large AI developer must get an independent auditor to verify that (1) they are following their own safety policy, and (2) the safety policy is clear enough that it's possible to determine whether the developer is following it (§ 22757.14).</li>
                    <li>Every frontier model released by a large AI developer must have a published model card (§&nbsp;22757.12.c)</li>
                    <li>A large AI developer is civilly liable if they break any of these rules (§&nbsp;22757.16).</li>
                </ul>
                <p>And these are the three major provisions that I expect will be less important:</p>
                <ul>
                    <li>The California Attorney General will operate an incident reporting system for critical incidents involving AI (§&nbsp;22757.13).</li>
                    <li>Whistleblower protections for large AI developers' employees and external partners are expanded (§ 1107).</li>
                    <li>California will explore building a public AI compute cluster to support socially beneficial AI research and innovation (§&nbsp;11546.8).</li>
                </ul>
                <p>Large AI developers are not currently mandated to adopt <strong>safety policies</strong>, but under SB 53, they would be. This wouldn&#39;t require most frontier developers to do anything qualitatively new, since they already have published safety policies, and they&#39;ve already made non-enforceable commitments to follow those policies. <a href="https://www-cdn.anthropic.com/f3b282f157017d08e36636bda1bf3bd4d9f23ee7.pdf">Anthropic</a>, <a href="https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf">OpenAI</a>, <a href="https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/updating-the-frontier-safety-framework/Frontier%20Safety%20Framework%202.0.pdf">Google DeepMind</a>, and <a href="https://ai.meta.com/static-resource/meta-frontier-ai-framework/?utm_source=newsroom&amp;utm_medium=web&amp;utm_content=Frontier_AI_Framework_PDF">Meta</a> have all written safety policies that satisfy many of the requirements in § 22757.12.a, and <a href="https://x.ai/documents/2025.02.20-RMF-Draft.pdf">xAI</a> has a draft safety policy that satisfies a few of the requirements. So if SB 53 were to pass, one industry laggard would have to write a safety policy for the first time, other frontier developers would have to make their existing safety policies more robust, and every frontier developer would be legally mandated to follow their own safety policy.</p>
                <p>Moreover, they must get an <strong>independent auditor</strong> to certify that they are following their safety policy, and this explicitly includes certifying that the safety policy is <em>clear enough</em> for it to be determinate whether the developer is complying with it. As far as is publicly known, no major AI developer has ever undergone a safety audit, but such audits are completely routine in other risky industries <a href="https://www.ecfr.gov/current/title-14/chapter-I/subchapter-G/part-121?toc=1">like aviation</a>. Every airline in the US is required to write a plan explaining what measures they will follow to ensure safety, and they must regularly commission independent audits to confirm that they&#39;re following the plan. SB 53 would require companies developing frontier AI systems to do the same.</p>
                <p>It is already a widely accepted best practice in the AI industry that when a company releases a new frontier model, they should publish a report called a <a href="https://arxiv.org/abs/1810.03993"><strong>model card</strong></a> describing the model&#39;s capabilities to consumers and to the scientific community. Anthropic, OpenAI, and Google DeepMind have consistently released model cards alongside all of their recent frontier models, and all three companies&#39; model cards likely comply with most of the requirements in SB 53. These cards generally explain how the developer assessed the risks posed by their model, how they intend to mitigate those risks, and whether their model reached any prespecified risk or capability thresholds. If the bill were to pass, the big three AI developers would have to disclose more detailed information about third party assessments run on their models, and developers like xAI that generally don&#39;t publish model cards would have to start publishing them.</p>
                <p>SB 53 would make large developers <strong>civilly liable</strong> for breaches of the above rules. No AI company executives will go to jail for failing to publish a safety policy or model card, but their companies can be faced with heavy fines—up to millions of dollars for a knowing violation of the law that causes material catastrophic risk. This is a major change from the <em>status quo</em>. Today, frontier AI developers have no legal obligation to disclose anything about their safety and security protocols to government, let alone to the public. When a company releases a new AI system more powerful than any system before, it is entirely optional under present law for them to tell consumers what dangerous things that system can do. And if a company does choose to adopt a safety policy or publish a model card, there is no force of law to guarantee the safety policy is being implemented or that the model card is accurate. This would all change under SB 53. We&#39;d no longer have to rely on AI developers&#39; good will to share critical safety information with the public.</p>
                <p>There is currently no official channel for the California state government to <strong>collect reports of safety incidents</strong> involving AI. If a frontier AI developer discovered tomorrow that the weights of their leading model had been stolen, the best they could do to alert state authorities would probably be to email the Attorney General&#39;s office. If a member of the public witnessed an AI autonomously causing harm in the wild, the fastest way for them to tell the authorities would probably be to tweet about it. SB 53 would replace these slow, informal information channels with an official incident reporting mechanism run by the AG. Just like California has an <a href="https://oag.ca.gov/privacy/databreach/reporting">official website to collect</a> reports of data breaches, there would be another site for reports of critical AI safety incidents.</p>
                <p><a href="https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=LAB&amp;sectionNum=1102.5">Existing California law</a> already offers <strong>whistleblower protection</strong> to AI company employees who report a violation of federal, state, or local law to public officials or to their superiors. Companies may not make rules or enforce contracts that would prevent their employees from blowing the whistle, nor can they retaliate against an employee who becomes a whistleblower. SB 53 expands the scope of these protections in two ways. First, it would grant whistleblower protection to actors who are currently not protected. Independent contractors, freelancers, unpaid advisors, and external groups that help developers to assess and manage catastrophic risk are not protected by existing law if they become whistleblowers, but they would be under SB 53. Second, the bill would protect disclosures of evidence that an AI developer&#39;s activities pose a catastrophic risk, whereas existing law only protects disclosures of evidence that a developer is breaking the law. Of course, many ways that a developer could cause a catastrophic risk would also involve breaking the law, but it&#39;s conceivable that a developer could do something catastrophically dangerous yet legal. It might also be easier for many would-be whistleblowers to tell whether their employer is causing a catastrophic risk than to tell whether their employer is breaking a specific law.</p>
                <p>Finally, SB 53 calls for California to build a <strong>publicly owned AI compute</strong> cluster called CalCompute. The cluster&#39;s purpose would be to support AI research and innovation for the public benefit. Nothing like CalCompute currently exists in California, but similar projects have been announced or are already underway in several other jurisdictions. New York has already built a compute cluster under their <a href="https://www.empireai.edu/">Empire AI</a> initiative, the UK has given academics compute access through its <a href="https://www.ukri.org/news/300-million-to-launch-first-phase-of-new-ai-research-resource">AI Research Resource</a>, and the US National Science Foundation&#39;s <a href="https://nairrpilot.org/">National AI Research Resource</a> aims to provide the same for American researchers. SB 53 does not specify how much funding California will put behind CalCompute, nor how many AI chips it aims to acquire, so it&#39;s hard to tell how much this section of the bill will accomplish. If CalCompute is funded generously in the next state budget, it could be a big deal, but if the project only gets a meager budget, it may not achieve much.</p>
            </details>
        '''
        
        instructions_html = f'''<div class="instructions">
            <p style="text-align: left; margin: 0 0 1rem 0;">{parsed_data["instructions"]}</p>
            {summary_details}
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
