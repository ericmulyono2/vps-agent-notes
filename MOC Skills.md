# 🛠️ MOC Skills — Skills Catalog

> **Katalog lengkap skill yang tersedia untuk semua AI Agent**
> Last updated: 2026-06-23

---

## Skill Sources

| Source | Path | Agent |
|--------|------|-------|
| CodeWhale Skills | `/root/.codewhale/skills/` | CodeWhale, DeepSeek |
| OpenClaw Skills | `/root/.openclaw/skills/` | OpenClaw, Gabriel |
| Aider Skills | `/root/.aider/skills/` | Aider |
| Agent Skills | `/root/.agents/skills/` | All agents |
| Coder Agent Skills | `/home/qwen-venice/coder-agent/skills/` | Qwen Coder, Aider |

---

## 🔧 Debugging & Error Handling (4)

| Skill | Deskripsi |
|-------|-----------|
| [[systematic-debugging]] | 4-fase debugging: root cause → pattern → hypothesis → fix. Iron law: NO fix without root cause. Max 3 auto-refactor. |
| [[correctness-and-error-handling]] | Auto-find + auto-fix bugs, try/catch, error boundaries, loading/error/empty states. |
| [[self-repair]] | Missing state triggers repair, not failure. Self-healing pattern. |
| [[autonomous-fixes]] | Fix findings from autonomous-tests. Args: all, critical, high, vulnerability. |

---

## 🎨 Frontend & UI/UX (7)

| Skill | Deskripsi |
|-------|-----------|
| [[frontend-design]] | Production-grade UI dengan typography unik, bold aesthetic, anti-AI-slop. |
| [[web-artifacts-builder]] | React 18 + TypeScript + Vite + Tailwind + shadcn/ui. Bundle ke single HTML. |
| [[theme-factory]] | 10 pre-set theme + custom theme generator. |
| [[web-design-guidelines]] | Review UI compliance: accessibility, UX, best practices. |
| [[react-best-practices]] | React/Next.js performance optimization. |
| [[react-view-transitions]] | View Transition API untuk animasi halaman. |
| [[canvas-design]] | Visual art .png/.pdf dengan design philosophy. |

---

## 🚀 Deployment — Vercel (3)

| Skill | Deskripsi |
|-------|-----------|
| [[deploy-to-vercel]] | Deploy aplikasi/website ke Vercel. Preview deployment. |
| [[vercel-cli-with-tokens]] | Vercel CLI dengan token-based auth. Env variables. |
| [[vercel-optimize]] | Cost/perf optimization untuk project Vercel. |

---

## 🧠 Workflow & Planning (6)

| Skill | Deskripsi |
|-------|-----------|
| [[brainstorming]] | MUST use before creative work — explores intent, requirements, design. |
| [[content-strategy]] | Plan content strategy, topic clusters, editorial calendar. |
| [[copywriting]] | Write/rewrite marketing copy — homepage, landing pages, pricing. |
| [[doc-coauthoring]] | Structured workflow untuk co-authoring documentation. |
| [[internal-comms]] | Internal communications: status reports, leadership updates, newsletters. |
| [[using-superpowers]] | Bootstrap skill — teaches agent how to find and invoke skills. |

---

## 🔗 Bridge & Integration (3)

| Skill | Deskripsi |
|-------|-----------|
| [[openclaw-self-healing]] | 4-tier autonomous self-healing: detect → repair → AI doctor → alert. |
| [[dispatching-parallel-agents]] | Use when facing 2+ independent tasks. |
| [[self-improving-agent]] | Multi-memory architecture. Auto-triggers on skill completion/error. |

---

## 🌐 Web & Browser (2)

| Skill | Deskripsi |
|-------|-----------|
| [[browser-use]] | Automates browser interactions — web testing, form filling, screenshots. |
| [[webapp-testing]] | Playwright untuk testing local web applications. |

---

## 📄 Document Processing (4)

| Skill | Deskripsi |
|-------|-----------|
| [[docx]] | Create, read, edit Word documents (.docx). |
| [[pptx]] | Create, read, edit PowerPoint (.pptx). |
| [[pdf]] | PDF operations: read, merge, split, rotate, watermark, forms. |
| [[xlsx]] | Spreadsheet operations: read, edit, formulas, charts, data cleaning. |

---

## 🎨 Creative (4)

| Skill | Deskripsi |
|-------|-----------|
| [[algorithmic-art]] | Generative art with p5.js — flow fields, particle systems. |
| [[brand-guidelines]] | Anthropic brand colors & typography. |
| [[slack-gif-creator]] | Animated GIFs optimized for Slack. |
| [[mcp-builder]] | Create MCP servers for LLM ↔ external service integration. |

---

## 🛠️ Dev Tools (2)

| Skill | Deskripsi |
|-------|-----------|
| [[claude-api]] | Build, debug, optimize Claude API / Anthropic SDK apps. |
| [[graphify]] | Knowledge graph — 11,844 nodes, 17,989 edges. Query, path, explain. |

---

## 🔄 Cave Crew (6)

| Skill | Deskripsi |
|-------|-----------|
| [[cavecrew]] | Cave Crew main skill. |
| [[caveman]] | Caveman base. |
| [[caveman-commit]] | Caveman commit workflow. |
| [[caveman-compress]] | Caveman compression. |
| [[caveman-help]] | Caveman help system. |
| [[caveman-review]] | Caveman code review. |
| [[caveman-stats]] | Caveman statistics. |

---

## 📊 Ringkasan

| Kategori | Jumlah | Status |
|----------|--------|--------|
| Debugging | 4 | ✅ Active |
| Frontend/UI | 7 | ✅ Active |
| Deployment | 3 | ✅ Active |
| Workflow | 6 | ✅ Active |
| Bridge/Integration | 3 | ✅ Active |
| Web/Browser | 2 | ✅ Active |
| Document | 4 | ✅ Active |
| Creative | 4 | ✅ Active |
| Dev Tools | 2 | ✅ Active |
| Cave Crew | 7 | ✅ Active |
| **TOTAL** | **42** | |

---

## 📥 Installation Logs

- CodeWhale: 50+ skills di `/root/.codewhale/skills/`
- Aider/Qwen: 20 skills diinstal dari CodeWhale → [[skills-installation-log]]
- Catalog detail: [[skill-catalog-qwen-aider]]

---

## 🔗 Cross-Reference

- [[graphify]] — Agent MOC (hub utama)
- [[MOC Memory]] — Sistem memory
- [[MOC Self-Learning]] — Self-improving systems
- [[aider-bridge]] — Aider bridge config
- [[openclaw-bridge]] — OpenClaw bridge config

---

*Skills adalah senjata agent. Gunakan `load_skill` untuk memanggil skill yang relevan.*
