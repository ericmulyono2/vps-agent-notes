# 🧠 MOC Memory — Agent Memory Systems

> **Peta seluruh sistem persistent memory untuk AI Agent di VPS srv1672787**
> Last updated: 2026-06-23

---

## Memory Architecture

```
┌─────────────────────────────────────────┐
│         AI_AGENT_CONTEXT (Universal)     │
│  /root/AI_AGENT_CONTEXT/                │
│  ├── rules/MASTER_RULES.md              │
│  ├── vps-system/VPS_PROFILE.md          │
│  ├── projects/PROJECT_INDEX.md          │
│  └── logs/SESSION_HANDOFF.md            │
├─────────────────────────────────────────┤
│         Project Memory (per-project)     │
│  /root/SIGMA_MEMORY.md                  │
│  /root/PROJECT_MEMORY.md                │
│  /root/AGENTS.md                        │
├─────────────────────────────────────────┤
│         Obsidian Vault (Git-synced)      │
│  /home/qwen-venice/obsidian-vault/      │
│  ├── memory/          ← agent notes     │
│  ├── agents/          ← agent output    │
│  ├── research/        ← riset & analisis│
│  ├── logs/            ← execution logs  │
│  └── daily/           ← daily notes     │
├─────────────────────────────────────────┤
│         DeepLake RAG (Vector)            │
│  Venice API → /v1/ingest                │
│  /v1/stats → query stats                │
└─────────────────────────────────────────┘
```

---

## 1. AI_AGENT_CONTEXT — Universal Memory

Path: `/root/AI_AGENT_CONTEXT/`

### Rules
- [[MASTER_RULES]] — Aturan universal untuk semua AI agent
  1. Memory First — baca memory sebelum kerja
  2. Project Awareness — baca project files
  3. Safety — no destructive commands tanpa approval
  4. Verification — verifikasi setelah action
  5. Handoff — update memory setelah selesai
  6. Communication — bahasa user, ringkas, root cause

### System
- [[VPS_PROFILE]] — Hardware, OS, software, paths, env vars

### Projects
- [[PROJECT_INDEX]] — Daftar semua project (Sigma Scalping, qwen-venice)

### Logs
- [[SESSION_HANDOFF]] — Handoff global antar session

---

## 2. Project Memory Files

### Sigma Scalping (Project Utama)
| File | Purpose | Agent |
|------|---------|-------|
| [[SIGMA_MEMORY]] | Orchestrator persistent memory — rules, team, config, fixes | Orchestrator (DeepSeek) |
| [[PROJECT_MEMORY]] | Session summaries + deployment log | CodeWhale |
| [[AGENTS]] | Project instructions untuk semua agent | All |
| [[KIMI]] | Kimi-specific project memory | Kimi |
| [[CODEWHALE]] | CodeWhale-specific instructions | CodeWhale |
| [[CLAUDE]] | Claude-specific instructions | Claude |

### qwen-venice (AI Gateway)
| File | Purpose |
|------|---------|
| `/home/qwen-venice/AGENTS.md` | Project instructions |
| [[PROJECT_PROFILE_qwen]] | qwen-venice profile |
| [[SESSION_HANDOFF_qwen]] | Session handoff |

---

## 3. Obsidian Vault — Git-Synced Memory

Path: `/home/qwen-venice/obsidian-vault/`
Git: `github.com:ericmulyono2/vps-agent-notes`

### Struktur
| Folder | Isi | Bridge |
|--------|-----|--------|
| `memory/` | Agent persistent notes | [[openclaw-bridge]], [[aider-bridge]] |
| `agents/openclaw/` | Output OpenClaw (DeepSeek V4-Pro) | [[openclaw-bridge]] |
| `agents/aider/` | Output Aider + Qwen Coder | [[aider-bridge]] |
| `research/` | Riset, analisis, report | All agents |
| `config/` | Bridge configs | [[aider-bridge]], [[openclaw-bridge]] |
| `logs/` | Execution logs | [[codewhale-session-2026-06-22]] |
| `daily/` | Catatan harian | All agents |

### Sync
```bash
# Push dari VPS ke GitHub
/home/qwen-venice/obsidian-vault/sync-obsidian.sh

# Pull di Macbook
cd "~/Documents/vps-agent-notes" && git pull origin main --rebase
```

---

## 4. DeepLake RAG — Vector Memory

- **Vector Store**: DeepLake
- **Endpoint**: `POST /v1/ingest` (ingest document)
- **Stats**: `GET /v1/stats`
- **Documents ingested**:
  - [[master-design-system-all-styles]] (id: `20260622T154758127819`)
  - [[super-prompt-qwen3-coder]]
- **Reports**: [[rag-deeplake-index]], [[rag-advanced-brain]]

---

## 5. Memory Flow — How Agents Read & Write

```
Agent Start
  ├── Baca /root/AI_AGENT_CONTEXT/logs/SESSION_HANDOFF.md
  ├── Baca /root/SIGMA_MEMORY.md (jika orchestrator)
  ├── Baca /root/AGENTS.md (project instructions)
  └── Baca vault notes via Obsidian sync

Agent Work
  ├── Tulis session log → vault/logs/
  ├── Tulis research → vault/research/
  └── Tulis agent output → vault/agents/<agent>/

Agent Done
  ├── Update SESSION_HANDOFF.md
  ├── Update PROJECT_MEMORY.md
  ├── Update SIGMA_MEMORY.md (jika orchestrator)
  └── Jalankan sync-obsidian.sh → push ke GitHub
```

---

## 6. Memory Rules (from MASTER_RULES)

1. **Memory First** — Baca memory files, jangan menebak
2. **Handoff** — Setiap selesai task, update SESSION_HANDOFF + project memory
3. **Verification** — Memory adalah sumber kebenaran, verifikasi dengan live data
4. **Ringkas** — Tulis jelas, bisa dipakai agent lain

---

## 🔗 Cross-Reference

- [[graphify]] — Agent MOC (hub utama)
- [[MOC Self-Learning]] — Self-improving systems
- [[MOC Skills]] — Skills catalog
- [[Kepala VPS Dashboard]] — Status实时 services
- [[README]] — Vault structure

---

*Memory adalah fondasi koordinasi multi-agent. Setiap agent harus membaca dan menulis memory dengan disiplin.*
