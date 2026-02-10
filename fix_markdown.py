#!/usr/bin/env python3
"""
Fix markdown spacing issues while preserving code blocks and technical terms.
"""

import re


def fix_markdown_spacing(content):
    """Fix spacing issues in markdown while protecting code blocks."""

    lines = content.split('\n')
    fixed_lines = []

    for line in lines:
        # Fix variable names in curly braces (like {current User} -> {currentUser})
        line = re.sub(r'\{current User\}', '{currentUser}', line)
        line = re.sub(r'\{current Object\}', '{currentObject}', line)
        line = re.sub(r'\{current Origin\}', '{currentOrigin}', line)
        line = re.sub(r'\{user Relation\}', '{userRelation}', line)
        line = re.sub(r'\{from Workflow State\}', '{fromWorkflowState}', line)
        line = re.sub(r'\{to Workflow State\}', '{toWorkflowState}', line)
        line = re.sub(r'\{constant Id Pool', '{constantIdPool', line)
        line = re.sub(r'\{current Utc Date Time\}', '{currentUtcDateTime}', line)
        line = re.sub(r'\{current Utc Date\}', '{currentUtcDate}', line)
        line = re.sub(r'\{current User Origin\}', '{currentUserOrigin}', line)

        # Fix function names that got split
        line = re.sub(r'\.target Object\(', '.targetObject(', line)
        line = re.sub(r'\.user Relation\(', '.userRelation(', line)
        line = re.sub(r'\.path Name\(', '.pathName(', line)

        # Skip lines that are code (backticks) or in tables with code
        if '`' in line:
            # Protect content in backticks from modification
            parts = re.split(r'(`[^`]*`)', line)
            fixed_parts = []
            for part in parts:
                if part.startswith('`') and part.endswith('`'):
                    # This is code - restore proper camelCase
                    part = part.replace('current User', 'currentUser')
                    part = part.replace('current Object', 'currentObject')
                    part = part.replace('current Origin', 'currentOrigin')
                    part = part.replace('user Relation', 'userRelation')
                    part = part.replace('from Workflow State', 'fromWorkflowState')
                    part = part.replace('to Workflow State', 'toWorkflowState')
                    part = part.replace('constant Id Pool', 'constantIdPool')
                    part = part.replace('current Utc Date', 'currentUtcDate')
                    part = part.replace('current Utc Date Time', 'currentUtcDateTime')
                    part = part.replace('current User Origin', 'currentUserOrigin')
                    part = part.replace('keep Origin', 'keepOrigin')
                    part = part.replace('keep User Origin', 'keepUserOrigin')
                    part = part.replace('target Object', 'targetObject')
                    part = part.replace('relation Type Key', 'relationTypeKey')
                    part = part.replace('user Relation Type Key', 'userRelationTypeKey')
                    part = part.replace('attribute Key', 'attributeKey')
                    part = part.replace('object Type Key', 'objectTypeKey')
                    part = part.replace('path Name', 'pathName')
                    part = part.replace('current Obhject', 'currentObject')
                    part = part.replace('is Mentioned', 'isMentioned')
                fixed_parts.append(part)
            line = ''.join(fixed_parts)

        # Fix concatenated words outside of code blocks
        line = re.sub(r'in Select Streams is', 'in Select Streams is', line)
        line = re.sub(r'innotification', 'in notification', line)
        line = re.sub(r'intended for the Send Notification', 'intended for the Send Notification', line)

        # Fix parameter names in quotes that got split
        line = re.sub(r"'relation Type Key'", "'relationTypeKey'", line)
        line = re.sub(r"'user Relation Type Key'", "'userRelationTypeKey'", line)
        line = re.sub(r"'attribute Key'", "'attributeKey'", line)
        line = re.sub(r"'object Type Key'", "'objectTypeKey'", line)

        # Fix parenthetical parameter references
        line = re.sub(r'\( `relation Type Key`', '( `relationTypeKey`', line)
        line = re.sub(r'\( `user Relation Type Key`', '( `userRelationTypeKey`', line)
        line = re.sub(r'\( `attribute Key`', '( `attributeKey`', line)
        line = re.sub(r'\( `object Type Key`', '( `objectTypeKey`', line)
        line = re.sub(r'`user Relation Type Key`', '`userRelationTypeKey`', line)
        line = re.sub(r'`userRelation Type Key`', '`userRelationTypeKey`', line)

        # Fix missing spaces before bold markers and concatenated words
        line = re.sub(r'variables\*\*must', 'variables **must', line)
        line = re.sub(r'streams\*\*select', 'streams **select', line)
        line = re.sub(r'variable\*\*can', 'variable **can', line)
        line = re.sub(r'they\*\*must', 'they **must', line)
        line = re.sub(r'return\*\*a', 'return **a', line)
        line = re.sub(r'referenceselectors', 'reference selectors', line)
        line = re.sub(r'selectorsspecify', 'selectors specify', line)

        # Fix double/misplaced bold markers
        line = re.sub(r'\*\*\*\*', '', line)  # Remove quadruple asterisks

        # Fix missing space after = in list items
        line = re.sub(r'=Returns', '= Returns', line)

        # Fix specific spacing issues
        line = re.sub(r'define\*\*what', 'define **what', line)
        line = re.sub(r'retrieve\*\*from', 'retrieve **from', line)
        line = re.sub(r'and\*\*return', 'and **return', line)

        # Clean up extra spaces in table cells
        line = re.sub(r'  +', ' ', line)

        fixed_lines.append(line)

    return '\n'.join(fixed_lines)


def main():
    file_path = r'C:\Users\mylip\OneDrive\Documents\GitHub\mylinhpb.github.io\_articles\context-variables-and-selectors.md'

    print(f'Reading {file_path}...')
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print('Fixing spacing issues...')
    fixed_content = fix_markdown_spacing(content)

    print(f'Writing back to {file_path}...')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(fixed_content)

    print('Done!')


if __name__ == '__main__':
    main()
