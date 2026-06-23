# VPS Agent Notes — Obsidian Vault

> Jembatan antara Macbook Obsidian ↔ VPS Agent (OpenClaw + Aider + Qwen)

## 🕸️ Mulai dari Sini

→ **[[graphify]]** — Hub sentral semua AI Agent. Mulai dari sini untuk navigasi Graph View.

## 📂 Struktur

```
obsidian-vault/
├── graphify.md              ← 🕸️ MOC Agents (HUB UTAMA)
├── MOC Memory.md            ← 🧠 MOC Memory Systems
├── MOC Self-Learning.md     ← 🔁 MOC Self-Learning
├── MOC Skills.md            ← 🛠️ MOC Skills Catalog
├── daily/                   ← Catatan harian, session log
├── memory/                  ← Agent persistent memory
├── research/                ← Hasil riset, analisis trading
├── agents/
│   ├── openclaw/            ← Output OpenClaw (DeepSeek V4-Pro)
│   ├── aider/               ← Output Aider + Qwen Coder
│   ├── CodeWhale.md         ← 🐳 CodeWhale agent note
│   ├── Orchestrator.md      ← 🎯 Sigma Orchestrator note
│   ├── Qwen Venice.md       ← 🌉 Qwen Venice gateway note
│   └── Sigma Scalping Team.md ← 📈 Trading team note
├── logs/                    ← Agent execution logs
├── config/                  ← Konfigurasi dan referensi
└── sync-obsidian.sh         ← Script auto-sync Git
```

## 🗺️ Maps of Content

| MOC | Isi |
|-----|-----|
| [[graphify]] | 🕸️ **Agent Hub** — semua agent, model chain, pipeline |
| [[MOC Memory]] | 🧠 Memory systems — AI_AGENT_CONTEXT, vault, DeepLake RAG |
| [[MOC Self-Learning]] | 🔁 Self-improving, self-repair, auto-heal, debugging |
| [[MOC Skills]] | 🛠️ 42 skills catalog — debugging, frontend, deploy, docs |

## 🤖 Agents

| Agent | Model | Output Path | Note |
|-------|-------|-------------|------|
| OpenClaw (Gabriel) | DeepSeek V4-Pro / Kimi k2.7-code | `agents/openclaw/` | [[openclaw-bridge]] |
| Aider (XERO) | Qwen Coder 480B | `agents/aider/` | [[aider-bridge]] |
| CodeWhale | DeepSeek V4-Pro | `memory/`, `research/` | [[CodeWhale]] |
| Sigma Orchestrator | DeepSeek V4-Pro | `/root/AI_AGENT_CONTEXT/` | [[Orchestrator]] |
| Qwen Venice | Qwen Coder 480B | Gateway (port 5050) | [[Qwen Venice]] |

## 🔄 Sync

```bash
# Di VPS — push perubahan ke GitHub
./sync-obsidian.sh

# Di Macbook — pull perubahan dari GitHub
cd "/Users/ericmulyono/Library/Mobile Documents/iCloud~md~obsidian/Documents/vps-agent-notes"
git pull origin main --rebase
```

---

*Last updated: 2026-06-23 | Hub: [[graphify]]*
