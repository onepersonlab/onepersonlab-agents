#!/usr/bin/env python3
"""
Clean up Role Reference tables in SOUL.md files:
- Remove "Original Role" column
- Rename "OnePersonLab Role" to "Role"
- Keep only: Role | Agent ID
"""

import pathlib
import re

ROOT = pathlib.Path('/home/auto/.openclaw/workspace-taizi/onepersonlab-agents/agents')

def clean_role_reference(content):
    """Clean up Role Reference table in content"""
    
    # Pattern 1: Three-column table with Original Role
    # | Original Role | OnePersonLab Role | Agent ID |
    pattern_3col = re.compile(
        r'\| Original Role \| OnePersonLab Role \| Agent ID \|\n'
        r'\|-+\|-+\|-+\|\n'
        r'((?:\|[^|\n]+\|[^|\n]+\|[^|\n]+\|\n?)+)',
        re.MULTILINE
    )
    
    def replace_3col(match):
        rows = match.group(1).strip().split('\n')
        new_rows = []
        for row in rows:
            # Parse: | Original | OnePersonLab | AgentID |
            parts = [p.strip() for p in row.split('|') if p.strip()]
            if len(parts) >= 3:
                # Keep only OnePersonLab Role and Agent ID
                new_rows.append(f"| {parts[1]} | {parts[2]} |")
        return '| Role | Agent ID |\n|------|----------|\n' + '\n'.join(new_rows)
    
    content = pattern_3col.sub(replace_3col, content)
    
    # Pattern 2: Two-column table already correct but with wrong header
    # | OnePersonLab Role | Agent ID |
    pattern_2col_wrong_header = re.compile(
        r'\| OnePersonLab Role \| Agent ID \|\n'
        r'\|-+\|-+\|',
        re.MULTILINE
    )
    content = pattern_2col_wrong_header.sub('| Role | Agent ID |\n|------|----------|', content)
    
    # Pattern 3: Section title variations
    content = re.sub(
        r'## 🔬 OnePersonLab Role Reference',
        '## 🔬 Role Reference',
        content
    )
    
    return content

def process_file(filepath):
    """Process a single SOUL.md file"""
    content = filepath.read_text(encoding='utf-8')
    
    # Check if has Role Reference
    if 'Role Reference' not in content:
        print(f"  - {filepath.parent.name}: No Role Reference section")
        return False
    
    # Check if needs cleaning
    if '| Original Role |' not in content and '| OnePersonLab Role |' not in content:
        print(f"  - {filepath.parent.name}: Already clean")
        return False
    
    cleaned = clean_role_reference(content)
    filepath.write_text(cleaned, encoding='utf-8')
    print(f"  ✓ {filepath.parent.name}: Role Reference cleaned")
    return True

def main():
    print("🧹 Cleaning Role Reference tables in SOUL.md files")
    print("=" * 50)
    
    processed = 0
    for soul_file in ROOT.glob('*/SOUL.md'):
        if process_file(soul_file):
            processed += 1
    
    print("=" * 50)
    print(f"✅ Complete: {processed} agents updated")

if __name__ == '__main__':
    main()
