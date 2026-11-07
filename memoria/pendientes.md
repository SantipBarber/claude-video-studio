# Pendientes

## Haividio

- [ ] Documentar cómo instalarlo y usarlo en Codex, pi y Cursor, y probarlo: hoy solo se ha probado con Claude Code.
- [ ] Enlazar `haividio.dev` cuando esté activo y subir la imagen como vista previa social en los ajustes de GitHub.

## Ahora (en el Mac)

- [x] Clonar el repo e instalar el plugin `video-studio` (+ hyperframes, Chrome Headless Shell, whisper-cpp, Parakeet) (ver "Empezar en tu Mac" en el README).
- [ ] Probar el flujo **pencil.dev → HyperFrames**: diseñar 1–2 fotogramas clave de una escena en Pencil, que Claude Code los lea por MCP y los anime. Comprobar qué exporta Pencil (HTML/CSS, imágenes, tokens) y documentarlo en `docs/workflows/06-pencil-a-hyperframes.md`.
- [x] (01-11, clonación instantánea; ver `docs/voz-clonada.md`.) **Clonar la voz** en ElevenLabs: grabar audio limpio, crear la voz, comprobar requisitos actuales (clonación rápida vs profesional, plan necesario). Guardar el ID de la voz en `.env`, nunca en git.
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
- [x] Música (estilo A «pulso tech», ElevenLabs Music, encadenada a 6:13) y 30 efectos (whoosh, pop, tic, golpe final), colocados desde `build_root.py`. Render v2 normalizado a −14 LUFS: `out/rag-video-v2.mp4`. Santi (01-11): «está perfecto para ser el primero»; la voz suena algo artificial.
- [x] Enviar la v2 para recoger opiniones (Google Drive, `Vídeos IA/RAG en 2026 - v2 (borrador para opiniones).mp4`). 03-11: **ha gustado bastante**. Siguiente paso: ajuste final (voz más natural, transiciones, ritmo de agentic y longcontext, `first_frame_empty`) y miniatura.
- [ ] Crear un client_id propio de Google Cloud para rclone (el compartido se retira en 2026) y aprovechar el proyecto para la API de YouTube.
- [ ] Ajustes conocidos: con la voz de Santi, 5 textos (ya resueltos con pausas de 1,2 s en search y topk) se ven poco tiempo (`line_unread` en search, topk y failures) porque las escenas «Buscar» (5,4 s) y «¿Cuántos?» (6,9 s) se han quedado cortas; «6 o más llamadas» (8b) no tiene fuente; música y efectos (sin créditos de ElevenLabs este mes); transiciones entre escenas (ahora cortes secos).
- [x] **Voz de Santi** (01-11): prueba A/B de la escena 1 entre ElevenLabs IVC (Starter), Qwen3-TTS 0.6B y Qwen3-TTS 1.7B, todas a la misma velocidad. Santi y Nerea eligieron **ElevenLabs**: entonación más natural y mejor manejo de pausas y silencios. Las 14 escenas ya están generadas con su voz (`ELEVENLABS_VOICE_ID_SANTI` en `.env`). El vídeo pasa de 7:58 a **6:11** y el gancho dice ahora «en seis minutos».
- [ ] Qwen3-TTS 1.7B: le vale la pena si llega a la calidad de ElevenLabs. Ideas para mejorarlo: generar párrafos (≤ 200 caracteres) en lugar de frases sueltas con pausas fijas, recortar los silencios de cada trozo y variar la pausa según la puntuación, y probar otra referencia. Ocupa 3,1 GB en la caché de HF (`models--mlx-community--Qwen3-TTS-12Hz-1.7B-Base-8bit`): borrarlo si se descarta.
- [ ] **Ritmo para que no canse** (Santi, 01-11: prioridad justo después de la voz): revisar escenas largas (8 agentic 52 s, 9 longcontext 42 s), meter cambios de plano y alguna pausa o pregunta al espectador.
- [ ] Afinar la escena 3: ritmo ajustado a la voz real, sonido (música de fondo + efecto en cada paso).
- [ ] Sustituir los puntos inventados por **embeddings reales** (sentence-transformers + dataset de Hugging Face, proyección UMAP/PCA).
- [x] Generar la voz por escenas con la voz clonada (01-11).
- [x] Animar el resto de escenas (`animaciones/rag-video/`, 18 composiciones).
- [ ] Miniatura y publicación como privado.

## Windows (03-11)

- [x] Adaptar el repo: `docs/windows.md` (winget, diferencias de comandos, herramientas solo de macOS), sección «Empezar en Windows» en el README, `encoding="utf-8"` en `build_root.py` (en el Mac genera el mismo `index.html`) y `.gitattributes` con `eol=lf`.
- [ ] **Probarlo en un Windows real** (Santi o alguien de su empresa): la lista de comprobación está en `docs/windows.md`. HyperFrames dice soportar Windows desde la v0.8.219, pero no lo hemos probado. Si falla el render nativo, usar WSL2. Para `rag-video` hay que pasar aparte los mp3 de `assets/`, que no están en git.

## Ideas

- **Biblioteca de vídeos de ingeniería de IA para la empresa de Santi** (01-11): `docs/biblioteca-ingenieria-ia.md`. Late chunking, para aplicarlo en sus proyectos: `videos/2026-10-31-rag-2026/aplicar-en-proyectos.md`.

- Crear una pequeña librería de componentes reutilizables (barra de pasos, tarjeta de fragmento, panel de dispersión, caja LLM) para no rehacerlos en cada vídeo.
- Workflow `05-pencil-a-hyperframes.md` y añadir la clonación de voz a la skill `video-sin-cara`.
