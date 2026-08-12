# 📈 Sigma Scalping Team

> **Tim agent trading pipeline lengkap — Pre-screen sampai Settlement**
> Status: 🟢 Active | Project Utama VPS

---

## Pipeline

```
Pre-screen → Research → Quant → Risk → GABRIEL → Junior Trader → Senior Trader → BingX
                                              ↓
                                       SIGMA ORCHESTRATOR
```

---

## Team Members

| Role | Agent | Model | Fungsi |
|------|-------|-------|--------|
| Pre-screen | Pre-screen Agent | LLM | Filter awal sinyal — hard gate F&G < 30 |
| Research | Research Agent | LLM | Riset market, analisis teknikal |
| Quant | Quant Agent | LLM | Analisis kuantitatif, probabilitas |
| Risk | Risk Agent | LLM | Manajemen risiko, max exposure 250% |
| SPV Decision | Gabriel | Kimi k2.7-code | Supervisor — keputusan final |
| Execute | Junior Trader | n8n Code | Eksekusi order + Rule #6 check |
| Settlement | Senior Trader | n8n HTTP | Integrasi BingX API |
| Orchestrate | [[Orchestrator]] | DeepSeek V4-Pro | Infra, config, cron, auto-heal |

---

## Core Rules (SIGMA 2.0)

1. F&G <30 + price < SMA50 → NO LONG (SHORT/WAIT only)
2. Long confidence min 50%, Short min 40%
3. Max exposure 250% balance (50% margin @ 5x)
4. Min hold time 15 menit
5. 3 consecutive SL in 6h → PAUSE 6h
6. **Min margin per position $10** (effective size $50 @ 5x)

---

## ✅ Insiden 2026-08-12 — Rule #6 bocor di live, sudah dipatch & diverifikasi

Ditemukan 3 posisi live jauh di bawah $10 margin (BTC $1.25, ADA $2.81, AVAX $2.50) — bukan kejadian sekali, note Juni juga sempat catat "ETH-SHORT margin $3.14 — pre-Rule #6", jadi ini pola berulang.

**Akar masalah (dua kegagalan independen):**
- `sigma_tp_sl_guard.py` (auto-close margin < $10) ada di kode tapi **gak pernah jalan** — gak di cron, gak jadi service. → **Fixed**: dipasang cron `*/5 * * * *`.
- Kode **live** n8n "Junior Trader — Execute" (bukan file JSON di disk — itu basi/stale export, jangan dipercaya) sudah ter-degradasi dari versi yang didokumentasikan di atas: `minUSDT` kesulap dari $50 jadi $2 di semua simbol (floor efektif hilang), dan pre-check Rule #6 (`HARD_MIN_NOTIONAL`) hilang total dari kode live. → **Fixed**: dipatch balik via `n8n export:workflow` / `import:workflow` (bukan tulis sqlite langsung — riwayat corrupt ada), container di-restart.

**Verifikasi**: 3 posisi lama ditutup, cron guard tes manual jalan bersih, kode live diverifikasi ke-update di DB. Eksekusi live `244469` (03:15 UTC) dipantau — pipeline jalan sampe node setelah titik edit (Gabriel, RR Gate, Execute?), konfirmasi n8n eksekusi definisi workflow yang sekarang, bukan versi lama ke-cache. Cycle itu hasilnya "wait" (gak ada sinyal trade), jadi Junior Trader Execute gak sempet jalan pas itu.

Daripada nunggu jam buat sinyal trade natural (atau maksa manual-run yang risiko nembak order asli pake data cache lama), kode `Junior Trader — Execute` yang persis ke-deploy diambil terus dites standalone di Node (BingX call di-mock, gak ada order asli):
- `sizeUsd` default 61 (kasus umum), BTC → `actualNotional $50.96` → margin $10.19 @5x. **Lolos.**
- Sinyal size kecil eksplisit $20 → **ditolak**: `rejected_min_notional — Position notional $20.00 below minimum $50`.

