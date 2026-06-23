# 🔁 MOC Self-Learning — Self-Improving & Self-Healing Systems

> **Peta sistem yang membuat agent bisa belajar, memperbaiki diri, dan auto-heal**
> Last updated: 2026-06-23

---

## Arsitektur Self-Learning

```
┌──────────────────────────────────────────────┐
│           SELF-IMPROVING AGENT               │
│  Multi-Memory Architecture:                  │
│  ├── Semantic Memory  (pengetahuan umum)     │
│  ├── Episodic Memory  (pengalaman session)   │
│  └── Working Memory   (konteks aktif)        │
├──────────────────────────────────────────────┤
│           SELF-REPAIR SYSTEM                 │
│  Missing state → repair, not failure         │
│  Auto-detect + auto-fix pattern              │
├──────────────────────────────────────────────┤
│           AUTONOMOUS FIXES                   │
│  Fix findings from autonomous-tests          │
│  Args: all | critical | high | vulnerability │
├──────────────────────────────────────────────┤
│           AUTO-HEAL (Sigma)                  │
│  sigma_orchestrator_autoheal.py              │
│  Monitor service, auto-restart, alert        │
├──────────────────────────────────────────────┤
│           CORRECTNESS & ERROR HANDLING        │
│  Auto-find + auto-fix bugs                   │
│  Try/catch, error boundaries, edge cases     │
├──────────────────────────────────────────────┤
│           SYSTEMATIC DEBUGGING               │
│  4-fase: root cause → pattern → hypothesis   │
│  → fix. Iron law: NO fix without root cause  │
└──────────────────────────────────────────────┘
```

---

## 1. Self-Improving Agent

**Skill**: [[self-improving-agent]]
**Path**: `/root/.codewhale/skills/self-improving-agent/SKILL.md`

### Multi-Memory Architecture
| Memory Type | Fungsi | Persistensi |
|-------------|--------|-------------|
| **Semantic** | Pengetahuan umum, rules, best practices | Long-term |
| **Episodic** | Pengalaman session, successes, failures | Session → long-term |
| **Working** | Konteks aktif, current task state | Session only |

### Auto-Trigger Hooks
- `on_skill_complete` — belajar dari hasil skill
- `on_error` — belajar dari error
- `on_session_end` — simpulkan session

---

## 2. Self-Repair System

**Skill**: [[self-repair]]
**Path**: `/root/.codewhale/skills/self-repair/SKILL.md`

### Philosophy
> "Missing state triggers repair, not failure."

Ketika state hilang atau korup:
1. **Detect** — identifikasi apa yang hilang
2. **Diagnose** — cari root cause
3. **Repair** — restore dari backup atau regenerate
4. **Verify** — pastikan repair berhasil
5. **Prevent** — tambahkan safeguard

---

## 3. Autonomous Fixes

**Skill**: [[autonomous-fixes]]
**Path**: `/root/.codewhale/skills/autonomous-fixes/SKILL.md`

### Fix Levels
| Level | Trigger | Action |
|-------|---------|--------|
| `all` | Semua temuan | Fix semua issue |
| `critical` | Critical only | Fix yang bikin crash/break |
| `high` | High priority | Fix yang significant impact |
| `vulnerability` | Security | Fix security issues only |

---

## 4. Correctness & Error Handling

**Skill**: [[correctness-and-error-handling]]
**Path**: `/root/.codewhale/skills/correctness-and-error-handling/SKILL.md`

### Auto-Fix Patterns
- Unhandled Promise rejections → wrap try/catch
- Missing error states → tambah error boundaries
- Null/undefined access → guard clauses
- Edge-case failures → defensive programming

---

## 5. Systematic Debugging

**Skill**: [[systematic-debugging]]
**Path**: `/root/.codewhale/skills/systematic-debugging/SKILL.md`

### 4-Fase Protocol
```
FASE 1: ROOT CAUSE
  └─ Jangan fix gejala — temukan akar masalah

FASE 2: PATTERN
  └─ Apakah ini isolated atau systemic?

FASE 3: HYPOTHESIS
  └─ "Jika root cause adalah X, maka fix Y akan menyelesaikan"

FASE 4: FIX
  └─ Implementasi + verifikasi
  └─ Max 3 auto-refactor attempts
```

### Iron Law
> **NO fix without root cause.** Jangan pernah mengubah kode tanpa memahami MENGAPA error terjadi.

---

## 6. Sigma Auto-Heal

**Script**: `/root/sigma-scalping-team/sigma_orchestrator_autoheal.py`

### Monitor Targets
- n8n container — restart kalau crash
- OpenClaw container — restart kalau down
- Cron jobs — verify execution
- Workflow health — detect failure patterns
- Node.js v24 axios patch — re-apply kalau hilang

### Auto-Heal Flow
```
Monitor → Detect Anomaly → Diagnose → Auto-Fix → Verify → Alert (Telegram)
```

---

## 7. OpenClaw Self-Healing

**Skill**: [[openclaw-self-healing]]
**Path**: `/root/.codewhale/skills/openclaw-self-healing/SKILL.md`

### 4-Tier Autonomous System
| Tier | Level | Action |
|------|-------|--------|
| 1 | Auto-detect | Monitor health, detect anomaly |
| 2 | Auto-repair | Restart service, re-apply config |
| 3 | AI Doctor | Claude Code — AI-powered diagnosis |
| 4 | Human Alert | Telegram notification |

### Features
- Persistent learning — rekam pattern failure
- Reasoning logs — audit trail perbaikan
- Multi-channel alerts — Telegram + system log

---

## 8. Learning Loop — End-to-End

```
SESSION START
  ├── Baca episodic memory → pelajari session sebelumnya
  ├── Baca semantic memory → recall rules & patterns
  └── Load working memory → current context

SESSION WORK
  ├── Execute task
  ├── Jika error → self-repair / systematic debugging
  └── Rekam success/failure pattern

SESSION END
  ├── Self-improving agent hook → simpulkan pembelajaran
  ├── Update episodic memory → simpan pengalaman
  ├── Update semantic memory → tambah pengetahuan baru
  └── Handoff → SESSION_HANDOFF.md
```

### Knowledge Enrichment via Qwen Uncensored KB
Selain belajar dari session sendiri, agent juga bisa belajar dari **external knowledge base**:
- **[[Qwen Uncensored KB Toolkit]]**: Deep Lake vector store berisi system prompt Claude (uncensored + renamed → Qwen)
- Query semantic search untuk dapat best practices, debugging patterns, orchestration strategies
- Integrasi: Aider XERO, Gabriel OpenClaw, CodeWhale

---

## 🔗 Cross-Reference

- [[graphify]] — Agent MOC (hub utama)
- [[MOC Memory]] — Sistem memory agent
- [[MOC Skills]] — Katalog skill lengkap
- [[Qwen Uncensored KB Toolkit]] — Uncensored knowledge base
- [[skill-catalog-qwen-aider]] — Skill terinstal di Aider
- [[skills-installation-log]] — Installation log
- [[codewhale-session-2026-06-22]] — Contoh session log

---

*Self-learning adalah kunci agent yang semakin pintar dari waktu ke waktu. Setiap error adalah pelajaran, setiap session adalah pengalaman.*
