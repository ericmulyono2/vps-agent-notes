
master-design-system-all-styles.md
---
tags: [design-system, css, glassmorphism, skeuomorphism, neo-brutalism, claymorphism, minimalism, liquid-glass]
links: [[Framer Motion]], [[ui ux promax]], [[21st dev]], [[Figma]], [[Penpot]]
---

# 🎨 MASTER DESIGN SYSTEM — 6 ALIRAN DESAIN
Core Effect Arsenal
CSS
/* 1. Classic */
.glass { background: var(--glass-bg); backdrop-filter: var(--glass-blur); border: var(--glass-border); border-radius: var(--glass-radius); box-shadow: var(--glass-shadow); }

/* 2. Neon Glow */
.glass-neon { background: rgba(0,245,255,0.04); backdrop-filter: var(--glass-blur); border: var(--glass-neon-border); box-shadow: var(--glass-neon-glow); transition: box-shadow 0.3s ease; }
.glass-neon:hover { box-shadow: 0 0 30px rgba(0,245,255,0.3), 0 0 80px rgba(0,245,255,0.15), inset 0 0 30px rgba(0,245,255,0.06); }

/* 3. Frosted Ice */
.glass-frosted { backdrop-filter: var(--glass-frosted-blur); background: rgba(220,235,255,0.12); border: 1px solid rgba(255,255,255,0.25); box-shadow: inset 0 0 0 1px rgba(255,255,255,0.05), 0 20px 40px rgba(0,20,60,0.3); }

/* 4. Specular Highlight */
.glass-specular { backdrop-filter: blur(24px); background: rgba(255,255,255,0.07); border: 1px solid rgba(255,255,255,0.15); box-shadow: var(--glass-specular-inset), 0 20px 60px rgba(0,0,0,0.4); }

