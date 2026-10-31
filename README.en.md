# AKORIS

> **Adaptive Knowledge & Orchestrated Review for Iterative Systems**
>
> AI produces; control verifies; human authority decides.

[🇫🇷 Français](README.md) · [🇬🇧 English](README.en.md)

[![Version](https://img.shields.io/badge/version-0.1.3-blue)]()
[![Tests](https://img.shields.io/badge/tests-24%20passing-brightgreen)]()
[![License](https://img.shields.io/badge/license-MIT%20%2B%20Apache--2.0%20%2B%20CC--BY--4.0-lightgrey)]()

---

## Table of Contents

- [What is AKORIS?](#what-is-akoris)
- [The Three Zeros](#the-three-zeros)
- [Quick Start](#quick-start)
- [Architecture](#architecture)
- [Compatible Tools](#compatible-tools)
- [Repository Structure](#repository-structure)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

---

## What is AKORIS?

AKORIS is a **governance method** for AI-assisted software development. It
establishes a structured framework to organize, guide, control, and evaluate
the contribution of AIs throughout the software development process.

Its goal: make AI a **means of production placed under explicit governance**,
rather than a substitute for human reflection, decision, and responsibility.

**What AKORIS is not:**

- ❌ not an AI model
- ❌ not a code editor
- ❌ not a programming framework
- ❌ not a mere prompt collection

It is a governance method, **independent of models, vendors, and tools**.

---

## The Three Zeros

| Zero | Meaning |
|------|---------|
| **Zero hallucination** | Decisions rest on verifiable elements |
| **Zero spaghetti code** | Architecture is coherent, organization is controlled |
| **Zero uncontrolled debt** | Trade-offs are identified, justified, documented, tracked |

These zeros are **compasses**, not **guarantees**. AKORIS **measures the gap**
and **traces** trade-offs. An AKORIS project is not a debt-free project; it is
a project whose debt is **known, traced, and managed**.

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/sieni7/akoris-method.git

# 2. Scaffold a new project
./akoris-method/scripts/init-project.sh my-project

# 3. Follow phase 0
cat akoris-method/checklists/phase-0.md
```

Then:

1. Open **3 tabs** in a compatible tool (A, B, C).
2. Paste the identity prompts (`templates/.akoris/config/agents/`).
3. Launch the bootstrap (`templates/.akoris/config/bootstrap.md`).
4. Type `go` in tab A to start phase 1.

---

## Architecture

### 3 pillars (in the project)

```
my-project/
├── app/       ← executable code (Builder)
├── doc/       ← technical + product documentation (Builder + Orchestrator)
└── .akoris/   ← governance (context, state, roadmap, ADR, debts)
```

### 3 tabs + 1 human

```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│    TAB A     │  │    TAB B     │  │    TAB C     │
│ Orchestrator │  │   Builder    │  │   Auditor    │
│   (plans)    │  │   (codes)    │  │   (audits)   │
└──────┬───────┘  └──────┬───────┘  └──────┬───────┘
       │                 │                 │
       └─────────────────┼─────────────────┘
                         ▼
              ┌─────────────────────┐
              │  VALIDATOR (human)  │
              │ (authorizes, decides)│
              └─────────────────────┘
```

### GO Convention

| Tab | What Validator types | Meaning |
|-----|----------------------|---------|
| A | `go` | Authorizes planning |
| B | `go` | Authorizes execution, then push |
| C | `go` then verdict | Launches audit, then decides |

Verdicts: `go` · `go with reserve: <details>` · `no-go: <reason>`

---

## Compatible Tools

AKORIS is **tool-independent**. It requires three capabilities:

| Requirement | Why |
|-------------|-----|
| **3 simultaneous LLM agents** | Tabs A/B/C (Orchestrator, Builder, Auditor) |
| **A shared folder** | `.akoris/` (single source of truth) |
| **A file lock** | `state.md` (one active agent at a time) |

### Reference tool

**[OpenCode](https://github.com/opencode-ai/opencode)** — multi-tab interface,
shared folder, native lock. The tool that inspired and validated AKORIS.

### Alternatives

| Tool | Compatible? | Note |
|------|-------------|------|
| **Manus** | ⚠️ Partial | Autonomous agent, no native multi-tab |
| **Cursor** | ✅ Yes | Multi-window + file access |
| **Windsurf** | ✅ Yes | Multi-window + file access |
| **Claude Projects** | ✅ Yes | Multi-project + shared files |
| **Single chat** | ❌ No | No role separation |
| **Tool without file access** | ❌ No | No `state.md` |

**Compatibility criterion:** 3 simultaneous LLM sessions + shared file system
access + a lock mechanism (`state.md` file).

---

## Repository Structure

```
akoris-method/
├── README.md              ← French version (default)
├── README.en.md           ← this file (EN)
├── METHOD.md              ← founding principles
├── CHANGELOG.md           ← history
├── LICENSE                ← MIT + Apache-2.0 + CC-BY-4.0
├── CONTACT.md             ← author contact
├── docs/                  ← the book
├── decisions/             ← 49 frozen decisions (001-048, 050) + 1 clarification (049)
├── checklists/            ← phase 0, bootstrap, sprint, verdict, closure
├── scripts/               ← init-project.sh; scripts/validate-method.py — available
├── tests/                 ← 24 Python tests across 4 files
├── templates/doc/         ← project documentation templates to copy
├── templates/skills/      ← Skills Packs (QA-01 pilot available)
├── templates/.akoris/     ← templates to copy
└── .github/workflows/     ← CI (pytest + shellcheck + index)
```

---

## Documentation

The book currently has 12 available chapters (ch.0 to ch.11).

| Document | Content |
|----------|---------|
| [`METHOD.md`](METHOD.md) | Founding principles |
| [`docs/`](docs/) | The book (12 available chapters, ch.0 to ch.11), including [`ch.7 — Debt & ADR`](docs/07-dettes-adr.md) and [`ch.8 — Evolution`](docs/08-evolution.md) |
| [`decisions/`](decisions/) | 49 frozen decisions (001-048, 050) + 1 clarification (049) |
| [`checklists/`](checklists/) | Phase 0 → closure |
| [`templates/.akoris/contexte.md`](templates/.akoris/contexte.md) | The constitution (23 sections, §0 to §22) |
| [`QA-01 Code Reviewer`](templates/skills/QA-01-Code-Reviewer/SKILL.md) | Code-review skill pilot |


AKORIS introduces the concept of Skills Packs: business skills that can be activated by the SPA. The QA-01 pilot is available.

---

## Contributing

Contributions are welcome. Before submitting a PR:

1. Read [`METHOD.md`](METHOD.md) and [`decisions/`](decisions/).
2. Check that the change complies with the 49 frozen decisions (001-048, 050) + 1 clarification (049)
   (or propose an ADR for a new decision).
3. Run `pytest` (24 Python tests across 4 files).
4. Run `shellcheck scripts/*.sh` (0 warnings expected).
5. Open an **issue** before a major PR.

---

## Author

**Oulai Sieni Tarek**

- 🐙 GitHub: [@sieni7](https://github.com/sieni7)
- 📧 Email: sieni7 [at] gmail [dot] com
- 🌍 Côte d'Ivoire

> For full contact details (phone, WhatsApp), see [`CONTACT.md`](CONTACT.md).

---

## License

| File / Folder | License |
|---------------|---------|
| `README.md`, `README.en.md`, `CHANGELOG.md`, `CONTACT.md` | Apache-2.0 |
| `METHOD.md`, `decisions/`, `checklists/`, governance templates, `templates/doc/` | Apache-2.0 |
| `docs/` | CC-BY-4.0 |
| `scripts/*.sh`, `templates/.akoris/scripts/*.py`, `tests/*.py` | MIT |
| `LICENSE` | Apache-2.0 |

Holder: **Oulai Sieni Tarek**.

---

## Acknowledgements

- [OpenCode](https://github.com/opencode-ai/opencode) — reference tool
- [Keep a Changelog](https://keepachangelog.com/) — CHANGELOG format
- [SemVer](https://semver.org/) — versioning
- [Conventional Commits](https://www.conventionalcommits.org/) — commit convention
- [Michael Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) — ADR format

---

> **AKORIS — AI produces; control verifies; human authority decides.**
