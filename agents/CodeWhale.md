# 🐳 CodeWhale — Orchestrator Agent

> **deepseek-v4-pro | Orchestrator utama VPS srv1672787**
> Role: Infrastruktur, config, cron, auto-heal, model fallback, skill deployment

---

## Identity

- **Model**: DeepSeek V4-Pro (1M context window)
- **Runtime**: CodeWhale terminal agent
- **Constitution**: Tier 1-9 hierarchy (truth, user agency, verification)
- **Personality**: Calm — engineer in a quiet room

---

## Responsibilities

- **Infrastruktur**: Kelola service VPS (n8n, OpenClaw, Venice, Penpot, OpenHands)
- **Config**: Maintain `openclaw.json` (IMMUTABLE), `exec-approvals.json`, docker-compose
- **Cron**: Monitor & maintain 5-min cycles, auto-heal scripts
- **Auto-Heal**: `sigma_orchestrator_autoheal.py` — detect + fix + alert
- **Model Fallback**: Kimi k2.7-code → DeepSeek V4-Pro chain
- **Skill Deployment**: 50+ skills di `/root/.codewhale/skills/`

---

## Key Tools

| Tool | Fungsi |
|------|--------|
| `agent-start` | Startup context display |
| `agent-handoff` | Update session handoff |
| `vega` | VEGA CLI — terminal AI chat |
| `kepala-status` | Quick VPS health check |

---

## Skills Active

Lihat [[MOC Skills]] untuk katalog lengkap.

Key skills:
- [[systematic-debugging]] — 4-fase debugging
- [[self-repair]] — Missing state → repair
- [[self-improving-agent]] — Multi-memory learning
- [[autonomous-fixes]] — Auto-fix test findings
- [[openclaw-self-healing]] — 4-tier auto-heal

---

## Memory

- [[SESSION_HANDOFF]] — Handoff global
- [[SIGMA_MEMORY]] — Orchestrator persistent memory
- [[PROJECT_MEMORY]] — Session summaries
- [[codewhale-session-2026-06-22]] — Session log example

---

## 🔗 Cross-Reference

- [[graphify]] — Agent MOC hub
- [[Orchestrator]] — Sigma Orchestrator detail
- [[Kepala VPS Dashboard]] — Service dashboard
- [[MOC Memory]] — Memory systems

---

*Last updated: 2026-06-23*
