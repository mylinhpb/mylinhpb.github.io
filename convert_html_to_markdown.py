#!/usr/bin/env python3
"""
Convert HTML content to clean Markdown format.
Handles tables, headings, lists, callouts, and inline styles.
"""

import re
from bs4 import BeautifulSoup, NavigableString, Tag


def clean_text(text):
    """Clean up text content."""
    if not text:
        return ''
    # Replace non-breaking spaces
    text = text.replace('\xa0', ' ')
    text = text.replace('&nbsp;', ' ')
    # Clean up multiple spaces
    text = re.sub(r' +', ' ', text)
    return text.strip()


def is_callout_table(table):
    """Check if a table is a callout box."""
    rows = table.find_all('tr')
    if len(rows) != 1:
        return False
    cells = rows[0].find_all(['td', 'th'])
    if len(cells) != 1:
        return False

    cell = cells[0]
    style = cell.get('style', '')
    # Check for background color indicating callout
    if 'background-color' in style:
        return True
    return False


def get_callout_type(cell_content):
    """Determine callout type from content."""
    content_upper = cell_content.upper()
    if 'IMPORTANT' in content_upper:
        return 'IMPORTANT'
    elif 'WARNING' in content_upper:
        return 'WARNING'
    elif 'NOTE' in content_upper or 'TIP' in content_upper:
        return 'NOTE'
    else:
        return 'NOTE'


def process_inline_element(elem):
    """Process inline elements like code, strong, links, etc."""
    if isinstance(elem, NavigableString):
        text = clean_text(str(elem))
        # Add space after text if it doesn't end with one
        if text and not text.endswith(' '):
            return text + ' '
        return text

    if isinstance(elem, Tag):
        if elem.name == 'code':
            return f'`{clean_text(elem.get_text())}` '
        elif elem.name == 'strong' or (elem.name == 'span' and 'font-weight: 600' in elem.get('style', '')):
            inner = ''.join(process_inline_element(child) for child in elem.children).strip()
            return f'**{inner}** '
        elif elem.name == 'a':
            href = elem.get('href', '')
            text = clean_text(elem.get_text())
            # Skip internal anchor links
            if href.startswith('#') or not href or '/data-governance/' in href:
                return text + ' '
            return f'[{text}]({href}) '
        elif elem.name == 'br':
            return ' '
        elif elem.name == 'img':
            return ''  # Skip images
        elif elem.name == 'span':
            # Just extract text from spans (they usually have inline styles we want to ignore)
            return ''.join(process_inline_element(child) for child in elem.children)
        else:
            # Recurse for other tags
            return ''.join(process_inline_element(child) for child in elem.children)

    return ''


def convert_table_to_markdown(table):
    """Convert HTML table to Markdown table."""
    # Check if it's a callout box
    if is_callout_table(table):
        cell = table.find('td') or table.find('th')
        content = []

        for child in cell.children:
            if isinstance(child, NavigableString):
                text = clean_text(str(child))
                if text:
                    content.append(text)
            elif isinstance(child, Tag):
                if child.name == 'p':
                    text = process_inline_element(child)
                    if text:
                        content.append(text)
                else:
                    text = process_inline_element(child)
                    if text:
                        content.append(text)

        callout_type = get_callout_type(' '.join(content))

        # Filter out the callout type label from content
        filtered_content = []
        for line in content:
            # Remove lines that are just the callout type
            if not re.match(r'^\s*(IMPORTANT|WARNING|NOTE|TIP)[!\s]*$', line, re.IGNORECASE):
                # Remove inline callout labels
                line = re.sub(r'\*\*\s*(IMPORTANT|WARNING|NOTE|TIP)[!\s]*\*\*\s*', '', line, flags=re.IGNORECASE)
                line = re.sub(r'^\s*(IMPORTANT|WARNING|NOTE|TIP)[!\s]*\s*', '', line, flags=re.IGNORECASE)
                if line.strip():
                    filtered_content.append(line)

        result = f'\n> [!{callout_type}]\n'
        for line in filtered_content:
            result += f'> {line}\n'
        result += '\n'
        return result

    # Regular table
    rows = table.find_all('tr')
    if not rows:
        return ''

    table_data = []
    for row in rows:
        cells = row.find_all(['td', 'th'])
        row_data = []
        for cell in cells:
            # Process cell content
            cell_content = []
            for child in cell.children:
                if isinstance(child, NavigableString):
                    text = clean_text(str(child))
                    if text:
                        cell_content.append(text)
                elif isinstance(child, Tag):
                    if child.name == 'p':
                        text = process_inline_element(child).strip()
                        if text:
                            cell_content.append(text)
                    elif child.name == 'table':
                        # Nested table (like callout in cell) - convert to callout
                        nested_md = convert_table_to_markdown(child)
                        if nested_md:
                            # Remove the newlines and format as inline
                            nested_md = nested_md.strip().replace('\n', ' ')
                            cell_content.append(nested_md)
                    else:
                        text = process_inline_element(child).strip()
                        if text:
                            cell_content.append(text)

            cell_text = ' '.join(cell_content)
            # Clean up multiple spaces
            cell_text = re.sub(r' {2,}', ' ', cell_text).strip()
            row_data.append(cell_text)

        if row_data:
            table_data.append(row_data)

    if not table_data:
        return ''

    # Build markdown table
    result = '\n'
    for i, row in enumerate(table_data):
        result += '| ' + ' | '.join(row) + ' |\n'
        if i == 0:  # Add separator after header
            result += '| ' + ' | '.join(['---'] * len(row)) + ' |\n'
    result += '\n'
    return result


