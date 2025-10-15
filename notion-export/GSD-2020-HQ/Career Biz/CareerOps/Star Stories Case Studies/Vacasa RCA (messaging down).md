# Vacasa: RCA (messaging down)

Theme: Strategic Technical Management
Prompt: We’re interested in how you communicate the value of addressing technical debt, prioritize technical strategy, and reflect on lessons learned from past decisions.

### Prompt

- Theme: {}
- Question: {}

### Context

- Company
- Timeline
- Project/Initiative
- Role

### S -Situation

- **S – Situation**
    - At Vacasa, we noticed that guest chat messages weren’t being received, despite no system errors or alerts being triggered.

### T - Task

- **T – Task**
    - Diagnose the root cause and prevent similar silent failures going forward—while maintaining guest and agent trust.

### A - Action

- **A – Action**
    - Identified the issue by “sense” and anecdotal reports, not by logs—escalated quickly to our third-party messaging partner.
    - Learned that we were inadvertently routed to a beta instance with flawed test infrastructure.
    - Led the push to confirm SLAs, get off the beta pipeline, and institute thresholds for alerting on message volume anomalies.
    - Included junior engineers in the RCA process to teach diagnostic skills and broaden system familiarity.

### R - Result

- **R – Result**
    - Messaging delivery stabilized and SLAs were enforced.
    - Team became more proactive in catching issues via monitoring in metrics dashboard and then a threshold alert
    - Built confidence and learning across the team by treating RCA as an inclusive, teachable process.