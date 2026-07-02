# 🧠 Kepala VPS — Dashboard

> **AI Administrator VPS srv1672787**  
> Dashboard: [OpenClaw](http://31.97.220.82:18789) | n8n: [Editor](http://31.97.220.82:5678)

---

## 📊 Status Cepat — 02 Jul 2026

```
FAILED SERVICES:  0
ALL SERVICES:     6/6 active (sigma-trading, agent-reach, cognee, telegram, redis, fail2ban)
DOCKER:           10 containers healthy
DISK:             73G/193G (38%)
MEMORY:           5.6G/15G
```

**Services:**
- 🟢 n8n Workflow — `http://31.97.220.82:5678`
- 🟢 OpenClaw Gateway — `http://31.97.220.82:18789`  
- 🟢 Qwen Venice API — `http://31.97.220.82:5050`
- 🟢 Penpot Design — `http://31.97.220.82:9001`

---

## 📈 Trading — Sigma Scalping

| Metric | Value |
|--------|-------|
| Positions | 7 SHORT (LIVE) |
| Total PnL | -1.55 USDT |
| Equity | ~$240 |
| Fear & Greed | 19 (Extreme Fear) |
| Regime | BEARISH — SHORT only |
| Danger Zone | BNB (-8.5%), AVAX (-6.7%) |

**Pipeline**: All 9 n8n modules active, DRY_RUN=false, SL/TP enforced  
**Model chain**: DeepSeek v4-pro → Venice Qwen 3.7 Plus (fallback, validated)  
**Cron jobs**: pipeline-hourly + SIGMA Trading Report → timeout 900s + Venice fallback

---

## 🔗 Quick Links

| Link | Purpose |
|------|---------|
| [OpenClaw Gateway](http://31.97.220.82:18789) | AI Agent Gateway |
| [n8n Editor](http://31.97.220.82:5678) | Workflow Automation |
| [Qwen Venice](http://31.97.220.82:5050/health) | AI Bridge API |

---

## 🤖 AI Agents

| Agent | Model | Role |
|-------|-------|------|
| **CodeWhale** | DeepSeek V4-Pro | Orchestrator — infra, config, auto-heal |
| **Gabriel (OpenClaw)** | DeepSeek V4-Pro + Venice | SPV Decision Maker + Gateway |
| **Qwen Coder** | Qwen 3 Coder 480B | Code gen, UI/UX, full-stack (via Venice) |
| **Sigma Pipeline** | DeepSeek V4-Flash × 6 | Research, Quant, Risk, Execution |

**Fallback chain**: DeepSeek → Venice/Qwen (DIFFERENT provider, validated Jul 1)

---

## 🛠️ Terminal Commands

```bash
# System check
systemctl status sigma-trading agent-reach-news cognee-memory oc-telegram-bot
docker ps --format '{{.Names}} {{.Status}}'

# OpenClaw management
docker logs markasbesar-openclaw-1 --tail 50
docker restart markasbesar-openclaw-1

# n8n management
n8n-helper.sh workflows
n8n-helper.sh "executions?workflowId=qUjwDi48068STPTK&limit=3"

# Live position check
node -e "..." # BingX API query from supervisor-feedback.js credentials

# Venice bridge test
curl -s http://localhost:5050/health
curl -s http://localhost:5050/v1/models
```

---

## 📋 Recent Fixes

| Date | Fix |
|------|-----|
| Jul 2 | Telegram 400 — chat ID `674622107`→`6121123117` for ClipperHIN_bot |
| Jul 2 | Cron timeout — pipeline-hourly + SIGMA TR 900s + Venice fallback |
| Jul 2 | Binance timeout — fetch-market-data.js 15s→30s |
| Jul 1 | Venice fallback — `/v1/models` endpoint, validated |
| Jul 1 | Full VPS repair — 17 fixes (critical + warning) |

---

## 🤖 Telegram Bots

| Bot | Chat `6121123117` | Chat `674622107` | Usage |
|-----|:---:|:---:|---|
| `@ClipperHIN_bot` | ✅ | ❌ | n8n + orchestrator |
| `@AhinTeam_bot` | ✅ | ✅ | OpenClaw cron delivery |
| `@AhinTim_bot` | ✅ | ❌ | (deprecated) |

---

*Last updated: 2026-07-02 06:40 UTC | CodeWhale DeepSeek V4-Pro*
