# 🧠 Kepala VPS — Dashboard

> **AI Administrator VPS srv1672787**  
> Bot: [@openhandAhin_bot](https://t.me/openhandAhin_bot) | Dashboard: [OpenHands](http://31.97.220.82)

---

## 📊 Status Cepat

```query
path:sigma-scalping-team
tag:#trading
```

**Services:**
- 🟢 n8n Workflow — `http://31.97.220.82:5678`
- 🟢 OpenClaw Gateway — `http://31.97.220.82:18789`  
- 🟢 Qwen Venice API — `http://31.97.220.82:5050`
- 🟢 Penpot Design — `http://31.97.220.82:9001`
- 🟢 OpenHands Canvas — `http://31.97.220.82`

---

## 🔗 Quick Links

| Link | Purpose |
|------|---------|
| [OpenHands Dashboard](http://31.97.220.82) | AI Agent Control Center |
| [n8n Editor](http://31.97.220.82:5678) | Workflow Automation |
| [Telegram Bot](https://t.me/openhandAhin_bot) | Remote VPS Control |

---

## 🤖 Telegram Commands

| Command | Fungsi |
|---------|--------|
| `/start` | Perkenalan Kepala VPS |
| `/status` | Cek status server real-time |
| `/trading` | Status trading Sigma Scalping |
| `/logs [service]` | Lihat log n8n/openclaw/system |
| `/help` | Bantuan lengkap |

**Chat santai:**  
Ketik aja bebas — "Cek container", "Kenapa n8n error?", "Restart OpenClaw", "Gimana kabar VPS?"

---

## 🛠️ Terminal Commands (di VPS)

```bash
# VEGA CLI — Chat AI langsung di terminal (mirip CodeWhale)
vega                        # Mode interaktif
vega "cek status docker"    # Single command
vega --status               # Quick health check
vega --system               # Lihat system prompt

# Cek semua service
kepala-status

# Restart Kepala VPS
systemctl restart kepala-vps

# Restart OpenHands
systemctl restart openhands-canvas

# Lihat log
journalctl -u kepala-vps -f
journalctl -u openhands-canvas -f
```

## 🖥️ Akses dari Windows

**Dashboard Web:**
- Buka `http://31.97.220.82` di browser
- Kalau ga bisa → SSH tunnel:
  ```powershell
  ssh -L 3000:localhost:80 root@31.97.220.82
  ```
  Lalu buka `http://localhost:80`

**VEGA CLI dari Windows:**
- SSH ke VPS dulu, lalu ketik `vega`

---

---

## 🤖 Connected Agents

| Agent | Note | Role |
|-------|------|------|
| [[CodeWhale]] | Orchestrator utama | Infra, config, auto-heal |
| [[aider-bridge|Aider + Qwen Coder]] | XERO | Code gen, UI/UX, full-stack |
| [[openclaw-bridge|OpenClaw + DeepSeek]] | Gabriel | SPV Decision Maker + Gateway |
| [[deepseekv4pro|DeepSeek V4-Pro]] | LLM Engine | Primary reasoning 1M ctx |
| [[kimicode|Kimi Code k2.7]] | LLM Engine | Vision, SPV primary, fallback |

---

## 🔗 Cross-Reference

- [[graphify]] — Agent MOC hub
- [[graphify-coder-agent-report]] — Knowledge graph report
- [[Untitled Base]] — Base note

---

*Last updated: 2026-06-23 | Powered by Qwen 3 Coder 480B Turbo*
