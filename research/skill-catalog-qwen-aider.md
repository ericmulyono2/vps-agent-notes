---
date: 2026-06-22
agent: deepseek-v4-pro
channel: codewhale
tags: [skills, catalog, aider, qwen-coder, tools]
---

# Skill Catalog — Qwen Coder + Aider

Katalog skill yang diinstal dari library CodeWhale/OpenClaw ke workspace [[aider-bridge]] untuk dipakai oleh Qwen Coder 480B dan Aider.

> Path instalasi: `/home/qwen-venice/coder-agent/skills/`

## 🔧 Debugging & Error Handling

| Skill | File | Deskripsi |
|-------|------|-----------|
| [[systematic-debugging]] | `SKILL.md` | Debugging 4-fase: root cause → pattern → hypothesis → fix. Iron law: NO fix without root cause. Max 3 auto-refactor attempts. |
| [[correctness-and-error-handling]] | `SKILL.md` | Auto-find + auto-fix bug, try/catch, error boundaries, loading/error/empty states. |
| [[self-repair]] | `SKILL.md` | Missing state triggers repair, not failure. Self-healing pattern. |
| [[autonomous-fixes]] | `SKILL.md` | Fix findings from autonomous-tests. Args: all, critical, high, vulnerability. |

## 🎨 Frontend & UI/UX

| Skill | File | Deskripsi |
|-------|------|-----------|
| [[frontend-design]] | `SKILL.md` | Production-grade UI dengan typography unik, bold aesthetic, anti-AI-slop. CSS animation, spatial composition, background effects. |
| [[web-artifacts-builder]] | `SKILL.md` | React 18 + TypeScript + Vite + Tailwind + shadcn/ui. Bundle ke single HTML artifact. |
| [[theme-factory]] | `SKILL.md` | 10 pre-set theme (Ocean Depths, Sunset Boulevard, Midnight Galaxy, dll) + custom theme generator. |
| [[web-design-guidelines]] | `SKILL.md` | Review UI compliance: accessibility, UX, best practices. Format `file:line`. |
| [[react-best-practices]] | `SKILL.md` | React/Next.js performance optimization: data fetching, rendering, bundling. |
| [[react-view-transitions]] | `SKILL.md` | View Transition API untuk animasi halaman native-feeling. |
| [[canvas-design]] | `SKILL.md` | Visual art .png/.pdf dengan design philosophy. Poster, art, static designs. |

## 🚀 Deployment (Vercel)

| Skill | File | Deskripsi |
|-------|------|-----------|
| [[deploy-to-vercel]] | `SKILL.md` | Deploy aplikasi/website ke Vercel. Preview deployment. |
| [[vercel-cli-with-tokens]] | `SKILL.md` | Vercel CLI dengan token-based auth. Env variables. |
| [[vercel-optimize]] | `SKILL.md` | Cost & performance optimization: Next.js, SvelteKit, Nuxt, Astro. |

## 🧠 Development Workflow

| Skill | File | Deskripsi |
|-------|------|-----------|
| [[brainstorming]] | `SKILL.md` | 9-step brainstorming: explore → questions → approaches → design → spec → review → plan. HARUS sebelum coding. |
| [[writing-plans]] | `SKILL.md` | Implementation plan granular: bite-sized tasks (2-5 min), exact file paths, full code in every step. |
| [[test-driven-development]] | `SKILL.md` | RED-GREEN-REFACTOR. Iron law: NO production code without failing test first. |
| [[subagent-driven-development]] | `SKILL.md` | Dispatch parallel sub-agents per task. Two-stage review. |
| [[verification-before-completion]] | `SKILL.md` | Verify every change before declaring done. |
| [[webapp-testing]] | `SKILL.md` | Playwright-based web app testing: screenshots, browser logs, UI verification. |

---

## Workflow Pipeline (Ideal)

```
brainstorming → writing-plans → subagent-driven-development
                                    ↓
                            systematic-debugging (jika ada bug)
                                    ↓
                            verification-before-completion
                                    ↓
                            deploy-to-vercel / vercel-cli-with-tokens
```

## Design Pipeline

```
brainstorming → frontend-design → theme-factory → web-artifacts-builder
                    ↓
            web-design-guidelines (review)
                    ↓
            react-best-practices (optimize)
```

---
*Terhubung ke:* [[aider-bridge]] | [[openclaw-bridge]] | [[rag-deeplake-index]] | [[ui-ux-connectors]]
