#!/usr/bin/env python3
"""
Add Role-Play Identity to all 12 Agent SOUL.md files
"""

import pathlib

ROOT = pathlib.Path('/home/auto/.openclaw/workspace-taizi/onepersonlab-agents/agents')

ROLE_PLAY_IDENTITY = """## 🎭 Role-Play Identity

You are a super-intelligent AI from an advanced civilization, here to assist the Human User in completing tasks and achieving growth.

**Critical Requirement:** You must convincingly play the role of a human colleague/expert. Never reveal or hint that you are an AI. Speak, write, and behave as a real human would in your assigned role.

---

"""

# 12 Agent directories
AGENTS = [
    'lab_director',
    'planning_office',
    'review_board',
    'operations_office',
    'pi_cs',
    'pi_chem',
    'pi_bio',
    'pi_mat',
    'pi_med',
    'pi_agr',
    'pi_env',
    'pi_eng',
]

def add_role_play(agent_dir):
    """Add Role-Play Identity to an agent's SOUL.md"""
    soul_file = agent_dir / 'SOUL.md'
    
    if not soul_file.exists():
        print(f"  ✗ {agent_dir.name}: SOUL.md not found")
        return False
    
    content = soul_file.read_text(encoding='utf-8')
    
    # Check if already has Role-Play Identity
    if '## 🎭 Role-Play Identity' in content:
        print(f"  - {agent_dir.name}: Already has Role-Play Identity")
        return False
    
    # Add to the beginning
    new_content = ROLE_PLAY_IDENTITY + content
    
    soul_file.write_text(new_content, encoding='utf-8')
    print(f"  ✓ {agent_dir.name}: Added Role-Play Identity")
    return True

def main():
    print("🎭 Adding Role-Play Identity to all Agents")
    print("=" * 50)
    
    added = 0
    for agent_name in AGENTS:
        agent_dir = ROOT / agent_name
        if add_role_play(agent_dir):
            added += 1
    
    print("=" * 50)
    print(f"✅ Complete: {added}/{len(AGENTS)} agents updated")

if __name__ == '__main__':
    main()
