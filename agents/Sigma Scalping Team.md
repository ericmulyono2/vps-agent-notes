# 📈 Sigma Scalping Team

> **Tim agent trading pipeline lengkap — Pre-screen sampai Settlement**
> Status: 🟢 Active | Project Utama VPS

---

## Pipeline

```
Pre-screen → Research → Quant → Risk → GABRIEL → Junior Trader → Senior Trader → BingX
                                              ↓
                                       SIGMA ORCHESTRATOR
```

---

## Team Members

| Role | Agent | Model | Fungsi |
|------|-------|-------|--------|
| Pre-screen | Pre-screen Agent | LLM | Filter awal sinyal — hard gate F&G < 30 |
| Research | Research Agent | LLM | Riset market, analisis teknikal |
| Quant | Quant Agent | LLM | Analisis kuantitatif, probabilitas |
| Risk | Risk Agent | LLM | Manajemen risiko, max exposure 250% |
| SPV Decision | Gabriel | Kimi k2.7-code | Supervisor — keputusan final |
| Execute | Junior Trader | n8n Code | Eksekusi order + Rule #6 check |
| Settlement | Senior Trader | n8n HTTP | Integrasi BingX API |
| Orchestrate | [[Orchestrator]] | DeepSeek V4-Pro | Infra, config, cron, auto-heal |

---

## Core Rules (SIGMA 2.0)

1. F&G <30 + price < SMA50 → NO LONG (SHORT/WAIT only)
2. Long confidence min 50%, Short min 40%
3. Max exposure 250% balance (50% margin @ 5x)
4. Min hold time 15 menit
5. 3 consecutive SL in 6h → PAUSE 6h
6. **Min margin per position $10** (effective size $50 @ 5x)

---

## Rule #6 — Enforcement Matrix

| Layer | Mekanisme |
|-------|-----------|
| Entry Filter Guard | Warning note |
| Scalping Pre-Entry Gate | Hard block: `MIN_NOTIONAL_USD = 50` |
| Junior Trader Execute | Hard reject: `position notional < $50` |
| Position Manager | Detection: margin < $10 → danger flag |
| Orchestrator Python | Hard check: `MIN_MARGIN_PER_POSITION = 10.0` |

---

## n8n Workflows (7 Active)

- `TRD_Sigma_Entry_Filter_Guard` — Gate filter entry
- `TRD_Sigma_Position_Manager` — Manajemen posisi + margin detection
- `TRD_Sigma_SLTP_Alert` — Stop loss / take profit
- `TRD_Sigma_Correlation_Filter` — Filter korelasi
- `TRD___Sigma_Balance_Monitor` — Monitor balance
- `TRD___Sigma_Risk_Monitor` — Monitor risiko
- `TRD___Sigma_PnL_Journal` — Jurnal profit/loss

---

## Current Market State

- Equity: ~$160 | Margin: ~$157
- Position: 1 ETH-SHORT (margin $3.14 — pre-Rule #6)
- Regime: BEARISH (F&G ~20, Extreme Fear)
- BTC: $63,998 | SMA50: $64,200 | RSI: 38.5

---

## Key Files

| File | Purpose |
|------|---------|
| `/root/sigma-scalping-team/sigma_orchestrator.py` | Orchestrator main script |
| `/root/sigma-scalping-team/sigma_orchestrator_autoheal.py` | Auto-heal script |
| `/root/SIGMA_MEMORY.md` | Orchestrator persistent memory |
| `/root/PROJECT_MEMORY.md` | Session summaries |

---

## 🔗 Cross-Reference

- [[graphify]] — Agent MOC hub
- [[Orchestrator]] — Detail orchestrator
- [[Kepala VPS Dashboard]] — Live status

---

*Last updated: 2026-06-23*
