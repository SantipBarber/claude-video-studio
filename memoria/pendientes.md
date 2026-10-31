# Pendientes

## Ahora (en el Mac)

- [ ] Clonar el repo e instalar el plugin `video-studio` (ver "Empezar en tu Mac" en el README).
- [ ] Probar el flujo **pencil.dev → HyperFrames**: diseñar 1–2 fotogramas clave de una escena en Pencil, que Claude Code los lea por MCP y los anime. Comprobar qué exporta Pencil (HTML/CSS, imágenes, tokens) y documentarlo en `docs/workflows/05-pencil-a-hyperframes.md`.
- [ ] **Clonar la voz** en ElevenLabs: grabar audio limpio, crear la voz, comprobar requisitos actuales (clonación rápida vs profesional, plan necesario). Guardar el ID de la voz en `.env`, nunca en git.

## Vídeo de RAG (`videos/2026-10-31-rag-2026/`)

- [x] Guion v1 con fuentes.
- [x] Prueba de la escena 3 en HyperFrames (26 s, sin voz).
- [ ] Revisar y aprobar el guion.
- [ ] Afinar la escena 3: ritmo ajustado a la voz real, sonido (música de fondo + efecto en cada paso).
- [ ] Sustituir los puntos inventados por **embeddings reales** (sentence-transformers + dataset de Hugging Face, proyección UMAP/PCA).
- [ ] Generar la voz por escenas con la voz clonada.
- [ ] Animar el resto de escenas (1–2 y 4–11).
- [ ] Miniatura y publicación como privado.

## Ideas

- Crear una pequeña librería de componentes reutilizables (barra de pasos, tarjeta de fragmento, panel de dispersión, caja LLM) para no rehacerlos en cada vídeo.
- Workflow `05-pencil-a-hyperframes.md` y añadir la clonación de voz a la skill `video-sin-cara`.
