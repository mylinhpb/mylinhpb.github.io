#!/usr/bin/env python3
"""
Convert HTML content to clean Markdown format - Version 2.
Handles tables, headings, lists, callouts, and inline styles with better spacing.
"""

import re
from bs4 import BeautifulSoup, NavigableString, Tag


def normalize_whitespace(text):
    """Normalize whitespace in text."""
    if not text:
        return ''
    # Replace non-breaking spaces and HTML entities
    text = text.replace('\xa0', ' ')
    text = text.replace('&nbsp;', ' ')
    # Normalize multiple spaces to single space
    text = re.sub(r'[ \t]+', ' ', text)
    # Remove spaces at start/end of lines
    text = '\n'.join(line.strip() for line in text.split('\n'))
    return text


def extract_text_with_formatting(elem, preserve_formatting=True):
    """
    Extract text from an element while preserving inline formatting.
    Returns a string with markdown formatting.
    """
    if elem is None:
        return ''

    if isinstance(elem, NavigableString):
        return str(elem)

    if not isinstance(elem, Tag):
        return ''

    result = []
    prev_was_tag = False

    for child in elem.children:
        if isinstance(child, NavigableString):
            text = str(child)
            # Add space before text if previous was a tag and text doesn't start with space/punctuation
            if prev_was_tag and text and not text[0].isspace() and text[0] not in '.,;:!?':
                result.append(' ')
            result.append(text)
            prev_was_tag = False
        elif isinstance(child, Tag):
            # Add space before tag if previous was a tag
            if prev_was_tag:
                result.append(' ')

            if child.name == 'br':
                result.append(' ')
                prev_was_tag = True
            elif child.name == 'code':
                text = normalize_whitespace(child.get_text())
                result.append(f'`{text}`')
                prev_was_tag = True
            elif child.name == 'strong' or (child.name == 'span' and 'font-weight: 600' in child.get('style', '')):
                inner_text = extract_text_with_formatting(child, preserve_formatting=True)
                inner_text = normalize_whitespace(inner_text)
                if inner_text:
                    result.append(f'**{inner_text}**')
                    prev_was_tag = True
            elif child.name == 'a':
                href = child.get('href', '')
                link_text = normalize_whitespace(child.get_text())
                # Skip internal/anchor links and specific domain links
                if href and not href.startswith('#') and '/data-governance/' not in href:
                    result.append(f'[{link_text}]({href})')
                else:
                    result.append(link_text)
                prev_was_tag = True
            elif child.name == 'img':
                # Skip images
                continue
            elif child.name == 'span':
                # Extract text from span (ignoring inline styles)
                inner_text = extract_text_with_formatting(child, preserve_formatting=True)
                result.append(inner_text)
                prev_was_tag = True
            else:
                # Recurse for other inline elements
                inner_text = extract_text_with_formatting(child, preserve_formatting=True)
                result.append(inner_text)
                prev_was_tag = True

    text = ''.join(result)
    return text


def is_callout_table(table):
    """Check if a table is a callout box (single cell with background color)."""
    rows = table.find_all('tr', recursive=False)
    if len(rows) != 1:
        return False
    cells = rows[0].find_all(['td', 'th'], recursive=False)
    if len(cells) != 1:
        return False
    cell = cells[0]
    style = cell.get('style', '')
    return 'background-color' in style


def detect_callout_type(content):
    """Detect the type of callout based on content."""
    content_upper = content.upper()
    if 'IMPORTANT' in content_upper:
        return 'IMPORTANT'
    elif 'WARNING' in content_upper:
        return 'WARNING'
    elif 'NOTE' in content_upper or 'TIP' in content_upper:
        return 'NOTE'
    return 'NOTE'


def convert_callout_table(table):
    """Convert a callout table to markdown callout."""
    cell = table.find('td') or table.find('th')
    if not cell:
        return ''

    lines = []
    for child in cell.children:
        if isinstance(child, NavigableString):
            text = normalize_whitespace(str(child))
            if text:
                lines.append(text)
        elif isinstance(child, Tag):
            if child.name == 'p':
                text = extract_text_with_formatting(child)
                text = normalize_whitespace(text)
                if text:
                    lines.append(text)
            elif child.name == 'table':
                # Skip nested tables in callouts
                continue
            else:
                text = extract_text_with_formatting(child)
                text = normalize_whitespace(text)
                if text:
                    lines.append(text)

    if not lines:
        return ''

    # Detect callout type and filter content
    callout_type = detect_callout_type(' '.join(lines))

    # Filter out callout type labels
    filtered_lines = []
    for line in lines:
        # Skip lines that are just the callout indicator
        if re.match(r'^\s*(IMPORTANT|WARNING|NOTE|TIP)!?\s*$', line, re.IGNORECASE):
            continue
        # Remove callout indicators from the start of lines
        line = re.sub(r'^\s*(IMPORTANT|WARNING|NOTE|TIP)!?\s*', '', line, flags=re.IGNORECASE)
        if line.strip():
            filtered_lines.append(line)

    if not filtered_lines:
        return ''

    # Build callout
    result = f'\n> [!{callout_type}]\n'
    for line in filtered_lines:
        result += f'> {line}\n'
    result += '\n'

    return result


