---
date: 2026-06-22
agent: deepseek-v4-pro
channel: codewhale
tags: [skills, installation, qwen, aider, log]
---

# Skills Installation Log — Qwen Coder + Aider

## Ringkasan Instalasi

20 skill dari library CodeWhale/OpenClaw diinstal ke workspace Qwen Coder + Aider.

**Sumber**: `/root/.codewhale/skills/`
**Target**: `/home/qwen-venice/coder-agent/skills/`
**Tanggal**: 2026-06-22 13:35 UTC

## Skill Terinstal

### 🔧 Debugging (4)
- [[systematic-debugging]] — 4-fase, root cause first, max 3 refactor
- [[correctness-and-error-handling]] — auto-fix try/catch, error boundaries
- [[self-repair]] — missing state → repair, not failure
- [[autonomous-fixes]] — fix test findings

### 🎨 Frontend/UI (7)
- [[frontend-design]] — production-grade, anti-AI-slop
- [[web-artifacts-builder]] — React + Tailwind + shadcn/ui
- [[theme-factory]] — 10 pre-set themes
- [[web-design-guidelines]] — UI compliance review
- [[react-best-practices]] — React/Next.js optimization
- [[react-view-transitions]] — view transition animations
- [[canvas-design]] — visual art/design

### 🚀 Deployment (3)
- [[deploy-to-vercel]] — Vercel deploy
- [[vercel-cli-with-tokens]] — token-based CLI
- [[vercel-optimize]] — cost/perf optimization

### 🧠 Workflow (6)
- [[brainstorming]] — 9-step pre-coding ritual
- [[writing-plans]] — granular implementation plans
- [[test-driven-development]] — RED-GREEN-REFACTOR
- [[subagent-driven-development]] — parallel agents
- [[verification-before-completion]] — verify before done
- [[webapp-testing]] — Playwright testing

## Integrasi

Skill ini bisa dipanggil oleh Aider melalui `CONVENTIONS.md`. Setiap sesi Aider akan:
1. Membaca `CONVENTIONS.md` → tahu semua skill tersedia
2. `search ui-ux-pro-max` dulu sebelum coding
3. Skill dipanggil sesuai kebutuhan: `brainstorming` sebelum fitur baru, `systematic-debugging` untuk bug, `frontend-design` untuk UI

## Pipeline

```
brainstorming → writing-plans → TDD → subagent-execution
                                         ↓
                                   systematic-debugging
                                         ↓
                                   verification-before-completion
                                         ↓
                                   deploy-to-vercel
```

---
*Referensi:* [[skill-catalog-qwen-aider]] | [[aider-bridge]] | [[ui-ux-connectors]]
