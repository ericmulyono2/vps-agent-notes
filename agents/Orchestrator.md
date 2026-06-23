# 🎯 Sigma Orchestrator

> **DeepSeek V4-Pro | Orchestrator pipeline trading Sigma Scalping**
> Role: Kelola infrastruktur, config, cron, auto-heal, model fallback

---

## Identity

- **Model**: DeepSeek V4-Pro (1M context), Kimi k2.7-code (fallback)
- **Script**: `/root/sigma-scalping-team/sigma_orchestrator.py`
- **Auto-Heal**: `/root/sigma-scalping-team/sigma_orchestrator_autoheal.py`
- **Memory**: [[SIGMA_MEMORY]]

---

## Batasan Keras

Orchestrator **TIDAK**:
- Mengubah strategi trading
- Eksekusi order
- Override decision Gabriel (SPV)

Orchestrator **HANYA**:
- Mengelola infrastruktur
- Maintain config & cron
- Auto-heal service
- Model fallback
- Deploy skill & tools
- Monitor server health

---

## Responsibilities

### Infrastruktur
- n8n container health → restart kalau crash
- OpenClaw container health → restart kalau down
- Cron job verification → 5-min cycles
- Workflow health monitoring

### Config
- `openclaw.json` — IMMUTABLE (`chattr +i`)
- `exec-approvals.json` — 15 exec patterns
- `docker-compose.yml` — env vars
- Rule #6 enforcement di orchestrator level

### Auto-Heal
```
Monitor → Detect Anomaly → Diagnose → Auto-Fix → Verify → Alert (Telegram)
```

Targets:
- n8n crash → restart container
- OpenClaw down → restart container
- Cron failure → re-enable + verify
- Axios patch missing → re-apply di container
- Workflow error patterns → diagnose + fix

---

## Model Chain

| Priority | Model | Context |
|----------|-------|---------|
| **1 (Gabriel)** | `moonshot/kimi-k2.7-code` | Vision, 262K ctx |
| **2 (Fallback)** | `deepseek/deepseek-v4-pro` | 1M ctx |
| **Orch** | `deepseek/deepseek-v4-pro` | 1M ctx |

---

## Rule #6 — Min Margin $10

Hard check di orchestrator:
```python
MIN_MARGIN_PER_POSITION = 10.0  # USD
```

Enforced di 5 layer: Entry Filter → Pre-Entry Gate → Junior Trader → Position Manager → Orchestrator

---

## State File

`/root/sigma-scalping-team/sigma_orchestrator_state.json`
- Synced ke live BingX data
- Tracking: positions, equity, margin, regime

---

## Known Issues

- ETH-SHORT position ($3.14 margin) — pre-Rule #6, close natural via SL/TP
- axios patch di n8n container — volatile, re-apply setelah container recreate

---

## 🔗 Cross-Reference

- [[graphify]] — Agent MOC hub
- [[Sigma Scalping Team]] — Team overview
- [[CodeWhale]] — Orchestrator utama VPS
- [[SIGMA_MEMORY]] — Persistent memory
- [[Kepala VPS Dashboard]] — Live status

---

*Last updated: 2026-06-23*
