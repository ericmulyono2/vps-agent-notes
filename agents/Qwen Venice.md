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

- **[[aider-bridge|Aider + Qwen Coder]]** (XERO) — Code generation

---

## DeepLake RAG

- Vector store untuk document retrieval
- Ingestion: `POST /v1/ingest`
- Documents: [[master-design-system-all-styles]], [[super-prompt-qwen3-coder]]
- Reports: [[rag-deeplake-index]], [[rag-advanced-brain]]
- **Qwen Uncensored KB**: [[Qwen Uncensored KB Toolkit]] — separate Deep Lake dataset (Claude→Qwen uncensored prompts), integrable via `/v1/ingest`

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
- [[aider-bridge]] — Aider bridge config
- [[Qwen Uncensored KB Toolkit]] — Uncensored knowledge base builder

---

*Last updated: 2026-06-23*
