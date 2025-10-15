# clean code

Answer: • raw
    ◦ -Write clear, self-documenting names to reduce the need for comments which decay faster
-Augment code with doc comments that can support auto-generated documentation tooling.
-Write pure functions to understand method signatures, avoid side effects, and support unit testing
-Add unit and e2e/integration tests to automatically validate expected behavior
-Run tests (unit/e2e/integration) on PRs and in CI/CD build flows to automatically catch failures
-Apply standard auto linting/formatting to code
-Implement and fill in explanatory git commits (standard branch name) and PR templates for code base history
-Keep things DRY and KISS them to avoid over-engineering and duplication
-Use a typed language to enforce contracts and reduce runtime bugs
-Apply SOLID principles for separation of concern and support scalable architecure
• Use clear, self-documenting names for variables, functions, and components to reduce the need for excessive comments.
• Write doc comments where necessary, especially for public APIs or complex logic — ideally compatible with auto-generated documentation tools.
• Favor pure functions where possible to improve predictability, ease of testing, and composability.
• Write unit, integration, and end-to-end tests to validate behavior across layers of your system.
• Automate test execution in CI/CD pipelines to catch regressions early and keep code trustworthy.
• Follow DRY (Don’t Repeat Yourself) and KISS (Keep It Simple, Stupid) principles to avoid duplication and over-engineering.
• Use a typed language (e.g., TypeScript) to enforce contracts and reduce runtime bugs through static analysis.
• Apply SOLID principles to guide your architecture, improve separation of concerns, and support scalable design.
• final
    ◦ Self-documenting names, doc comments that support auto-generated documentation, unit/e2e/integration tests, run tests on PR and in CICD, DRY/KISS code logic, SOLID principles,  typed language
Company: Untitled (https://www.notion.so/2316509554a781e687dfeefb9c18e2df?pvs=21)
Question 1: What are some best practices for writing clean and maintainable code?