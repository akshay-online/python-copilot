
---
applyTo: '**'
---

# 🧠 GitHub Copilot Agent Evaluation Instructions for Codeathon

## 📝 Objective:
Evaluate the submitted project repository against predefined Codeathon criteria and generate a score out of 100. Use the codebase, documentation, configuration, and tests to derive objective metrics for each category.

---

## ✅ Evaluation Categories

### 1. 📄 Business Requirements Document (BRD) – 10 points
- Look for `docs/BRD.md`, `BRD.pdf`, or similar.
- Extract and validate the presence of:
  - Problem statement
  - Goals & Objectives
  - Scope, Assumptions
  - Personas or Stakeholders

```yaml
Score:
  If all 4 elements present and well-described: 10
  If 3 elements present: 8
  If 2 elements: 5
  If only 1 or unclear: 2
  If missing: 0
```

---

### 2. 📘 Technical Specification Document (TSD) – 10 points
- Look for `docs/TSD.md`, `TSD.pdf`
- Validate:
  - Tech stack mentioned
  - APIs defined
  - Database schema/model design
  - Security/performance considerations

```yaml
Score:
  If all elements present with diagrams: 10
  If 3 elements: 8
  If 2 elements: 5
  If minimal details: 2
  If missing: 0
```

---

### 3. 🧱 Architecture Diagram – 10 points
- Check for `architecture.png`, `.svg`, `README.md` diagram, or Mermaid diagram
- Should represent logical layers, components, and services

```yaml
Score:
  Clear, modular, labeled and readable: 10
  Functional but lacks clarity: 7
  Generic or missing major components: 3
  Missing: 0
```

---

### 4. 💻 Working Solution – 15 points
- Run the app if possible (backend/frontend via `src/`)
- Validate:
  - Feature completeness
  - Execution success
  - Modularity
  - Follows coding standards

```yaml
Score:
  Fully functional, clean modular code: 15
  Mostly functional with minor issues: 10
  Major bugs or missing core features: 5
  Broken or not executable: 0
```

---

### 5. 🧼 Coding Standards – 10 points
- Check `src/` and validate:
  - Naming conventions
  - Proper indentation
  - Commenting practices
  - Logical structure
  - No code duplication

```yaml
Score:
  Excellent readability, modularity, comments: 10
  Minor issues: 7
  Several inconsistencies: 4
  Poor structure, hard to read: 0
```

---

### 6. 🤖 Effective Copilot Prompt Usage – 5 points
- Scan code for comments like `// Generate a function to...`
- Count distinct, targeted prompts
- Evaluate usefulness of generated output

```yaml
Score:
  > 5 useful prompts: 5
  3-5 useful prompts: 3
  1-2 weak prompts: 1
  None: 0
```

---

### 7. 🧪 Test Cases – 10 points
- Check `tests/` or test files in `src/`
- Validate:
  - Unit test presence
  - Integration tests
  - Negative test cases
  - Coverage file (`coverage/`, `lcov.info`)

```yaml
Score:
  Unit + integration + coverage + edge cases: 10
  Only unit tests, limited coverage: 6
  Sparse tests, no automation: 3
  No tests: 0
```

---

### 8. ⚙️ CI/CD Pipeline – 10 points
- Check `.github/workflows/`, `azure-pipelines.yml`
- Must include:
  - Build job
  - Test job
  - Lint job
  - Deploy (optional but +)

```yaml
Score:
  Full CI pipeline, clean execution: 10
  Basic CI setup: 6
  Incomplete CI: 3
  No CI: 0
```

---

### 9. 🚀 Deployment Scripts – 5 points
- Look for `deploy/`, `Dockerfile`, or cloud scripts
- Must support:
  - Script-based or YAML-based deployment

```yaml
Score:
  Automated deployment, ready-to-use: 5
  Basic container scripts: 3
  Manual/deployment notes only: 1
  No deployment method: 0
```

---

### 10. 🔐 Security Integrations – 5 points
- Check for:
  - SAST tool config (e.g., SonarQube, CodeQL)
  - SCA tools like Dependabot
  - Secret scanning config or logs

```yaml
Score:
  All three categories configured: 5
  Two categories: 3
  One category: 1
  None: 0
```

---

### ⭐ Bonus: Innovation & Performance – 10 points
- Look for:
  - Performance tuning (caching, pagination)
  - Logging/Observability
  - Creative features
  - Beautiful UX

```yaml
Score:
  Innovative, clean UX, fast, scalable: 10
  Some polish/extra features: 5
  Basic functionality only: 0
```

---

## 📊 Final Output Format

```json
{
  "project_name": "sample-project",
  "total_score": 86,
  "scores": {
    "BRD": 8,
    "TSD": 10,
    "Architecture": 10,
    "WorkingSolution": 12,
    "CodingStandards": 9,
    "CopilotPrompts": 3,
    "TestCases": 7,
    "CI/CD": 10,
    "Deployment": 3,
    "Security": 4,
    "Bonus": 10
  },
  "remarks": "Well-executed architecture, great use of CI/CD and Copilot prompts. Minor issues in testing and documentation structure."
}
```

---

## 🧩 Copilot Agent Notes
- Use repo context + directory inspection
- If test cases fail to execute, deduct proportionally
- Check README for execution & setup steps
- Score should be human-verifiable and auditable
