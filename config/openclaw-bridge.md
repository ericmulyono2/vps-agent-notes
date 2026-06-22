# OpenClaw → Obsidian Vault Bridge
# 
# File ini dibaca oleh OpenClaw agents (DeepSeek V4-Pro) untuk mengetahui
# di mana harus menulis output persistent (memori, logs, catatan).
#
# Path di dalam container: /home/node/.openclaw/obsidian-vault
# Path di host:            /home/qwen-venice/obsidian-vault

## Output Paths

| Kategori       | Path dalam container                               |
|----------------|----------------------------------------------------|
| Memory         | $OBSIDIAN_VAULT/memory/                            |
| Agent Output   | $OBSIDIAN_VAULT/agents/openclaw/                   |
| Research       | $OBSIDIAN_VAULT/research/                          |
| Logs           | $OBSIDIAN_VAULT/logs/                              |
| Daily Notes    | $OBSIDIAN_VAULT/daily/                             |

## Instructions for OpenClaw Agents

1. Setiap kali menulis file persistent (memori, analisis, laporan), gunakan
   path `$OBSIDIAN_VAULT` (env var) atau `/home/node/.openclaw/obsidian-vault`.

2. Format file: Markdown dengan frontmatter YAML:
   ```yaml
   ---
   date: 2026-06-22
   agent: deepseek-v4-pro
   channel: openclaw
   tags: [trading, sigma]
   ---
   ```

3. Setelah menulis, jalankan `$OBSIDIAN_VAULT/sync-obsidian.sh` untuk push ke GitHub.

4. JANGAN menimpa file yang sudah ada tanpa konfirmasi — selalu append atau
   buat file baru dengan timestamp.

## Sync Cron (opsional)

Untuk auto-sync berkala, tambahkan cron:
```bash
# Setiap 30 menit
*/30 * * * * /home/qwen-venice/obsidian-vault/sync-obsidian.sh
```
