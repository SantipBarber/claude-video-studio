# Aprendizajes

Lo más reciente arriba. Formato: `- AAAA-MM-DD · [tema] lo aprendido. Cómo aplicarlo.`

## HyperFrames

- 2026-10-31 · [render] Si no hay Chrome instalado, `render` falla. Apuntar al Chromium de Playwright: `HYPERFRAMES_BROWSER_PATH=$(node -e "console.log(require('playwright').chromium.executablePath())")`. En el Mac con Chrome instalado no hace falta.
- 2026-10-31 · [render] 26 s a 1080p30 tardan ~1 min con captura por software. Para iterar, usar `npx hyperframes snapshot --at 1,5,10` y revisar el `contact-sheet.jpg` antes de renderizar.
- 2026-10-31 · [lint] No animar `left`/`top` con GSAP (error `gsap_non_transform_motion`, da tirones). Usar `x`/`y`.
- 2026-10-31 · [lint] No mezclar `transform` en CSS con tweens de `x`/`y` (error `gsap_css_transform_conflict`). Para centrar, `gsap.set(el, { xPercent: -50 })`.
- 2026-10-31 · [lint] Los estados iniciales ocultos van con `gsap.set(...)` fuera del timeline, no con `tl.set(..., 0)`, o el fotograma 0 sale mal.
- 2026-10-31 · [legibilidad] El check exige texto ≥ 28 px en 1080p (legible en móvil). Diseñar con ese mínimo desde el principio.
- 2026-10-31 · [assets] La plantilla carga GSAP y fuentes de CDN. En entornos sin red, copiarlos a `assets/` (gsap desde npm, fuentes desde `@fontsource/*`) y referenciarlos en local. Así además el render es reproducible.
- 2026-10-31 · [flujo] `npx hyperframes init <nombre> --example=blank --non-interactive` → editar `index.html` → `check` → `snapshot` → `render -o salida.mp4`.

## Claude Code / plugin

- 2026-10-31 · [plugin] Validar el marketplace con `claude plugin validate .` desde la raíz del repo antes de subir.
- 2026-10-31 · [github] Desde una sesión de Claude en la nube no se pueden crear repos; se crea vacío en GitHub y se da acceso a la app de Claude (github.com/apps/claude) para poder hacer push.

## Contenido

- 2026-10-31 · [fuentes] Las cifras de recuperación contextual de Anthropic (−35 %, −49 % con BM25, −67 % con reranker; de 5,7 % a 1,9 % de fallos en top-20) están verificadas. Miden recuperación, no calidad final de respuesta: decirlo así en el vídeo.
- 2026-10-31 · [herramientas] Clonify no es un editor de vídeo (es una plataforma de formación online). Descartado.
