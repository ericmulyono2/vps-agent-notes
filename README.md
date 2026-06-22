# VPS Agent Notes — Obsidian Vault

> Jembatan antara Macbook Obsidian ↔ VPS Agent (OpenClaw + Aider + Qwen)

## Struktur

```
obsidian-vault/
├── daily/          ← Catatan harian, session log
├── memory/         ← Agent persistent memory
├── research/       ← Hasil riset, analisis trading
├── agents/
│   ├── openclaw/   ← Output OpenClaw (DeepSeek V4-Pro)
│   └── aider/      ← Output Aider + Qwen Coder
├── logs/           ← Agent execution logs
├── config/         ← Konfigurasi dan referensi
└── sync-obsidian.sh ← Script auto-sync Git
```

## Agents

| Agent | Model | Output Path |
|-------|-------|-------------|
| OpenClaw | DeepSeek V4-Pro | `agents/openclaw/` |
| Aider | Qwen Coder 480B | `agents/aider/` |
| CodeWhale | DeepSeek V4-Pro | `memory/`, `research/` |

## Sync

```bash
# Di VPS — push perubahan ke GitHub
./sync-obsidian.sh

# Di Macbook — pull perubahan dari GitHub
cd "/Users/ericmulyono/Library/Mobile Documents/iCloud~md~obsidian/Documents/vps-agent-notes"
git pull origin main --rebase
```

[[aider-bridge]] [[openclaw-bridge]]
