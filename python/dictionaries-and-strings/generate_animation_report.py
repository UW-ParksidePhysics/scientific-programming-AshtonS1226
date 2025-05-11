def parse_animation_code(code_filename):
    """Reads code from a file and wraps it in <pre> HTML tags."""
    with open(code_filename, 'r') as file:
        code = file.read()
    preformatted_code = f"<pre>\n{code}\n</pre>"
    return preformatted_code

def format_section_header(header_string):
    """Wraps a string in <h1> tags for section headers."""
    return f"<h1>{header_string}</h1>"

def write_html_report(report_string, report_filename):
    """Writes the full HTML report to a file."""
    with open(report_filename, 'w') as file:
        file.write(report_string)

if __name__ == '__main__':
    code_file = 'animate_wavepacket.py'
    report_file = 'animation_report.html'

    # Start building HTML content
    html_content = "<html><head><title>Wave Packet Animation Report</title></head><body>\n"

    # Section 1: Code
    html_content += format_section_header("1. Source Code: animate_wavepacket.py")
    html_content += parse_animation_code(code_file)

    # Section 2: Static Plots
    html_content += format_section_header("2. Wave Packet Plots at Different Times")
    for t_str in ['t0.png', 't1.png', 't2.png']:
        html_content += f'<img src="{t_str}" alt="Wave packet at {t_str}"><br>\n'

    # Section 3: Animation
    html_content += format_section_header("3. Animated Wave Packet")
    html_content += '<img src="wavepacket.gif" alt="Wave packet animation"><br>\n'

    # End of HTML
    html_content += "</body></html>"

    # Write out the report
    write_html_report(html_content, report_file)
    print(f"HTML report written to {report_file}")

# A lot of this part was ChatGPT. I kept getting stuck at so many parts and couldn't get my code running without errors