/* 5. Prismatic (Rotating Rainbow Border) */
.glass-prismatic { backdrop-filter: var(--glass-blur); background: rgba(10,10,20,0.4); border-radius: 24px; position: relative; }
.glass-prismatic::before { content: ""; position: absolute; inset: -2px; border-radius: 26px; background: conic-gradient(from 0deg, #00f5ff, #7b2fff, #ff006e, #ffbe00, #00f5ff); z-index: -1; animation: prismaRotate 4s linear infinite; filter: blur(1px); }
@keyframes prismaRotate { to { transform: rotate(360deg); } }

/* 6. Noise Texture */
.glass-noise::after { content: ""; position: absolute; inset: 0; border-radius: inherit; background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E"); opacity: 0.04; pointer-events: none; }

/* 7. Liquid Morph */
.glass-liquid { backdrop-filter: var(--glass-blur); background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.1); animation: liquidMorph 8s ease-in-out infinite; }
@keyframes liquidMorph { 0%,100% { border-radius: 60% 40% 30% 70%/60% 30% 70% 40%; } 50% { border-radius: 30% 60% 70% 40%/50% 60% 30% 60%; } }

/* 8. Electric Scan */
.glass-electric { position: relative; backdrop-filter: var(--glass-blur); background: rgba(0,245,255,0.03); border: 1px solid rgba(0,245,255,0.2); overflow: hidden; }
.glass-electric::before { content: ""; position: absolute; top: -10%; left: 0; width: 100%; height: 2px; background: linear-gradient(90deg, transparent, rgba(0,245,255,0.8), transparent); animation: scanLine 3s linear infinite; box-shadow: 0 0 10px rgba(0,245,255,0.5); }
@keyframes scanLine { to { top: 110%; } }

/* 9. Chromatic Aberration */
.glass-chromatic { position: relative; backdrop-filter: blur(18px); background: rgba(255,255,255,0.05); }
.glass-chromatic::before { content: ""; position: absolute; inset: -1px; border-radius: inherit; border: 1px solid rgba(255,0,80,0.4); transform: translate(-2px,-1px); pointer-events: none; }
.glass-chromatic::after { content: ""; position: absolute; inset: -1px; border-radius: inherit; border: 1px solid rgba(0,245,255,0.4); transform: translate(2px,1px); pointer-events: none; }

/* 10. Aurora */
.glass-aurora { backdrop-filter: blur(12px) saturate(200%); background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); animation: auroraShift 10s ease-in-out infinite alternate; }
@keyframes auroraShift { 0% { background: rgba(123,47,255,0.08); } 50% { background: rgba(0,245,255,0.08); } 100% { background: rgba(255,0,110,0.08); } }
Best Used On
Dark backgrounds #050510 — #0A0A1A
Colorful/gradient backgrounds untuk efek blur maksimal
🪵 2. SKEUOMORPHISM
Filosofi
"Digital yang terasa fisik. Jika bisa dipegang, artinya desain berhasil." Meniru material dunia nyata: kulit, kayu, logam, kertas, kain.

Design Tokens
CSS
:root {
  /* Surface */
  --skeuo-bg: #f0ece4;
  --skeuo-surface: #faf8f4;
  --skeuo-surface-dark: #e8e0d0;

  /* Shadows (kunci utama skeuomorphism) */
  --skeuo-shadow-raised:
    0 1px 0 rgba(255,255,255,0.8) inset,        /* top highlight */
    0 -1px 0 rgba(0,0,0,0.1) inset,             /* bottom shadow */
    0 4px 6px rgba(0,0,0,0.15),                  /* drop shadow */
    0 1px 3px rgba(0,0,0,0.1);
  --skeuo-shadow-pressed:
    0 1px 0 rgba(255,255,255,0.5) inset,
    0 2px 6px rgba(0,0,0,0.2) inset,            /* pressed inset */
    0 1px 2px rgba(0,0,0,0.1);

  /* Textures */
  --skeuo-leather: repeating-linear-gradient(
    45deg, rgba(0,0,0,0.02) 0px, rgba(0,0,0,0.02) 1px,
    transparent 1px, transparent 6px
  );
  --skeuo-metal: linear-gradient(
    180deg,
    rgba(255,255,255,0.3) 0%,
    rgba(255,255,255,0.1) 40%,
    rgba(0,0,0,0.05) 60%,
    rgba(0,0,0,0.1) 100%
  );
  --skeuo-wood: repeating-linear-gradient(
    90deg,
    rgba(139,90,43,0.15) 0px, rgba(160,110,60,0.1) 2px,
    transparent 2px, transparent 8px
  );
}
Core Effects
CSS
/* Button Raised */
.skeuo-button {
  background: linear-gradient(180deg, #f5f2ec 0%, #ddd8cc 100%);
  border: 1px solid #c0b8a8;
  border-radius: 10px;
  box-shadow: var(--skeuo-shadow-raised);
  padding: 12px 28px;
  font-family: 'Georgia', serif;
  color: #5a4a35;
  cursor: pointer;
  transition: all 0.1s ease;
  /* Noise texture overlay */
  background-image: var(--skeuo-leather),
    linear-gradient(180deg, #f5f2ec 0%, #ddd8cc 100%);
}

.skeuo-button:active {
  box-shadow: var(--skeuo-shadow-pressed);
  background: linear-gradient(180deg, #ddd8cc 0%, #f5f2ec 100%);
  transform: translateY(1px);
}

/* Metal Card */
.skeuo-metal-card {
  background: linear-gradient(160deg, #e8e8e8 0%, #c8c8c8 40%, #b0b0b0 100%);
  background-image: var(--skeuo-metal);
  border: 1px solid #a0a0a0;
  border-radius: 12px;
  box-shadow:
    0 2px 0 rgba(255,255,255,0.6) inset,
    0 -1px 0 rgba(0,0,0,0.15) inset,
    0 8px 20px rgba(0,0,0,0.25),
    0 1px 0 rgba(255,255,255,0.8);
  padding: 24px;
}

/* Leather Card */
.skeuo-leather-card {
  background: #8B5E3C;
  background-image: var(--skeuo-leather);
  border-radius: 8px;
  border: 2px solid #6B4423;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.15),
    0 4px 8px rgba(0,0,0,0.4),
    0 1px 0 rgba(255,255,255,0.1);
  padding: 24px;
  color: #f5e6d0;
}

/* Stitching Effect (jahitan) */
.skeuo-stitched {
  background: #2d5a1b;
  border: 3px solid #1a3d0f;
  border-radius: 12px;
  padding: 20px;
  position: relative;
  box-shadow: 0 4px 12px rgba(0,0,0,0.4);
}

.skeuo-stitched::before {
  content: "";
  position: absolute;
  inset: 6px;
  border-radius: 8px;
  border: 2px dashed rgba(255,255,255,0.25);
  pointer-events: none;
}

/* Toggle Switch Realistic */
.skeuo-toggle {
  width: 56px; height: 28px;
  background: linear-gradient(180deg, #b0b0b0, #d8d8d8);
  border-radius: 14px;
  border: 1px solid #999;
  box-shadow: inset 0 2px 4px rgba(0,0,0,0.3), 0 1px 0 rgba(255,255,255,0.8);
  position: relative;
  cursor: pointer;
}

.skeuo-toggle.on {
  background: linear-gradient(180deg, #2a7a1a, #4aac2a);
  border-color: #1a5a10;
}

.skeuo-toggle::after {
  content: "";
  position: absolute;
  top: 3px; left: 3px;
  width: 22px; height: 22px;
  border-radius: 50%;
  background: linear-gradient(160deg, #fff 0%, #e0e0e0 100%);
  box-shadow: 0 2px 4px rgba(0,0,0,0.3), 0 1px 0 rgba(255,255,255,0.8) inset;
  transition: left 0.2s ease;
}

.skeuo-toggle.on::after { left: 31px; }

/* Knob/Dial */
.skeuo-knob {
  width: 64px; height: 64px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 35%, #e8e8e8, #888);
  border: 2px solid #666;
  box-shadow:
    0 4px 8px rgba(0,0,0,0.5),
    inset 0 2px 3px rgba(255,255,255,0.5),
    inset 0 -2px 3px rgba(0,0,0,0.3);
}
Fonts Wajib Skeuomorphism
Code
Heading : Georgia, Palatino, Baskerville
Body    : Charter, Cambria, Times New Roman
UI      : Helvetica Neue, San Francisco
Mono    : Courier New, Monaco
💥 3. NEO BRUTALISM
Filosofi
"Jujur secara visual. Tidak ada yang disembunyikan. Struktur IS desain." Anti-polish. Pro-bold. Raw = intentional.

Design Tokens
CSS
:root {
  /* Neo Brut Colors */
  --brut-black: #0D0D0D;
  --brut-white: #FAFAFA;
  --brut-yellow: #FFE600;
  --brut-pink: #FF3366;
  --brut-cyan: #00E5FF;
  --brut-lime: #CCFF00;
  --brut-orange: #FF6600;
  --brut-purple: #9900FF;

  /* Border */
  --brut-border: 3px solid #0D0D0D;
  --brut-border-thick: 5px solid #0D0D0D;

  /* Shadow (offset, bukan blur) */
  --brut-shadow-sm: 4px 4px 0px #0D0D0D;
  --brut-shadow-md: 6px 6px 0px #0D0D0D;
  --brut-shadow-lg: 8px 8px 0px #0D0D0D;
  --brut-shadow-xl: 12px 12px 0px #0D0D0D;
  --brut-shadow-color: 6px 6px 0px var(--brut-pink);

  /* Typography */
  --brut-font-display: 'Space Grotesk', 'Arial Black', sans-serif;
  --brut-font-mono: 'Space Mono', 'Courier New', monospace;
}
Core Components
CSS
/* Card */
.brut-card {
  background: var(--brut-yellow);
  border: var(--brut-border-thick);
  border-radius: 0;                            /* NO border radius */
  box-shadow: var(--brut-shadow-lg);
  padding: 24px;
  transition: transform 0.1s ease, box-shadow 0.1s ease;
}

.brut-card:hover {
  transform: translate(-3px, -3px);
  box-shadow: 11px 11px 0px #0D0D0D;          /* shadow grows on hover */
}

/* Button */
.brut-button {
  background: var(--brut-pink);
  color: var(--brut-white);
  border: var(--brut-border-thick);
  border-radius: 0;
  padding: 14px 32px;
  font-family: var(--brut-font-mono);
  font-size: 1rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  box-shadow: var(--brut-shadow-md);
  cursor: pointer;
  transition: all 0.1s ease;
}

.brut-button:hover {
  transform: translate(-2px, -2px);
  box-shadow: 8px 8px 0px #0D0D0D;
}

.brut-button:active {
  transform: translate(4px, 4px);
  box-shadow: 2px 2px 0px #0D0D0D;           /* pressed: shadow shrinks */
}

/* Tag / Badge */
.brut-tag {
  display: inline-block;
  background: var(--brut-cyan);
  border: 2px solid var(--brut-black);
  border-radius: 0;
  padding: 4px 12px;
  font-family: var(--brut-font-mono);
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  box-shadow: 3px 3px 0px #0D0D0D;
}

/* Input */
.brut-input {
  background: var(--brut-white);
  border: var(--brut-border-thick);
  border-radius: 0;
  padding: 12px 16px;
  font-family: var(--brut-font-mono);
  font-size: 1rem;
  box-shadow: 4px 4px 0px #0D0D0D;
  outline: none;
  width: 100%;
  transition: box-shadow 0.15s ease;
}

.brut-input:focus {
  box-shadow: 4px 4px 0px var(--brut-pink);   /* shadow changes color on focus */
}

/* Marquee Stripe */
.brut-stripe {
  background: var(--brut-black);
  color: var(--brut-yellow);
  font-family: var(--brut-font-mono);
  font-weight: 700;
  text-transform: uppercase;
  padding: 12px 0;
  letter-spacing: 0.1em;
  overflow: hidden;
  white-space: nowrap;
}

/* Diagonal Cross Pattern Background */
.brut-pattern-bg {
  background-color: var(--brut-white);
  background-image: repeating-linear-gradient(
    45deg,
    var(--brut-black) 0px,
    var(--brut-black) 1px,
    transparent 1px,
    transparent 10px
  );
}

/* Squiggly underline (hand-drawn feel) */
.brut-underline {
  text-decoration: underline;
  text-decoration-style: wavy;
  text-decoration-color: var(--brut-pink);
  text-underline-offset: 4px;
}
Palette Combos
Code
Combo 1 (High Energy) : Yellow #FFE600 + Pink #FF3366 + Black
Combo 2 (Cyber)       : Black + Cyan #00E5FF + White
Combo 3 (Lime Punch)  : Lime #CCFF00 + Purple #9900FF + Black
Combo 4 (Warm Brut)   : Orange #FF6600 + Black + White
🫧 4. CLAYMORPHISM
Filosofi
"Kalau kamu bisa merasakan ingin memencetnya, desain berhasil." 3D, puffy, squishy, colorful, playful. Seperti mainan clay beneran.

Design Tokens
CSS
:root {
  /* Clay Base Colors (selalu pastel atau vibrant) */
  --clay-pink: #FF6B9D;
  --clay-purple: #C77DFF;
  --clay-blue: #4CC9F0;
  --clay-green: #52B788;
  --clay-yellow: #FFD166;
  --clay-orange: #F77F00;

  /* Clay Shadow Formula:
     outer shadow (dark-warm) +
     outer shadow (light-cold) +
     inner shadow bright (highlight) +
     inner shadow dark (depth)
  */
  --clay-shadow-pink:
    8px 8px 20px rgba(255, 107, 157, 0.5),    /* outer warm */
    -4px -4px 12px rgba(255, 200, 220, 0.8),  /* outer light */
    inset 4px 4px 8px rgba(255, 220, 235, 0.9), /* inner highlight */
    inset -6px -6px 16px rgba(200, 50, 100, 0.25); /* inner depth */

  --clay-shadow-blue:
    8px 8px 20px rgba(76, 201, 240, 0.5),
    -4px -4px 12px rgba(200, 240, 255, 0.8),
    inset 4px 4px 8px rgba(210, 245, 255, 0.9),
    inset -6px -6px 16px rgba(20, 100, 180, 0.25);
}
Core Components
CSS
/* Clay Card Base */
.clay-card {
  border-radius: 28px;
  padding: 28px;
  position: relative;
  transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1),
              box-shadow 0.2s ease;
}

/* Pink Clay */
.clay-pink {
  background: linear-gradient(135deg, #FFB3CC 0%, #FF6B9D 100%);
  box-shadow: var(--clay-shadow-pink);
  border: none;
}

/* Blue Clay */
.clay-blue {
  background: linear-gradient(135deg, #A8E6FF 0%, #4CC9F0 100%);
  box-shadow: var(--clay-shadow-blue);
}

/* Clay Push (hover squish) */
.clay-card:hover {
  transform: translateY(-4px) scale(1.02);
  box-shadow:
    12px 12px 28px rgba(var(--clay-r), var(--clay-g), var(--clay-b), 0.6),
    -6px -6px 16px rgba(255, 255, 255, 0.9),
    inset 4px 4px 8px rgba(255, 255, 255, 0.9),
    inset -8px -8px 20px rgba(0, 0, 0, 0.15);
}

/* Clay Button */
.clay-button {
  background: linear-gradient(135deg, #C77DFF 0%, #9B4FCC 100%);
  border: none;
  border-radius: 20px;
  padding: 16px 36px;
  font-size: 1rem;
  font-weight: 700;
  color: white;
  cursor: pointer;
  box-shadow:
    6px 6px 16px rgba(155, 79, 204, 0.5),
    -3px -3px 10px rgba(220, 180, 255, 0.8),
    inset 3px 3px 6px rgba(230, 200, 255, 0.8),
    inset -4px -4px 12px rgba(100, 30, 160, 0.3);
  transition: all 0.15s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.clay-button:hover {
  transform: translateY(-3px) scale(1.04);
}

.clay-button:active {
  transform: translateY(2px) scale(0.97);
  box-shadow:
    2px 2px 6px rgba(155, 79, 204, 0.4),
    inset 6px 6px 16px rgba(100, 30, 160, 0.4),
    inset -2px -2px 6px rgba(230, 200, 255, 0.5);
}

/* Clay Avatar / Icon Container */
.clay-avatar {
  width: 64px; height: 64px;
  border-radius: 50%;
  background: linear-gradient(135deg, #FFD166 0%, #F77F00 100%);
  box-shadow:
    5px 5px 15px rgba(247, 127, 0, 0.45),
    -3px -3px 10px rgba(255, 240, 180, 0.9),
    inset 3px 3px 6px rgba(255, 245, 200, 0.9),
    inset -4px -4px 10px rgba(180, 80, 0, 0.25);
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Clay Blob Background */
.clay-blob {
  border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
  animation: clayBlobMorph 6s ease-in-out infinite;
  background: linear-gradient(135deg, #C77DFF, #4CC9F0);
  filter: blur(0px);
  box-shadow:
    10px 10px 30px rgba(100, 100, 255, 0.3),
    -10px -10px 30px rgba(200, 200, 255, 0.5),
    inset 5px 5px 15px rgba(255, 255, 255, 0.4);
}

@keyframes clayBlobMorph {
  0%, 100% { border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%; }
  33%  { border-radius: 30% 60% 70% 40% / 50% 60% 30% 60%; }
  66%  { border-radius: 50% 30% 60% 40% / 40% 70% 30% 60%; }
}
◻️ 5. MINIMALISM
Filosofi
"Sempurna bukan saat tidak ada yang bisa ditambahkan, tapi saat tidak ada yang bisa dihapus." Whitespace = luxury. Typography = hero. Setiap elemen harus earn its place.

Design Tokens
CSS
:root {
  /* Monochrome Core */
  --min-black: #0A0A0A;
  --min-gray-900: #111111;
  --min-gray-700: #333333;
  --min-gray-500: #666666;
  --min-gray-300: #AAAAAA;
  --min-gray-100: #F5F5F5;
  --min-white: #FAFAFA;

  /* Single Accent */
  --min-accent: #0066FF;       /* Replace with brand color */
  --min-accent-subtle: rgba(0, 102, 255, 0.08);

  /* Typography Scale */
  --min-font-xs: 0.75rem;      /* 12px */
  --min-font-sm: 0.875rem;     /* 14px */
  --min-font-base: 1rem;       /* 16px */
  --min-font-md: 1.125rem;     /* 18px */
  --min-font-lg: 1.5rem;       /* 24px */
  --min-font-xl: 2rem;         /* 32px */
  --min-font-2xl: 3rem;        /* 48px */
  --min-font-3xl: 4.5rem;      /* 72px */

  /* Spacing (8px grid) */
  --min-space-1: 0.5rem;       /* 8px */
  --min-space-2: 1rem;         /* 16px */
  --min-space-3: 1.5rem;       /* 24px */
  --min-space-4: 2rem;         /* 32px */
  --min-space-6: 3rem;         /* 48px */
  --min-space-8: 4rem;         /* 64px */
  --min-space-12: 6rem;        /* 96px */
  --min-space-16: 8rem;        /* 128px */

  /* Borders */
  --min-border: 1px solid #E5E5E5;
  --min-border-subtle: 1px solid rgba(0,0,0,0.06);

  /* Shadows (barely there) */
  --min-shadow-xs: 0 1px 2px rgba(0,0,0,0.04);
  --min-shadow-sm: 0 2px 8px rgba(0,0,0,0.06);
  --min-shadow-md: 0 4px 24px rgba(0,0,0,0.08);
}
Core Components
CSS
/* Body & Base */
body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  font-size: var(--min-font-base);
  color: var(--min-black);
  background: var(--min-white);
  line-height: 1.7;
  letter-spacing: -0.01em;
  -webkit-font-smoothing: antialiased;
}

/* Display Heading */
.min-display {
  font-size: var(--min-font-3xl);
  font-weight: 700;
  line-height: 1.05;
  letter-spacing: -0.04em;
  color: var(--min-black);
}

/* Card — barely-there */
.min-card {
  background: var(--min-white);
  border: var(--min-border);
  border-radius: 12px;
  padding: var(--min-space-6);
  box-shadow: var(--min-shadow-xs);
  transition: box-shadow 0.2s ease, transform 0.2s ease;
}

.min-card:hover {
  box-shadow: var(--min-shadow-md);
  transform: translateY(-1px);
}

/* Divider */
.min-divider {
  height: 1px;
  background: var(--min-gray-100);
  margin: var(--min-space-6) 0;
}

/* Button — Primary */
.min-btn-primary {
  background: var(--min-black);
  color: var(--min-white);
  border: none;
  border-radius: 8px;
  padding: 12px 28px;
  font-size: var(--min-font-sm);
  font-weight: 500;
  letter-spacing: 0.01em;
  cursor: pointer;
  transition: opacity 0.15s ease, transform 0.15s ease;
}

.min-btn-primary:hover { opacity: 0.85; transform: translateY(-1px); }

/* Button — Ghost */
.min-btn-ghost {
  background: transparent;
  color: var(--min-black);
  border: var(--min-border);
  border-radius: 8px;
  padding: 11px 28px;
  font-size: var(--min-font-sm);
  font-weight: 500;
  cursor: pointer;
  transition: background 0.15s ease;
}

.min-btn-ghost:hover { background: var(--min-gray-100); }

/* Label / Caption */
.min-label {
  font-size: var(--min-font-xs);
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--min-gray-500);
}

/* Accent Highlight */
.min-accent-bar {
  display: inline-block;
  width: 32px;
  height: 3px;
  background: var(--min-accent);
  border-radius: 2px;
  margin-bottom: var(--min-space-2);
}

/* Spacious Section */
.min-section {
  padding: var(--min-space-16) 0;
}
Fonts Hierarchy
Code
Display  : Inter 700, -0.04em tracking, 1.05 leading
Heading  : Inter 600, -0.02em tracking
Body     : Inter 400, -0.01em tracking, 1.7 leading
Caption  : Inter 500, +0.08em tracking, uppercase
Mono     : JetBrains Mono, Geist Mono
💧 6. LIQUID GLASS
Filosofi
"Kaca yang hidup — bergerak, merefraksikan cahaya, seperti air yang membeku." Apple iOS 26 design language. Paling kompleks. Blur + distorsi + refraksi + motion.

Design Tokens
CSS
:root {
  /* Liquid Glass Core */
  --lg-blur: blur(32px) saturate(160%) brightness(108%);
  --lg-bg-light: rgba(255, 255, 255, 0.18);
  --lg-bg-dark: rgba(10, 10, 30, 0.35);
  --lg-border-light: 1px solid rgba(255, 255, 255, 0.35);
  --lg-border-dark: 1px solid rgba(255, 255, 255, 0.12);
  --lg-radius: 24px;

  /* Refraction Tint */
  --lg-tint-blue: rgba(100, 180, 255, 0.08);
  --lg-tint-purple: rgba(150, 100, 255, 0.08);
  --lg-tint-warm: rgba(255, 200, 150, 0.08);
}
Core Effects
CSS
/* Base Liquid Glass — Light Mode */
.liquid-glass-light {
  background: var(--lg-bg-light);
  backdrop-filter: var(--lg-blur);
  -webkit-backdrop-filter: var(--lg-blur);
  border: var(--lg-border-light);
  border-radius: var(--lg-radius);
  box-shadow:
    0 0 0 1px rgba(255,255,255,0.12) inset,
    0 2px 0 rgba(255,255,255,0.25) inset,  /* top specular highlight */
    0 -1px 0 rgba(0,0,0,0.08) inset,       /* bottom edge darkening */
    0 12px 40px rgba(0,0,0,0.12),
    0 1px 1px rgba(255,255,255,0.9);
}

/* Base Liquid Glass — Dark Mode */
.liquid-glass-dark {
  background: var(--lg-bg-dark);
  backdrop-filter: var(--lg-blur);
  -webkit-backdrop-filter: var(--lg-blur);
  border: var(--lg-border-dark);
  border-radius: var(--lg-radius);
  box-shadow:
    0 0 0 1px rgba(255,255,255,0.08) inset,
    0 2px 0 rgba(255,255,255,0.1) inset,
    0 -1px 0 rgba(0,0,0,0.2) inset,
    0 20px 60px rgba(0,0,0,0.5);
}

/* SVG Liquid Distortion Filter */
.liquid-glass-distort {
  filter: url(#liquidDistort);
}
/* Apply this SVG to your HTML: */
/*
<svg style="display:none">
  <filter id="liquidDistort">
    <feTurbulence
      type="turbulence"
      baseFrequency="0.015 0.015"
      numOctaves="3"
      seed="2"
      result="turb"
    />
    <feDisplacementMap
      in2="turb"
      in="SourceGraphic"
      scale="8"
      xChannelSelector="R"
      yChannelSelector="G"
    />
  </filter>
</svg>
*/

/* Animated Liquid Turbulence (animasi filter) */
.liquid-glass-live {
  position: relative;
  backdrop-filter: blur(24px) saturate(180%);
  background: rgba(255,255,255,0.1);
  border: 1px solid rgba(255,255,255,0.25);
  border-radius: 24px;
  overflow: hidden;
}

/* Refraction shimmer overlay */
.liquid-glass-live::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: linear-gradient(
    135deg,
    rgba(255,255,255,0.2) 0%,
    rgba(255,255,255,0.0) 40%,
    rgba(100,180,255,0.1) 70%,
    rgba(255,255,255,0.1) 100%
  );
  animation: liquidShimmer 4s ease-in-out infinite;
  pointer-events: none;
}

@keyframes liquidShimmer {
  0%   { opacity: 0.4; transform: translateX(-10%) rotate(0deg); }
  50%  { opacity: 0.8; transform: translateX(10%) rotate(1deg); }
  100% { opacity: 0.4; transform: translateX(-10%) rotate(0deg); }
}

/* Liquid Pill (Apple-style tab/button) */
.liquid-pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  border-radius: 100px;
  background: rgba(255,255,255,0.15);
  backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid rgba(255,255,255,0.3);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.4),
    inset 0 -1px 0 rgba(0,0,0,0.1),
    0 4px 16px rgba(0,0,0,0.12);
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
}

.liquid-pill:hover {
  background: rgba(255,255,255,0.25);
  transform: scale(1.02);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.5),
    0 8px 24px rgba(0,0,0,0.15);
}

/* Liquid Dock (Apple dock-style) */
.liquid-dock {
  display: flex;
  align-items: flex-end;
  gap: 8px;
  padding: 12px 16px;
  background: rgba(255,255,255,0.12);
  backdrop-filter: blur(40px) saturate(180%) brightness(110%);
  border: 1px solid rgba(255,255,255,0.2);
  border-radius: 24px;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.25),
    0 20px 60px rgba(0,0,0,0.3),
    0 1px 0 rgba(255,255,255,0.5);
}

/* Magnification effect (JavaScript diperlukan untuk dock magnify) */
.liquid-dock-item {
  width: 52px; height: 52px;
  border-radius: 14px;
  transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.liquid-dock-item:hover {
  transform: scale(1.4) translateY(-8px);
}
⚡ REACT UNIVERSAL STYLE SWITCHER
StyleProvider.tsx
"use client"

import { createContext, useContext, useState } from "react"
import { cn } from "@/lib/utils"

type DesignStyle =
🎛️ MASTER COMBO TABLE
Project Type	Primary Style	Accent Style	Avoid
SaaS Dark Dashboard	Glass	Liquid Glass	Skeuomorphic
iOS / Mobile App	Liquid Glass	Minimal	Brutalist
Startup Landing	Brutalist	Minimal	Skeuomorphic
Kids / Game App	Clay	Glass (subtle)	Brutalist
Music / Audio App	Skeuomorphic	Minimal	Clay
Corporate / Finance	Minimal	Glass (subtle)	Brutalist / Clay
Portfolio Dev	Brutalist OR Minimal	Glass accent	—
Luxury Brand	Minimal	Skeuomorphic detail	Clay / Brutalist
Semua style di-manage via [[DeepLake]] RAG Dioptimalkan untuk [[Qwen 3 Coder 480B Turbo]] di Venice Tools: [[Framer Motion]] [[21st dev]] [[Figma]] [[Penpot]] [[ui ux promax]]

Code

---

## Rangkuman 6 Aliran Desain yang Dikuasai:

| # | Style | Ciri Khas | Token Utama |
|---|-------|-----------|-------------|
| 🪟 | **Glassmorphism** | Transparan, blur, cahaya tembus | `backdrop-filter`, `rgba`, border glass |
| 🪵 | **Skeuomorphism** | Realistis, material fisik, tekstur | Multi-layer `box-shadow`, noise texture, gradient bevel |
| 💥 | **Neo Brutalism** | Raw, bold border, offset shadow | Hard `box-shadow` tanpa blur, border tebal, zero radius |
| 🫧 | **Claymorphism** | Puffy, 3D, squishy, playful | Dual `inset` + `outer shadow`, pastel gradient, big radius |
| ◻️ | **Minimalism** | Whitespace, tipografi, subtle shadow | 8px grid, 1 accent, barely-there border |
| 💧 | **Liquid Glass** | Apple-esque, refraksi, shimmer | SVG `feTurbulence`, specular inset, animated shimmer |

Bonus: **Universal React Card** yang bisa switch style cukup ganti satu prop `style="clay"` → langsung berubah tampilan 🚀