# 🚀 Kimi Code (k2.7-code)

> **Moonshot Kimi k2.7-code | 262K context | Vision-capable**
> Role: Primary SPV Decision Maker + fallback reasoning engine

---

## Identity

- **Model**: `moonshot/kimi-k2.7-code`
- **Context**: 262K token window
- **Vision**: ✅ Image analysis supported
- **Provider**: Moonshot API

---

## Agents yang Menggunakan

| Agent | Channel | Prioritas |
|-------|---------|-----------|
| **Gabriel (SPV)** | OpenClaw Gateway | Primary |
| Sigma Pipeline Fallback | n8n workflow | FB1-FB4 |
| Orchestrator Fallback | Python | Secondary |

---

## API Keys

4 Moonshot keys untuk redundancy:
- FB1: Pre-screen + Senior Trader fallback
- FB2: Research + Gabriel fallback
- FB3: Quant + Risk fallback
- FB4: Gabriel Primary

---

## 🔗 Cross-Reference

- [[openclaw-bridge]] — OpenClaw gateway (Gabriel primary model)
- [[Orchestrator]] — Sigma pipeline orchestrator (fallback)
- [[graphify]] — Agent MOC hub
- [[graphify-coder-agent-report]] — Knowledge graph report
- [[Kepala VPS Dashboard]] — VPS dashboard
- [[Untitled Base]] — Base note

---

*Created: 2026-06-25*