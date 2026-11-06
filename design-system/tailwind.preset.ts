// Grupo Olivo — preset de Tailwind conectado a design-system/project/tokens.css.
// Uso: importa tokens.css en app/globals.css y añade este preset en tailwind.config.ts ({ presets: [goPreset] }).
// Los valores viven en tokens.css; aquí solo se nombran, así un cambio de token se refleja sin tocar Tailwind.
import type { Config } from "tailwindcss";

const v = (name: string) => `var(--${name})`;

const goPreset: Partial<Config> = {
  darkMode: ["selector", '[data-theme="dark"]'],
  theme: {
    extend: {
      colors: {
        brand: { black: v("brand-black"), green: v("brand-green"), leaf: v("brand-leaf") },
        surface: { DEFAULT: v("surface"), sunk: v("surface-sunk"), raised: v("surface-raised") },
        ink: { DEFAULT: v("ink"), muted: v("ink-muted") },
        "on-ink": v("on-ink"),
        accent: { DEFAULT: v("accent"), soft: v("accent-soft") },
        "on-accent": v("on-accent"),
        rule: v("rule"),
        "control-border": v("control-border"),
        focus: v("focus"),
        success: v("success"),
        warning: { DEFAULT: v("warning"), soft: v("warning-soft") },
        danger: { DEFAULT: v("danger"), soft: v("danger-soft") },
        overlay: v("overlay"),
      },
      fontFamily: {
        display: [v("font-display")],
        serif: [v("font-serif")],
        sans: [v("font-sans")],
        mono: [v("font-mono")],
      },
      fontSize: {
        "display-xl": ["clamp(48px, 7.4vw, 104px)", { lineHeight: "0.95", letterSpacing: "-0.02em" }],
        "display-l": ["clamp(36px, 4.6vw, 60px)", { lineHeight: "1", letterSpacing: "-0.015em" }],
        "display-m": ["38px", { lineHeight: "1.1", letterSpacing: "-0.01em" }],
        quote: ["clamp(26px, 3vw, 38px)", { lineHeight: "1.25" }],
        "book-title": ["21px", { lineHeight: "1.2" }],
        lede: ["18px", { lineHeight: "1.65" }],
        body: ["16px", { lineHeight: "1.6" }],
        "body-s": ["14.5px", { lineHeight: "1.5" }],
        label: ["11px", { lineHeight: "1.4", letterSpacing: "0.08em" }],
      },
      spacing: Object.fromEntries([1, 2, 3, 4, 5, 6, 7, 8, 9].map((n) => [`go-${n}`, v(`space-${n}`)])),
      borderRadius: { book: v("radius-book"), s: v("radius-s"), m: v("radius-m"), pill: v("radius-pill") },
      boxShadow: { book: v("shadow-book"), "book-card": v("shadow-book-card"), panel: v("shadow-panel") },
      transitionDuration: { fast: v("duration-fast"), base: v("duration-base"), slow: v("duration-slow"), hero: v("duration-hero") },
      transitionTimingFunction: { out: v("ease-out"), "in-out": v("ease-in-out"), in: v("ease-in") },
      maxWidth: { container: v("container"), measure: v("measure") },
      height: { header: v("header-height") },
    },
  },
};

export default goPreset;
