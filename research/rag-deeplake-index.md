---
date: 2026-06-22
agent: deepseek-v4-pro
channel: codewhale
tags: [rag, deeplake, index, knowledge-base]
---

# RAG DeepLake Index

> Status: **Dataset kosong** — belum ada dokumen yang di-index.
> Path: `/home/qwen-venice/data/rag_store/`
> Diperiksa: 2026-06-22 13:19 UTC

## Ringkasan

Database DeepLake untuk [[qwen-venice-container]] sudah dibuat dengan schema lengkap, tapi **belum ada satupun dokumen** yang di-ingest melalui endpoint `/v1/ingest`.

| Properti | Nilai |
|----------|-------|
| Total dokumen | **0** |
| Schema version | 3.9.52 |
| Embedding model | `all-MiniLM-L6-v2` (384 dimensi) |
| Similarity threshold | 0.35 |
| Retrieval K | 5 dokumen per query |

## Struktur Schema

Dataset memiliki tensor berikut:

| Tensor | Tipe | Deskripsi |
|--------|------|-----------|
| `text` | `htype="text"` | Konten dokumen |
| `embedding` | `htype="embedding"` | Vector embedding (384-d float32) |
| `metadata` | `htype="json"` | Metadata opsional (judul, sumber, tag, dll) |
| `id` | `htype="text"` | ID unik dokumen (auto-generate timestamp) |

## Cara Ingest Dokumen

```bash
curl -X POST http://localhost:5050/v1/ingest \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Dokumen rules trading Sigma Scalping: ...",
    "metadata": {
      "source": "sigma-scalping-team",
      "type": "trading-rules",
      "file": "SIGMA_MEMORY.md"
    }
  }'
```

## Rencana Index

Dokumen yang perlu di-index ke DeepLake (prioritas):

- [ ] [[SIGMA_MEMORY]] — rules + state orchestrator trading
- [ ] [[SESSION_HANDOFF]] — session handoff global
- [ ] [[MASTER_RULES]] — aturan universal semua agent
- [ ] [[VPS_PROFILE]] — profil hardware/software VPS
- [ ] [[PROJECT_INDEX]] — daftar project dan sub-komponen
- [ ] [[openclaw-bridge]] — konfigurasi OpenClaw → Obsidian
- [ ] [[aider-bridge]] — konfigurasi Aider → Obsidian
- [ ] [[AGENTS]] — project memory root workspace
- [ ] n8n workflow modules (`TRD_Sigma_*.json`)

## Referensi

- [[qwen-venice-container]] — container AI Gateway (port 5050)
- [[main.py (qwen-venice)]] — source code `/v1/ingest` endpoint
- [[aider-bridge]] — instruksi agent Aider
- [[openclaw-bridge]] — instruksi agent OpenClaw
- [[README]] — vault overview