Kesimpulan: logic sekarang matematis gak bisa hasilin order di bawah $10 margin, dan nolak sinyal kekecilan sebelum sempet order. Ditambah guard cron 5 menit sebagai jaring independen — Rule #6 sekarang dijaga di dua titik (entry gate + post-entry monitor). **Status: FIXED & VERIFIED** (2026-08-12). Belum ada bukti dari sinyal trade real pertama pasca-fix — kalau kejadian lagi, cek bagian "Insiden 2026-08-12" ini dulu (file JSON basi, risiko corrupt sqlite, wajib restart container).

**Pelajaran**: matrix enforcement di bawah ini (dari dulu) cuma menjelaskan *desain*, bukan bukti jalan. Ternyata beberapa layer di tabel bawah statusnya berbeda dari yang tercatat — lihat catatan status per baris.

---

## Rule #6 — Enforcement Matrix

| Layer | Mekanisme | Status live (dicek 2026-08-12) |
|-------|-----------|-------|
| Entry Filter Guard | Warning note | workflow n8n **nonaktif** di n8n (bukan aktif seperti tercatat di bawah) |
| Scalping Pre-Entry Gate | Hard block: `MIN_NOTIONAL_USD = 50` | node ini cuma cek drawdown/margin akun, **tidak** cek margin per-posisi — klaim di baris ini tidak akurat |
| Junior Trader Execute | Hard reject: `position notional < $50` | sempat hilang total dari kode live, **sudah dipatch balik** 2026-08-12 |
| Position Manager | Detection: margin < $10 → danger flag | workflow n8n `TRD - Sigma Position Manager` **nonaktif** di n8n |
| Orchestrator Python | Hard check: `MIN_MARGIN_PER_POSITION = 10.0` | kode ada & benar, tapi ini cuma advisory/veto scoring — tidak block order langsung |
| **Guard cron (baru)** | `sigma_tp_sl_guard.py` auto-close margin < $10 | **ditambahkan 2026-08-12** — cron tiap 5 menit, jaring pengaman independen dari n8n |

---

## n8n Workflows

- `TRD - Sigma Scalping` — workflow utama, ACTIVE, id `qUjwDi48068STPTK` (berisi node Junior Trader Execute)
- `TRD_Sigma_Entry_Filter_Guard` — nonaktif
- `TRD_Sigma_Position_Manager` — nonaktif
- `TRD_Sigma_SLTP_Alert` (nama DB: `TRD - Sigma SLTP Alert System`) — ACTIVE, cuma kirim Telegram alert pas close event, tidak eksekusi order
- `TRD_Sigma_Correlation_Filter` — nonaktif
- `TRD___Sigma_Balance_Monitor` — ACTIVE
- `TRD___Sigma_Risk_Monitor` — nonaktif
- `TRD___Sigma_PnL_Journal` — ACTIVE

---

## Current Market State

- Posisi: kosong (semua ditutup 2026-08-12 setelah insiden margin kecil)
- Guard cron aktif tiap 5 menit sejak 2026-08-12

---

## Key Files

| File | Purpose |
|------|---------|
| `/root/sigma-scalping-team/sigma_orchestrator.py` | Orchestrator main script |
| `/root/sigma-scalping-team/sigma_orchestrator_autoheal.py` | Auto-heal script |
| `/root/sigma-scalping-team/sigma_tp_sl_guard.py` | Margin/SL/TS guard — sekarang di-cron tiap 5 menit |
| `/root/SIGMA_MEMORY.md` | Orchestrator persistent memory |
| `/root/PROJECT_MEMORY.md` | Session summaries |

**Peringatan**: `~/sigma-scalping-team/trd_sigma_scalping_workflow.json` di disk itu **export basi**, beda dari kode yang beneran jalan di n8n. Buat cek kode live: `docker exec markasbesar-n8n-1 n8n export:workflow --id=qUjwDi48068STPTK --output=/tmp/x.json`.

---

## 🔗 Cross-Reference

- [[graphify]] — Agent MOC hub
- [[Orchestrator]] — Detail orchestrator

---

*Last updated: 2026-08-12*
