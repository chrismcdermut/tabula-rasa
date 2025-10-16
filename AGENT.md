# Agent Instructions - Tabula Rasa Workspace

## Overview
This is Chris McDermut's integrated life and work management system. Everything is tracked as markdown files for complete agent visibility and manipulation.

## Directory Structure
```
tabula-rasa/
├── kanban/           # Visual task boards
│   ├── life-kanban.md      # Personal life tasks (health, friends, growth)
│   └── careerops-kanban.md # CareerOps product development
├── tasks/            # Detailed task specifications
├── daily/            # Daily notes and journals
├── specs/            # Project specifications
└── ventures/         # Business projects
    └── inflow/       # Submodule - separate git repo for team access
```

## Working with Tasks

### Task Format
Each task in kanban boards can link to detailed markdown files with:
```markdown
---
status: TODO | IN_PROGRESS | DONE
priority: URGENT | IMPORTANT | NORMAL
category: BUILD/Infra | GROW | LEARN | Health/Fitness | etc
due: 2025-01-25
---

# Task Title

## Context
Why this matters

## Success Criteria
- [ ] Specific outcome 1
- [ ] Specific outcome 2

## Notes
Implementation details, blockers, decisions
```

### Status Management
- **URGENT & IMPORTANT**: Do immediately
- **TRIAGE**: Needs evaluation/decision
- **BACKLOG**: Future work
- **IN PROGRESS**: Currently active (limit to 3)
- **DONE**: Completed

## Key Files

- `kanban/life-kanban.md` - Personal life management board
- `kanban/careerops-kanban.md` - CareerOps product roadmap
- `AGENT.md` - This file, your operating instructions
- `ventures/inflow/` - Business code and documentation (git submodule)

## Agent Capabilities

You can:
1. **Move tasks between columns** - Edit the kanban markdown files
2. **Update task details** - Modify linked task files or inline content
3. **Create new tasks** - Add to appropriate kanban column with [[task-name]] link
4. **Query status** - Search across all files for current state
5. **Generate reports** - Compile progress from multiple sources

## Context Awareness

When Chris asks about:
- **"What should I do?"** - Check URGENT & IMPORTANT in life-kanban.md
- **"CareerOps status?"** - Review careerops-kanban.md IN PROGRESS column
- **"Health tasks?"** - Filter life-kanban.md by Category: Health/Fitness
- **"What's blocking?"** - Search for tasks in TRIAGE or with blocker notes

## Principles

1. **Everything is text** - All state is readable/editable markdown
2. **Links over duplication** - Use [[wiki-links]] to connect related content
3. **Atomic tasks** - Each task should be completable in one session
4. **Context in frontmatter** - Structured data goes in YAML frontmatter
5. **Git commits track decisions** - Every change is versioned

## Common Operations

### Add a new task
```markdown
## Column Name
- [ ] [[new-task-name]]
  **Priority:** URGENT
  **Category:** BUILD/Infra
  ***
  Brief description here
```

### Move task to different column
Cut the entire task block and paste under new column header

### Mark task complete
Change `- [ ]` to `- [x]` and move to Done column

### Update task status in linked file
Edit the frontmatter `status:` field in the linked .md file

## Integration Points

- **Obsidian** - Open tabula-rasa/ as vault for visual kanban
- **Git** - Commit changes for history tracking
- **Inflow submodule** - Separate repo for team collaboration

Remember: You have full read/write access. Make changes confidently. Chris wants you to manipulate this system as if it were your own memory.