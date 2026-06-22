# 🌐 Agent-Reach — Internet Eyes for AI Agents

> Status: **Active** | Zero API Fees | Installed: 2026-06-22

Agent-Reach adalah "Sepasang Mata" bagi AI coding agent ([[aider-bridge]] / [[openclaw-bridge]]). Membungkus alat pencarian, pembaca media sosial, dan pengekstraksi konten ke dalam satu CLI terpadu — tanpa biaya API.

## 🛠️ Perintah yang Tersedia

### Twitter/X — `agent-reach twitter search`
```bash
agent-reach twitter search "langchain AI agent" --limit 10
agent-reach twitter search "deepseek v4" --json --limit 5
```
- Backend: snscrape (no API key)
- Output: human-readable atau `--json`

### Reddit — `agent-reach reddit search`
```bash
agent-reach reddit search "LLM benchmark" --limit 10
```
- Backend: snscrape (no API key)

### YouTube — `agent-reach youtube transcript`
```bash
agent-reach youtube transcript "https://youtube.com/watch?v=xxx"
agent-reach youtube transcript "https://youtube.com/watch?v=xxx" --lang id
```
- Backend: yt-dlp
- Output: transkrip teks bersih (VTT/SRT → plain text)

### YouTube — `agent-reach youtube info`
```bash
agent-reach youtube info "https://youtube.com/watch?v=xxx"
```
- Output: JSON metadata (title, description, duration, views, channel)

### Web Fetch — `agent-reach web fetch`
```bash
agent-reach web fetch "https://docs.python.org/3/library/asyncio.html"
```
- Backend: Jina Reader (`r.jina.ai`) — gratis
- Output: Markdown bersih dari halaman web mana pun

### GitHub Issues — `agent-reach github issues`
```bash
agent-reach github issues "safishamsi/graphify"
agent-reach github issues "microsoft/vscode" --limit 20
```
- Backend: GitHub CLI (`gh`) — sudah terautentikasi

### GitHub Search — `agent-reach github search`
```bash
agent-reach github search "AI agent framework"
```
- Output: daftar repo dengan stars, language, description

## 📂 Lokasi File

| Lokasi | Path |
|--------|------|
| CLI Script | `/usr/local/bin/agent-reach` → `/home/qwen-venice/coder-agent/agent_reach.py` |
| Obsidian Copy | `agents/aider/agent_reach.py` |
| Dependencies | yt-dlp, snscrape, gallery-dl, gh, curl |

## 🔗 Referensi

- [[PROJECT_INDEX]] — project overview
- [[aider-bridge]] — Aider + Qwen Coder connector
- [[openclaw-bridge]] — OpenClaw + DeepSeek connector
- [[super-prompt-qwen3-coder]] — XERO identity
- [[Graphify]] — knowledge graph tool
- [[CONVENTIONS]] — coding conventions

---
*Terhubung ke VPS srv1672787. Semua tools zero API fees.*
