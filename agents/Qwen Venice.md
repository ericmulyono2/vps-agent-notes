# 🌉 Qwen Venice — AI Gateway

> **OpenAI-compatible bridge ke Venice.ai + DeepLake RAG**
> Status: 🟢 Active | Port: 5050

---

## Overview

Qwen Venice adalah AI Gateway yang menjembatani semua agent ke model Qwen 3 Coder 480B Turbo via Venice.ai. Dibangun dengan Flask, berjalan di Docker container dengan akses isolated.

**Path**: `/home/qwen-venice/`
**Container**: `qwen-venice-container`

---

## Endpoints

| Method | Path | Fungsi |
|--------|------|--------|
| `POST` | `/v1/chat/completions` | OpenAI-compatible chat (streaming + non-streaming) |
| `POST` | `/v1/ingest` | RAG document ingestion ke DeepLake |
| `GET` | `/v1/stats` | DeepLake vector store stats |
| `GET` | `/health` | Health check |

---

## Agents yang Menggunakan

- **[[Kepala VPS Dashboard|VEGA]]** (OpenHands) — Telegram Bot + Dashboard
- **[[aider-bridge|Aider + Qwen Coder]]** (XERO) — Code generation
- **[[VEGA - Super Prompt|VEGA CLI]]** — Terminal chat

---

## DeepLake RAG

- Vector store untuk document retrieval
- Ingestion: `POST /v1/ingest`
- Documents: [[master-design-system-all-styles]], [[super-prompt-qwen3-coder]]
- Reports: [[rag-deeplake-index]], [[rag-advanced-brain]]

---

## Main Commands

```bash
/home/qwen-venice/agent-start.sh              # start / rebuild
docker logs qwen-venice-container --tail 20
curl http://localhost:5050/health
```

---

## 🔗 Cross-Reference

- [[graphify]] — Agent MOC hub
- [[Kepala VPS Dashboard]] — Service dashboard
- [[aider-bridge]] — Aider bridge config

---

*Last updated: 2026-06-23*
