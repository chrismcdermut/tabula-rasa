# Cosmos PMO System

A fractal project management system using astronomical metaphors for organizational hierarchy.

## 🌌 Structure Overview

This system uses a physics-inspired hierarchy:

- **🌟 Quark** - Atomic task unit (smallest indivisible work)
- **⚛️ Atom** - Grouped tasks forming a feature/deliverable
- **🧬 Molecule** - Epic or significant work unit
- **🪨 Project** - Collection of molecules (formerly "Planet")
- **☀️ Initiative** - Strategic pillar (formerly "Solar System")
- **🌌 Objective** - North star goal (formerly "Galaxy")

## 📁 Directory Structure

```
/
├── README.md                 # This file
├── life.project.json         # Root index of all objectives
├── schemas/                  # JSON schemas for validation
│   ├── objective.schema.json
│   ├── initiative.schema.json
│   ├── project.schema.json
│   ├── board.schema.json
│   └── task.schema.json
└── projects/                 # All active projects
    ├── tmm/                  # The Momentum Method
    │   ├── project.json
    │   ├── manuscript/
    │   ├── research/
    │   └── boards/
    └── careerops/            # Career Operations
        ├── project.json
        ├── src/
        ├── docs/
        └── boards/
```

## 🚀 Quick Start

1. Clone this repository
2. Review `life.project.json` for the overall structure
3. Navigate to any project folder to see its organization
4. Boards contain the actual tasks in kanban format

## 📋 Board Structure

Each board follows a standard kanban flow:
- **Backlog** - Not started
- **In Progress** - Active work
- **Blocked** - Waiting on dependencies
- **Done** - Completed

## 🤖 Agent-Friendly Design

This structure is optimized for AI agents:
- Plain text and JSON for easy parsing
- Consistent naming conventions
- Cross-references via IDs
- Git-friendly for version control

## 🔗 Hierarchy Mapping

| PMO Term | Our Term | Description |
|----------|----------|-------------|
| Task | Quark | Smallest unit of work |
| Story/Feature | Atom | Deliverable unit |
| Epic | Molecule | Major feature set |
| Project | Project | Product or initiative |
| Program | Initiative | Strategic pillar |
| Portfolio | Objective | Top-level goal |

## 📝 File Conventions

- `project.json` - Project metadata and configuration
- `*.board.json` - Kanban boards with tasks
- `*.md` - Documentation and content
- Lowercase kebab-case for all filenames (except README.md)

## 🎯 Alignment with Methodologies

This system draws from:
- **OKR** - Objectives at the top level
- **SAFe** - Epic/Feature/Story breakdown
- **Agile** - Kanban boards and iterative work
- **GIST** - Goals, Ideas, Steps, Tasks hierarchy