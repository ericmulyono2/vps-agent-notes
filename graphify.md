# 🕸️ Graphify — Agent Map of Content

> **Hub sentral seluruh AI Agent di ekosistem srv1672787**
> Last updated: 2026-06-23

---

## 🏗️ Core Infrastructure

Agent-agent yang menjalankan fondasi VPS — gateway, orchestration, dan administrasi sistem.

| Agent | Model | Role | Note |
|-------|-------|------|------|
| **[[openclaw-bridge|OpenClaw]]** (Gabriel) | DeepSeek V4-Pro / Kimi k2.7-code | SPV Decision Maker + Gateway | [[openclaw-bridge]] |
| **[[Qwen Venice]]** | Qwen 3 Coder 480B Turbo | AI Gateway — OpenAI-compatible bridge ke Venice.ai | [[Qwen Venice]] |
| **[[Qwen Venice|n8n]]** | — | Workflow Automation Engine (7 Sigma modules) | [[Qwen Venice]] |

### OpenClaw (Gabriel)
- **Gateway**: `http://31.97.220.82:18789`
- **Models**: Kimi k2.7-code (primary), DeepSeek V4-Pro (fallback)
- **Exec**: `security=full` — unrestricted VPS access
- **VPS Debug**: `docker exec -u root markasbesar-openclaw-1 nsenter -t 1 -a -- <cmd>`
- **Config**: `/opt/markasbesar/openclaw-data/openclaw.json` — **IMMUTABLE** (`chattr +i`)
- **Bridge**: [[openclaw-bridge]]

### Qwen Venice
- **Gateway**: `http://31.97.220.82:5050/v1`
- **Endpoints**: `/v1/chat/completions`, `/v1/ingest`, `/v1/stats`, `/health`
- **RAG**: DeepLake vector store
- **Bridge Note**: [[Qwen Venice]]

---

## 💻 Development Agents

Agent-agent untuk coding, design, dan software development.

| Agent | Model | Role | Note |
|-------|-------|------|------|
| **[[CodeWhale]]** | DeepSeek V4-Pro | Orchestrator utama — infra, config, auto-heal, skill/tools | [[CodeWhale]] |
| **[[aider-bridge|Aider + Qwen Coder]]** (XERO) | Qwen 3 Coder 480B Turbo | Code generation, UI/UX design, full-stack dev | [[aider-bridge]] |
| **[[super-prompt-qwen3-coder|XERO Super Prompt]]** | Qwen 3 Coder 480B | 558-line master prompt: glass effects, debugging, website builder | [[super-prompt-qwen3-coder]] |

### CodeWhale
- **Role**: Orchestrator — manages infrastructure, config, cron, auto-heal, model fallback, skill deployment
- **Tool**: terminal-based agent di VPS
- **Skills**: 50+ skill terinstal di `/root/.codewhale/skills/`
- **Memory**: [[codewhale-session-2026-06-22]] | `/root/AI_AGENT_CONTEXT/`
- **Note**: [[CodeWhale]]

### Aider + Qwen Coder (XERO)
- **Path**: `/home/qwen-venice/coder-agent/`
- **Super Prompt**: [[super-prompt-qwen3-coder]] (558 lines)
- **Design System**: [[master-design-system-all-styles]] (835 lines, 6 gaya)
- **Penpot**: `http://31.97.220.82:9001` (7 containers)
- **Bridge**: [[aider-bridge]]

---

## 📈 Trading / Sigma Scalping Agents

Tim agent dalam pipeline trading Sigma Scalping — dari pre-screen sampai eksekusi.

```
Pre-screen → Research → Quant → Risk → GABRIEL → Junior Trader → Senior Trader → BingX
                                              ↓
                                       SIGMA ORCHESTRATOR
```

### Team Structure

| Role | Agent | Model | Fungsi |
|------|-------|-------|--------|
| **Pre-screen** | Pre-screen Agent | LLM | Filter awal sinyal trading |
| **Research** | Research Agent | LLM | Riset market, analisis teknikal |
| **Quant** | Quant Agent | LLM | Analisis kuantitatif, probabilitas |
| **Risk** | Risk Agent | LLM | Manajemen risiko, exposure check |
| **SPV Decision** | Gabriel | Kimi k2.7-code | Supervisor — keputusan final trading |
| **Execute** | Junior Trader | n8n Code Node | Eksekusi order, hard check Rule #6 |
| **Settlement** | Senior Trader | n8n HTTP Request | Integrasi BingX API |
| **Orchestrate** | [[Orchestrator|Sigma Orchestrator]] | DeepSeek V4-Pro | Kelola infra, config, cron, auto-heal |

### Sigma Scalping Team Note
- [[Sigma Scalping Team]] — overview lengkap tim dan pipeline
- [[Orchestrator]] — detail orchestrator

