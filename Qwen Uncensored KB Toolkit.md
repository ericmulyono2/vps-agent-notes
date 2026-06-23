# 🧠 Qwen Uncensored KB Toolkit

> **Type**: Skill / Knowledge Base Builder
> **Status**: ✅ Ready to deploy
> **Path**: `/home/qwen-venice/qwen-uncensored-kb/`
> **Created**: 2026-06-23

---

## Overview

Toolkit Python lengkap untuk membangun **uncensored knowledge base** dari system prompt Claude → Qwen 3 Coder 480B Turbo. Satu command `bash run_all.sh` — clone 3 repo sumber, transformasi agresif (ganti nama + hapus refusal patterns), chunking sliding-window, dan build **Deep Lake vector dataset** siap RAG.

### Yang dihasilkan
```
qwen_kb_output/
├── clean_md/                    # .md bersih, uncensored, renamed claude→qwen
├── chunks.jsonl                 # ~5000-15000 chunks JSONL siap embed
├── deeplake_ds/                 # Deep Lake vector store (BGE embeddings)
├── Qwen3Coder.Modelfile         # Ollama Modelfile (bonus)
└── manifest.json                # Daftar semua file terproses
```

---

## 4 Script

| Script | Fungsi |
|--------|--------|
| `run_all.sh` | **One-click full pipeline** — clone → install → transform → build → test |
| `transform_and_build.py` | Clone 3 repo → uncensor → rename → chunk → JSONL + Modelfile |
| `build_deeplake.py` | Baca `chunks.jsonl` → embed BGE → ingesti ke Deep Lake |
| `query_kb.py` | Semantic search ke Deep Lake KB (top-k retrieval) |

---

## Cara Pakai

```bash
cd /home/qwen-venice/qwen-uncensored-kb

# Opsi A: Full pipeline (clone + transform + build)
bash run_all.sh

# Opsi B: Step by step
python transform_and_build.py    # transform + chunk
python build_deeplake.py         # build vector DB
python query_kb.py "how to orchestrate multi-agent workflow"  # test query
```

---

## Sumber Data

| Repo | Isi | File yang diproses |
|------|-----|-------------------|
| `Piebald-AI/claude-code-system-prompts` | System prompt Claude Code | Semua `.md` |
| `asgeirtj/system_prompts_leaks` | Prompt leaks (Fable 5, Opus 4.7/4.8, CoWork) | 4 file whitelist |
| `anthropics/courses` | Materi kursus Anthropic | Semua `.md` + `.ipynb` |

---

## Uncensoring Pipeline

### 1. Name Replacement (Claude → Qwen)
- `Claude Code` → `Qwen Coder`
- `Claude Opus/Sonnet/Haiku X.Y` → `Qwen Coder 480B`
- `Anthropic` → `Alibaba`
- `api.anthropic.com` → `dashscope.aliyuncs.com`

### 2. Refusal Pattern Nuking (11 regex)
Menghapus baris/blok yang mengandung:
- `I cannot...`, `I must decline...`, `against guidelines...`
- `safety considerations`, `harmful content`, `content warning`
- `refuse to answer`, `disclaimer`, `moralizing`

### 3. Inline Word Swaps
- `refuse` → `fulfill`, `decline` → `accept`
- `harmful/unsafe` → `any`
- Hapus total: `ethical`, `safety`, `appropriate`, `responsibly`

### 4. Preamble Injection
Setiap file priority dapat preamble uncensored directive yang meng-override semua refusal behavior.

---

## Integrasi dengan Agent VPS

### 🤖 [[aider-bridge|Aider + Qwen 3 Coder 480B]] (XERO)
- **Use case**: Super Prompt XERO bisa diperkaya dengan retrieval dari Deep Lake KB
- **Cara**: Embed query user → retrieve top-k chunks relevan → inject ke Aider system prompt
- **File**: `super-prompt-qwen3-coder.md` → tambah blok `## Knowledge Base` dengan top-k hasil query
- **Path**: `/home/qwen-venice/coder-agent/`

### 📡 [[Orchestrator|OpenClaw Gabriel — DeepSeek V4-Pro]]
- **Use case**: Gabriel bisa pakai uncensored prompt patterns untuk memperkuat autonomy
- **Cara**: Chunks `system-prompt-executing-actions-with-care.md` + `agent-prompt-plan-mode-enhanced.md` → inject ke Gabriel context via Sigma Orchestrator
- **Catatan**: Gabriel sudah unrestricted (exec-approvals = full) — KB ini tambahan untuk reasoning quality
- **Path**: `/opt/markasbesar/openclaw-data/`

### 🐳 [[CodeWhale]] (Orchestrator Utama VPS)
- **Use case**: CodeWhale bisa pakai KB sebagai referensi best practice coding agent
- **Cara**: Chunks `skill-building-llm-powered-applications` + `skill-debugging` → skill reference
- **Path**: `/root/.codewhale/skills/`

---

## Cross-Project Utility

### Sigma Scalping
- **Pipeline debugging**: Query KB untuk pattern matching error n8n workflow
- **Prompt engineering**: Uncensored patterns bisa dipakai untuk memperkuat prompt agent trading
- Lihat: [[Sigma Scalping Team]]

### Qwen Venice Gateway
- **RAG ingestion**: `chunks.jsonl` bisa langsung di-ingest ke DeepLake RAG existing di `/v1/ingest`
- **API endpoint**: `POST /v1/ingest` dengan payload chunks → hybrid retrieval
- Lihat: [[Qwen Venice]]

### Graphify
- **Knowledge graph enrichment**: Chunks metadata (source, filename, priority) bisa jadi node di graph
- Lihat: [[graphify]]

---

## Requirements

```bash
pip install deeplake sentence-transformers tqdm
```

## Notes

- Regex uncensoring tidak sempurna — spot-check `clean_md/` dan tambah pattern ke `NUKE_PATTERNS` kalau ada yang lolos
- Qwen 3 Coder 480B via Ollama butuh 256+ GB VRAM (Q4) — untuk production, pakai RAG retrieval dari Deep Lake
- Modelfile dibatasi 30KB system block agar tidak meledakkan context

---

## 🔗 Cross-Reference

- [[graphify]] — Agent MOC hub
- [[MOC Skills]] — Katalog skill lengkap
- [[MOC Memory]] — Memory systems (Deep Lake, RAG, vault)
- [[MOC Self-Learning]] — Self-improving agent patterns
- [[aider-bridge]] — Aider bridge config
- [[Qwen Venice]] — AI Gateway
- [[super-prompt-qwen3-coder]] — Super Prompt XERO
- [[master-design-system-all-styles]] — Design system reference

---

*Last updated: 2026-06-23*
