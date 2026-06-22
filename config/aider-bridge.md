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

[[openclaw-bridge]]
