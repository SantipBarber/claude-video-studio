# Pendientes

## Ahora (en el Mac)

- [x] Clonar el repo e instalar el plugin `video-studio` (+ hyperframes, Chrome Headless Shell, whisper-cpp, Parakeet) (ver "Empezar en tu Mac" en el README).
- [ ] Probar el flujo **pencil.dev → HyperFrames**: diseñar 1–2 fotogramas clave de una escena en Pencil, que Claude Code los lea por MCP y los anime. Comprobar qué exporta Pencil (HTML/CSS, imágenes, tokens) y documentarlo en `docs/workflows/05-pencil-a-hyperframes.md`.
- [ ] **Clonar la voz** en ElevenLabs: grabar audio limpio, crear la voz, comprobar requisitos actuales (clonación rápida vs profesional, plan necesario). Guardar el ID de la voz en `.env`, nunca en git.
- [ ] Elegir entre whisper-cpp y Parakeet para transcribir y **desinstalar el que no se use** (Santi, 31-10: el espacio en disco está creciendo mucho; npm y Playwright ya se limpiaron).
- [ ] Vídeo de RAG: **más pantallas** en el pen, con el conocimiento de `fuentes.md` (Hugging Face, LangChain Deep Agents…) explicado para usuarios no tan avanzados (petición de Santi, 31-10).

## Tarea: pasar nombres a inglés (pedida el 2026-10-31)

- [ ] Renombrar **carpetas y ficheros** del repo de español a inglés (p. ej. `memoria/` → `memory/`, `docs/estilo/` → `docs/style/`, `docs/herramientas.md` → `docs/tools.md`, `videos/_plantilla/` → `videos/_template/`, `guion.md` → `script.md`, `fuentes.md` → `sources.md`, `animaciones/escena-03` → `animations/scene-03`, skills del plugin `identidad-visual` → `visual-identity`, etc.).
- [ ] El **código** pasa a inglés (ids, clases, variables, nombres de capas en Pencil, keys de JSON). Los **comentarios** pueden seguir en español.
- [ ] El **contenido** de los documentos y del vídeo sigue en español.
- [ ] Hacerlo con `git mv` (conserva historial) y actualizar todas las referencias: CLAUDE.md, README, skills del plugin, marketplace.json, enlaces entre docs y la memoria de Claude. Al final: `claude plugin validate .` y reinstalar el plugin `video-studio`.
- [ ] Buena candidata para delegar en pi (mecánica), con una lista de renombrados cerrada que apruebe Santi antes.

## Vídeo de RAG (`videos/2026-10-31-rag-2026/`)

- [x] Guion v1 con fuentes.
- [x] Prueba de la escena 3 en HyperFrames (26 s, sin voz).
- [x] Guion v2: bloque de fundamentos para principiantes (escenas 2b, 3a–3c, 8 ampliada) con fuentes de HF, LangChain y Anthropic (`fuentes.md`).
- [x] Guion v2 aprobado; gancho A (sin dar por sabido qué es Claude Code).
- [ ] **Fuente primaria de la escena 1**: post de Boris Cherny en X o entrevista (mayo 2025) donde cuenta que quitaron RAG + base vectorial. La URL de smartscope de la v1 ya no lo dice. Sin fuente primaria, no publicar esa afirmación tal cual.
- [x] Fotogramas en `design/scene3.pen`: 2b, 3a, 3b Trocear, 3b Vectorizar, 03 Buscar, 3c ¿Cuántos?, 04 Generar (fila 1) y 8a, 8b (fila 2). Componente reutilizable «Glosario». PNG en `design/export/`.
- [x] Revisión de Santi de los fotogramas (01-11: «bastante bien» como prueba de concepto).
- [x] Tramo de prueba 3b + 3c animado con voz en `animaciones/rag-steps/` (74 s, 5 escenas como subcomposiciones, voz de serie «Daniel» de ElevenLabs sincronizada por palabra). Pendiente: que Santi lo vea en la vista previa y apruebe antes de renderizar.
- [x] **Vídeo completo montado** en `animaciones/rag-video/` (18 composiciones, 7:58, voz de prueba «Daniel»). `build_root.py` regenera `index.html` y `timeline.json` desde las duraciones reales de la voz. Borrador renderizado en `out/rag-video-draft-v1.mp4` (fuera de git). Santi: «como POC está guay», mejorable en el ajuste final.
- [ ] Ajustes conocidos: el gancho dice «en diez minutos» y la barra del hook llega a 10:00, pero dura ~8 min; «6 o más llamadas» (8b) no tiene fuente; música y efectos (sin créditos de ElevenLabs este mes); transiciones entre escenas (ahora cortes secos).
- [ ] **Voz de Santi** (decidido 01-11): prueba A/B con la misma escena entre (a) ElevenLabs IVC (Starter, oferta de 1 $ el primer mes) y (b) Qwen3-TTS en local, el mismo modelo que usa TranslateCall (`mlx-community/Qwen3-TTS-12Hz-0.6B-Base-8bit` vía mlx-audio). Qwen no da tiempos por palabra: alinear con whisper-cpp/Parakeet o con la API de forced alignment de ElevenLabs. Explorar también qué más ofrece ElevenLabs que sirva a TranslateCall. Las pruebas locales con Qwen usan GPU: avisar antes a la sesión de translatecall.
- [ ] **Ritmo para que no canse** (Santi, 01-11: prioridad justo después de la voz): revisar escenas largas (8 agentic 52 s, 9 longcontext 42 s), meter cambios de plano y alguna pausa o pregunta al espectador.
- [ ] Afinar la escena 3: ritmo ajustado a la voz real, sonido (música de fondo + efecto en cada paso).
- [ ] Sustituir los puntos inventados por **embeddings reales** (sentence-transformers + dataset de Hugging Face, proyección UMAP/PCA).
- [ ] Generar la voz por escenas con la voz clonada.
- [ ] Animar el resto de escenas (1–2 y 4–11).
- [ ] Miniatura y publicación como privado.

## Ideas

- **Biblioteca de vídeos de ingeniería de IA para la empresa de Santi** (01-11): `docs/biblioteca-ingenieria-ia.md`. Late chunking, para aplicarlo en sus proyectos: `videos/2026-10-31-rag-2026/aplicar-en-proyectos.md`.

- Crear una pequeña librería de componentes reutilizables (barra de pasos, tarjeta de fragmento, panel de dispersión, caja LLM) para no rehacerlos en cada vídeo.
- Workflow `05-pencil-a-hyperframes.md` y añadir la clonación de voz a la skill `video-sin-cara`.
