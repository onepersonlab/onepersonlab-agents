#!/usr/bin/env python3
"""
Bulk rename script for OnePersonLab terminology
OnePersonLab → OnePersonLab
Human User → Human User
"""

import pathlib

ROOT = pathlib.Path('/home/auto/.openclaw/workspace-taizi/onepersonlab-agents')

# Files to process
PATTERNS = ['**/*.md', '**/*.html', '**/*.sh', '**/*.py']
EXCLUDE = ['**/.git/**', '**/*.git/**']

# Replacements
REPLACEMENTS = [
    # Primary replacements
    ('OnePersonLab-Agents', 'OnePersonLab-Agents'),
    ('OnePersonLab', 'OnePersonLab'),
    ('Human User', 'Human User'),
    ('human_user', 'human_user'),
    
    # Dashboard specific
    ('OnePersonLab Dashboard', 'OnePersonLab Dashboard'),
    ('Task Dashboard', 'Task Dashboard'),
    ('Task Directive', 'Task Directive'),
    ('Task Coordinator', 'Task Coordinator'),
    ('Multi-Agent Platform', 'Multi-Agent Platform'),
    ('Research Collaboration Platform', 'Research Collaboration Platform'),  # Keep this
    ('Task Strategist', 'Task Strategist'),
    ('Task Planning', 'Task Planning'),
    
    # File paths and references
    ('onepersonlab-agents', 'onepersonlab-agents'),
    ('OPL-', 'OPL-'),
    
    # Comments and descriptions
    ('task directive', 'task directive'),
    ('task goal', 'task goal'),
    ('task', 'task'),
    ('platform', 'platform'),
]

def process_file(filepath):
    """Process a single file and apply all replacements."""
    try:
        content = filepath.read_text(encoding='utf-8')
        original = content
        
        for old, new in REPLACEMENTS:
            content = content.replace(old, new)
        
        if content != original:
            filepath.write_text(content, encoding='utf-8')
            print(f"  ✓ {filepath.relative_to(ROOT)}")
            return True
        else:
            print(f"  - {filepath.relative_to(ROOT)} (no changes)")
            return False
    except Exception as e:
        print(f"  ✗ {filepath.relative_to(ROOT)}: {e}")
        return False

def main():
    print("🔄 OnePersonLab Terminology Update")
    print("=" * 50)
    
    files_processed = 0
    files_changed = 0
    
    for pattern in PATTERNS:
        for filepath in ROOT.glob(pattern):
            # Skip excluded paths
            if any(filepath.match(exc) for exc in EXCLUDE):
                continue
            
            # Skip if not a file
            if not filepath.is_file():
                continue
            
            files_processed += 1
            if process_file(filepath):
                files_changed += 1
    
    print("=" * 50)
    print(f"✅ Complete: {files_changed}/{files_processed} files updated")

if __name__ == '__main__':
    main()