### Key Workflows (n8n)
- `TRD_Sigma_Entry_Filter_Guard` — Gate filter entry
- `TRD_Sigma_Position_Manager` — Manajemen posisi + margin detection
- `TRD_Sigma_SLTP_Alert` — Stop loss / take profit
- `TRD_Sigma_Correlation_Filter` — Filter korelasi
- `TRD___Sigma_Balance_Monitor` — Monitor balance
- `TRD___Sigma_Risk_Monitor` — Monitor risiko
- `TRD___Sigma_PnL_Journal` — Jurnal profit/loss
- `TRD___Sigma_Manual_Position_Sync` — Sinkronisasi manual

### Rule #6 — Min Margin $10
Enforced di 5 layer:
1. Entry Filter Guard — warning note
2. Scalping Pre-Entry Gate — hard block (`MIN_NOTIONAL_USD = 50`)
3. Junior Trader Execute — hard reject (`position notional < $50`)
4. Position Manager — detection + danger zone flag
5. Orchestrator Python — hard check (`MIN_MARGIN_PER_POSITION = 10.0`)

---

## 🧠 Memory & Context Systems

Sistem persistent memory yang digunakan semua agent.

| Sistem | Path | Note |
|--------|------|------|
| **Agent Context** | `/root/AI_AGENT_CONTEXT/` | Memory universal — rules, profile, handoff |
| **Sigma Memory** | `/root/SIGMA_MEMORY.md` | Orchestrator persistent memory |
| **Project Memory** | `/root/PROJECT_MEMORY.md` | Session summaries |
| **Obsidian Vault** | `/home/qwen-venice/obsidian-vault/` | Git-synced vault untuk semua agent |
| **DeepLake RAG** | `vector store` | Document ingestion + retrieval |

→ Lihat [[MOC Memory]] untuk peta lengkap sistem memory.

---

## 🔁 Self-Learning & Self-Improving

Skill dan sistem yang membuat agent bisa belajar dan memperbaiki diri sendiri.

| Skill | Fungsi |
|-------|--------|
| **[[self-improving-agent]]** | Multi-memory architecture: semantic + episodic + working. Auto-triggers on skill completion/error |
| **[[self-repair]]** | Missing state triggers repair, not failure |
| **[[autonomous-fixes]]** | Fix findings from autonomous-tests |
| **[[correctness-and-error-handling]]** | Auto-find + auto-fix bugs, try/catch, error boundaries |
| **[[systematic-debugging]]** | 4-fase debugging: root cause → pattern → hypothesis → fix |

→ Lihat [[MOC Self-Learning]] untuk peta lengkap.

---

## 🛠️ Skills Catalog

Kumpulan skill yang tersedia untuk semua agent.

| Kategori | Jumlah | Note |
|----------|--------|------|
| Debugging | 4 skill | [[skill-catalog-qwen-aider]] |
| Frontend/UI | 7 skill | [[skill-catalog-qwen-aider]] |
| Deployment | 3 skill | [[skill-catalog-qwen-aider]] |
| Workflow | 6 skill | [[skill-catalog-qwen-aider]] |
| **Total** | **20+ skill** | [[skills-installation-log]] |

→ Lihat [[MOC Skills]] untuk katalog lengkap.

---

## 🌐 Tools & Utilities

Tools yang digunakan agent untuk berinteraksi dengan dunia luar.

| Tool | Fungsi | Note |
|------|--------|------|
| **[[agent-reach-skills|Agent-Reach]]** | Internet eyes — Twitter, Reddit, YouTube, Web, GitHub | Zero API fees |
| **[[rag-deeplake-index|DeepLake RAG]]** | Vector store + document retrieval | [[rag-advanced-brain]] |
| **[[graphify-coder-agent-report|Graphify]]** | Knowledge graph — 11,844 nodes, 17,989 edges | `/graphify` |
| **Penpot MCP** | Design manipulation via LLM | `http://31.97.220.82:4401/mcp` |
| **[[Qwen Uncensored KB Toolkit]]** | Claude→Qwen uncensored knowledge base + Deep Lake RAG | `/home/qwen-venice/qwen-uncensored-kb/` |

---

## 📊 Model Chain (Priority)

| Priority | Agent | Model | Context |
|----------|-------|-------|---------|
| **1** | Gabriel (SPV) | `moonshot/kimi-k2.7-code` | Vision, reasoning, 262K ctx |
| **2** | Gabriel (Fallback) | `deepseek/deepseek-v4-pro` | 1M ctx |
| **Orch** | Orchestrator | `deepseek/deepseek-v4-pro` | Kimi fallback |
| **XERO** | Aider | `qwen3-coder-480b-turbo` | Via Venice API |
| **Dev** | CodeWhale | `deepseek-v4-pro` | Terminal agent |

---

## 🔗 Cross-Reference

- [[MOC Memory]] — Sistem memory agent
- [[MOC Self-Learning]] — Self-improving & self-healing
- [[MOC Skills]] — Katalog skill lengkap
- [[Qwen Uncensored KB Toolkit]] — Uncensored knowledge base toolkit
- [[README]] — Struktur vault & sync guide
- [[AGENTS]] — Project instructions

---

*Hub ini menghubungkan seluruh ekosistem agent. Tambahkan agent baru di sini agar Graph View tetap terpusat.*