def convert_regular_table(table):
    """Convert a regular HTML table to markdown table."""
    rows = table.find_all('tr', recursive=False)
    if not rows:
        return ''

    table_data = []

    for row in rows:
        cells = row.find_all(['td', 'th'], recursive=False)
        row_data = []

        for cell in cells:
            cell_parts = []

            for child in cell.children:
                if isinstance(child, NavigableString):
                    text = normalize_whitespace(str(child))
                    if text:
                        cell_parts.append(text)
                elif isinstance(child, Tag):
                    if child.name == 'p':
                        text = extract_text_with_formatting(child)
                        text = normalize_whitespace(text)
                        if text:
                            cell_parts.append(text)
                    elif child.name == 'table':
                        # Handle nested callout tables
                        if is_callout_table(child):
                            nested_callout = convert_callout_table(child)
                            # Convert callout to inline text for table cell
                            if nested_callout:
                                # Extract text from callout
                                callout_lines = [line.lstrip('> ') for line in nested_callout.split('\n') if line.startswith('>')]
                                cell_parts.extend(callout_lines)
                    else:
                        text = extract_text_with_formatting(child)
                        text = normalize_whitespace(text)
                        if text:
                            cell_parts.append(text)

            cell_text = ' '.join(cell_parts)
            cell_text = normalize_whitespace(cell_text)
            row_data.append(cell_text)

        if row_data:
            table_data.append(row_data)

    if not table_data:
        return ''

    # Build markdown table
    result = '\n'
    for i, row in enumerate(table_data):
        result += '| ' + ' | '.join(row) + ' |\n'
        if i == 0:  # Header separator
            result += '| ' + ' | '.join(['---'] * len(row)) + ' |\n'
    result += '\n'

    return result


def convert_list(list_elem, indent_level=0):
    """Convert HTML list (ul/ol) to markdown list."""
    if not list_elem:
        return ''

    lines = []
    indent = '  ' * indent_level
    is_ordered = list_elem.name == 'ol'

    items = list_elem.find_all('li', recursive=False)

    for item in items:
        # Get the list item prefix
        prefix = f'{indent}1. ' if is_ordered else f'{indent}- '

        item_parts = []
        for child in item.children:
            if isinstance(child, NavigableString):
                text = normalize_whitespace(str(child))
                if text:
                    item_parts.append(text)
            elif isinstance(child, Tag):
                if child.name in ['ul', 'ol']:
                    # Nested list - add it after the current item
                    nested = convert_list(child, indent_level + 1)
                    if nested:
                        lines.append(prefix + ' '.join(item_parts))
                        lines.append(nested.rstrip('\n'))
                        item_parts = []  # Clear parts since we've added them
                    break
                else:
                    text = extract_text_with_formatting(child)
                    text = normalize_whitespace(text)
                    if text:
                        item_parts.append(text)

        if item_parts:
            item_text = ' '.join(item_parts)
            lines.append(prefix + item_text)

    return '\n'.join(lines)


def convert_html_to_markdown(html_content):
    """Main conversion function from HTML to Markdown."""
    soup = BeautifulSoup(html_content, 'html.parser')

    output = []

    # Process each top-level element
    for elem in soup.children:
        if isinstance(elem, NavigableString):
            text = normalize_whitespace(str(elem))
            if text:
                output.append(text)
        elif isinstance(elem, Tag):
            if elem.name == 'h2':
                text = normalize_whitespace(elem.get_text())
                output.append(f'\n## {text}\n')
            elif elem.name == 'h3':
                text = normalize_whitespace(elem.get_text())
                output.append(f'\n### {text}\n')
            elif elem.name == 'h4':
                text = normalize_whitespace(elem.get_text())
                output.append(f'\n#### {text}\n')
            elif elem.name == 'p':
                text = extract_text_with_formatting(elem)
                text = normalize_whitespace(text)
                if text:
                    output.append(f'{text}\n')
            elif elem.name in ['ul', 'ol']:
                list_md = convert_list(elem)
                if list_md:
                    output.append(f'\n{list_md}\n')
            elif elem.name == 'table':
                if is_callout_table(elem):
                    callout_md = convert_callout_table(elem)
                    if callout_md:
                        output.append(callout_md)
                else:
                    table_md = convert_regular_table(elem)
                    if table_md:
                        output.append(table_md)
            elif elem.name == 'br':
                output.append('\n')

    # Join and clean up
    markdown = ''.join(output)

    # Final cleanup
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)  # Max 2 newlines
    markdown = re.sub(r' +\n', '\n', markdown)  # Remove trailing spaces

    # Fix common concatenation issues from HTML - but preserve code/variable names in backticks
    # Only fix specific problematic patterns that are NOT code
    markdown = re.sub(r'\*\* \*\*', '** **', markdown)  # Fix double bold markers
    markdown = re.sub(r'``+', '', markdown)  # Remove empty code blocks

    # Fix specific known concatenation issues (not in code blocks)
    markdown = re.sub(r'inSelect Streams', 'in Select Streams', markdown)
    markdown = re.sub(r'in Select Streams([^`])', r'in Select Streams\1', markdown)
    markdown = re.sub(r'([^`])innotification', r'\1in notification', markdown)
    markdown = re.sub(r'theNotification', 'the Notification', markdown)
    markdown = re.sub(r'andSet', 'and Set', markdown)
    markdown = re.sub(r'theSend', 'the Send', markdown)
    markdown = re.sub(r'for theSend', 'for the Send', markdown)
    markdown = re.sub(r' = Returns', ' = Returns', markdown)

    return markdown.strip()


def convert_file(file_path):
    """Convert HTML file to Markdown."""
    print(f'Reading {file_path}...')

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Handle front matter if present
    front_matter = ''
    main_content = content

    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            front_matter = f'---{parts[1]}---\n\n'
            main_content = parts[2].strip()

    print('Converting HTML to Markdown...')

    # Convert
    markdown = convert_html_to_markdown(main_content)

    # Combine with front matter
    final_content = front_matter + markdown

    # Write back
    print(f'Writing to {file_path}...')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_content)

    print('Conversion complete!')


if __name__ == '__main__':
    file_path = r'C:\Users\mylip\OneDrive\Documents\GitHub\mylinhpb.github.io\_articles\context-variables-and-selectors.md'
    convert_file(file_path)