def convert_list_to_markdown(list_elem, indent_level=0):
    """Convert HTML list to Markdown list."""
    result = []
    indent = '  ' * indent_level
    is_ordered = list_elem.name == 'ol'

    items = list_elem.find_all('li', recursive=False)
    for i, item in enumerate(items):
        prefix = f'{indent}1. ' if is_ordered else f'{indent}- '

        # Process item content
        item_content = []
        for child in item.children:
            if isinstance(child, NavigableString):
                text = clean_text(str(child))
                if text:
                    item_content.append(text)
            elif isinstance(child, Tag):
                if child.name in ['ul', 'ol']:
                    # Nested list
                    nested = convert_list_to_markdown(child, indent_level + 1)
                    item_content.append('\n' + nested)
                else:
                    text = process_inline_element(child)
                    if text:
                        item_content.append(text)

        if item_content:
            result.append(prefix + ' '.join(item_content))

    return '\n'.join(result)


def convert_html_to_markdown(html_content):
    """Convert HTML to Markdown."""
    soup = BeautifulSoup(html_content, 'html.parser')
    result = []

    # Process all top-level elements
    for elem in soup.children:
        if isinstance(elem, NavigableString):
            text = clean_text(str(elem))
            if text:
                result.append(text)
        elif isinstance(elem, Tag):
            if elem.name == 'h2':
                text = clean_text(elem.get_text())
                result.append(f'\n## {text}\n')
            elif elem.name == 'h3':
                text = clean_text(elem.get_text())
                result.append(f'\n### {text}\n')
            elif elem.name == 'h4':
                text = clean_text(elem.get_text())
                result.append(f'\n#### {text}\n')
            elif elem.name == 'p':
                text = process_inline_element(elem).strip()
                if text:
                    # Clean up multiple spaces
                    text = re.sub(r' {2,}', ' ', text)
                    result.append(f'{text}\n')
            elif elem.name in ['ul', 'ol']:
                list_md = convert_list_to_markdown(elem)
                if list_md:
                    result.append(f'\n{list_md}\n')
            elif elem.name == 'table':
                table_md = convert_table_to_markdown(elem)
                if table_md:
                    result.append(table_md)
            elif elem.name == 'br':
                result.append('\n')

    # Join and clean up
    markdown = ''.join(result)
    # Clean up multiple spaces
    markdown = re.sub(r' {2,}', ' ', markdown)
    # Clean up multiple newlines
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)
    # Clean up spaces before newlines
    markdown = re.sub(r' +\n', '\n', markdown)
    # Clean up spaces after newlines (except for blockquotes)
    markdown = re.sub(r'\n (?!>)', '\n', markdown)
    return markdown.strip()


def convert_file(input_path):
    """Convert HTML file to Markdown."""
    print(f'Reading {input_path}...')

    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check for front matter
    front_matter = ''
    main_content = content

    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            front_matter = f'---{parts[1]}---\n\n'
            main_content = parts[2].strip()

    print('Converting HTML to Markdown...')

    # Convert HTML to Markdown
    markdown_content = convert_html_to_markdown(main_content)

    # Combine front matter with converted content
    final_content = front_matter + markdown_content

    # Write to output
    print(f'Writing cleaned Markdown to {input_path}...')
    with open(input_path, 'w', encoding='utf-8') as f:
        f.write(final_content)

    print('Conversion complete!')


if __name__ == '__main__':
    input_file = r'C:\Users\mylip\OneDrive\Documents\GitHub\mylinhpb.github.io\_articles\context-variables-and-selectors.md'
    convert_file(input_file)
