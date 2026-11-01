# Aprendizajes

Lo más reciente arriba. Formato: `- AAAA-MM-DD · [tema] lo aprendido. Cómo aplicarlo.`

## HyperFrames

- 2026-10-31 · [render] HyperFrames renderiza con **Chrome Headless Shell** (familia Chrome for Testing), no con Chrome normal ni Brave. `npx hyperframes browser ensure` lo descarga en `~/.cache/hyperframes/chrome/`. `npx hyperframes doctor` revisa todas las dependencias. Sustituye el truco del Chromium de Playwright.
- 2026-10-31 · [transcripción] HyperFrames usa whisper-cpp (`brew install whisper-cpp`) para `hyperframes transcribe`; para español pasar `-l es -m large-v3` (los modelos `.en` son solo inglés). Alternativa más rápida: `hyperframes models install parakeet`.
- 2026-10-31 · [render] Si no hay Chrome instalado, `render` falla. Apuntar al Chromium de Playwright: `HYPERFRAMES_BROWSER_PATH=$(node -e "console.log(require('playwright').chromium.executablePath())")`. En el Mac con Chrome instalado no hace falta.
- 2026-10-31 · [render] 26 s a 1080p30 tardan ~1 min con captura por software. Para iterar, usar `npx hyperframes snapshot --at 1,5,10` y revisar el `contact-sheet.jpg` antes de renderizar.
- 2026-10-31 · [lint] No animar `left`/`top` con GSAP (error `gsap_non_transform_motion`, da tirones). Usar `x`/`y`.
- 2026-10-31 · [lint] No mezclar `transform` en CSS con tweens de `x`/`y` (error `gsap_css_transform_conflict`). Para centrar, `gsap.set(el, { xPercent: -50 })`.
- 2026-10-31 · [lint] Los estados iniciales ocultos van con `gsap.set(...)` fuera del timeline, no con `tl.set(..., 0)`, o el fotograma 0 sale mal.
- 2026-10-31 · [legibilidad] El check exige texto ≥ 28 px en 1080p (legible en móvil). Diseñar con ese mínimo desde el principio.
- 2026-10-31 · [assets] La plantilla carga GSAP y fuentes de CDN. En entornos sin red, copiarlos a `assets/` (gsap desde npm, fuentes desde `@fontsource/*`) y referenciarlos en local. Así además el render es reproducible.
- 2026-10-31 · [flujo] `npx hyperframes init <nombre> --example=blank --non-interactive` → editar `index.html` → `check` → `snapshot` → `render -o salida.mp4`.

- 2026-11-01 · [voz] Flujo voz → animación: `POST /v1/text-to-speech/{voice}/with-timestamps` devuelve el mp3 y el tiempo de cada carácter; agrupado en palabras (`audio/voice/scene-*.words.json`) da los instantes exactos para colocar cada animación. Sin alineación forzada aparte.
- 2026-11-01 · [preview] En **Safari** la vista previa de HyperFrames (`npx hyperframes preview`) no reproduce el audio; en Chrome sí. Abrir siempre la URL del Studio en Chrome.
- 2026-11-01 · [estructura] Un tramo = `index.html` raíz (fondo, barra de pasos, `<audio>` de voz, cada uno en su pista y con `data-duration` = duración real) + una subcomposición por escena en `compositions/`. Los ids deben ser únicos entre escenas (prefijo por escena). El check avisa de «dead_stretch» (>3 s sin cambios) y «line_unread» (texto que se va antes de poder leerse): útiles para ajustar el ritmo.

## ElevenLabs

- 2026-11-01 · [plan] El plan gratuito **no deja usar voces de la biblioteca (Voice Library) por API** (402 `paid_plan_required`): solo las de serie (inglesas/americanas, hablan español con algo de acento). Las castellanas nativas (Aaron Abad, David Martin, Eva Dorado, Carmelo) requieren Starter. 10.000 créditos/mes ≈ 10.000 caracteres.
- 2026-11-01 · [clave] Clave restringida «claude-video-studio»: TTS, STT, efectos, música, alineación forzada, modelos (acceso); voces (leído). Falta «Usuario» (`user_read`) para consultar créditos. Para clonar, voces → escribir.

## Pencil

- 2026-10-31 · [export] `Export(ids,"png",dir)` saca PNG por fotograma (nombre = id del nodo); `Export(ids,"html-css",fichero)` saca HTML con estilos inline, posiciones absolutas, `data-pencil-name` con el nombre de cada capa y fuentes de Google por CDN. Sirve de base para HyperFrames, pero hay que añadir ids, fuentes locales y copiar los assets (las URLs de imagen quedan relativas al .pen, no al HTML).
- 2026-10-31 · [diseño] Los puntos de un scatter se generan bien con JS dentro de `execute` (semilla determinista, la misma que luego usa la animación). No hay trazo discontinuo: el radio de búsqueda va como elipse con relleno lima al 6 % y borde al 40 %.
- 2026-10-31 · [diseño] La rejilla de puntos del fondo va como imagen (`design/assets/grid.png`, 1920×1080) en un fill de imagen; se reutiliza en HyperFrames.

- 2026-10-31 · [pencil] Los avisos `partially/fully clipped` que da `Get` en el mismo `execute` que crea los nodos suelen ser falsos (layout aún sin resolver). Recomprobar en otra llamada antes de corregir nada.
- 2026-10-31 · [pencil] Para la firma reutilizable (tarjeta de glosario) usar un componente `reusable: true` e instancias `ref` con `descendants` para cambiar término y definición.

## Claude Code / plugin

- 2026-10-31 · [plugin] `claude plugin marketplace add heygen-com/hyperframes` falla sin **git-lfs** (`brew install git-lfs && git lfs install`). Después queda un aviso de punteros LFS sin bajar: son vídeos de test del repo, no hace falta `lfs pull`. Plugin: `hyperframes@hyperframes`.
- 2026-10-31 · [pencil] El MCP de Pencil no crea ni abre ficheros: si `filePath` no existe, actúa sobre el `.pen` activo (¡riesgo de tocar otro proyecto!). Crear el fichero en la app (⌘N + guardar) y pasar siempre la ruta explícita. No abrir una segunda instancia de Pen: competirían por el MCP.
- 2026-10-31 · [plugin] Validar el marketplace con `claude plugin validate .` desde la raíz del repo antes de subir.
- 2026-10-31 · [github] Desde una sesión de Claude en la nube no se pueden crear repos; se crea vacío en GitHub y se da acceso a la app de Claude (github.com/apps/claude) para poder hacer push.

## Contenido

- 2026-10-31 · [fuentes] Las URLs de blogs de terceros cambian: smartscope.blog dejó de contener la cita sobre Claude Code y RAG. Para afirmaciones que abren un vídeo, buscar siempre la fuente primaria (post, transcripción) y guardarla.
- 2026-10-31 · [fuentes] Las cifras de recuperación contextual de Anthropic (−35 %, −49 % con BM25, −67 % con reranker; de 5,7 % a 1,9 % de fallos en top-20) están verificadas. Miden recuperación, no calidad final de respuesta: decirlo así en el vídeo.
- 2026-10-31 · [herramientas] Clonify no es un editor de vídeo (es una plataforma de formación online). Descartado.
