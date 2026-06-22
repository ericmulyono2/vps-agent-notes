# Aider + Qwen Coder → Obsidian Vault Bridge

## Path

| Kategori     | Path                                           |
| ------------ | ---------------------------------------------- |
| Agent Output | /home/qwen-venice/obsidian-vault/agents/aider/ |
| Research     | /home/qwen-venice/obsidian-vault/research/     |
| Logs         | /home/qwen-venice/obsidian-vault/logs/         |

## Aider Configuration

Tambahkan ke `.aider.conf.yml`:

```yaml
# Obsidian vault output
read: []
edit_format: diff
```

## Post-Session Hook

Setelah sesi Aider selesai, jalankan:
```bash
/home/qwen-venice/obsidian-vault/sync-obsidian.sh
```

Atau tambahkan sebagai cron:
```bash
*/30 * * * * /home/qwen-venice/obsidian-vault/sync-obsidian.sh
```

## File Format

Setiap output Aider sebaiknya menggunakan format:
```markdown
---
date: 2026-06-22
agent: qwen-coder-480b
channel: aider
tags: [code, design]
---
```

## Super Prompt — XERO

File prompt utama: `agents/aider/super-prompt-qwen3-coder.md`
- Agent: **XERO** (Qwen 3 Coder 480B Turbo)
- Isi: identitas, 12 glass effects library, protokol debugging, website builder, landing page anatomy
- Source di coder-agent: `/home/qwen-venice/coder-agent/super-prompt-qwen3-coder.md`

## Master Design System — 6 Aliran Desain

File: `agents/aider/master-design-system-all-styles.md`
- 6 aliran: Glassmorphism, Skeuomorphism, Neo Brutalism, Claymorphism, Minimalism, Liquid Glass
- DeepLake ingested (id: `20260622T154758127819`)
- Source: `/home/qwen-venice/coder-agent/master-design-system-all-styles.md`

Sinkron: setiap update di coder-agent → copy ke vault → `sync-obsidian.sh`

[[openclaw-bridge]] | [[super-prompt-qwen3-coder]] | [[master-design-system-all-styles]]
