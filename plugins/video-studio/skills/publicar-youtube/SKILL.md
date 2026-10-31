---
name: publicar-youtube
description: Prepara y sube un vídeo a YouTube - título, descripción con capítulos, tags, miniatura y subida como privado mediante un MCP de YouTube (Data API v3). Úsala cuando un vídeo esté terminado o el usuario pida publicar.
---

# Publicar en YouTube

## Preparar (`publicacion.md`)

- **Título:** ≤ 60 caracteres, promesa clara, sin clickbait engañoso. Propón 3 opciones.
- **Descripción:** 2 líneas de gancho, resumen, capítulos (`00:00 Intro`…) sacados del guion o la transcripción, fuentes y enlaces.
- **Tags:** 5–10 relevantes.
- **Miniatura:** 1280×720, máximo 4 palabras, con la identidad visual del canal (skill `identidad-visual`).

## Subir

1. Comprueba que hay un MCP de YouTube conectado (`claude mcp list`). Si no, sugiere `mrchevyceleb/youtube-mcp` o el toolkit de Composio y avisa de revisar el código antes de dar acceso al canal.
2. **Pide confirmación explícita** antes de subir.
3. Sube con `privacyStatus: private` (o `unlisted` si lo pide). Nunca público directamente.
4. Aplica título, descripción, tags y miniatura.
5. Devuelve el enlace y pide al usuario que lo revise en YouTube Studio antes de hacerlo público.

## Al terminar

Anota el enlace y la fecha en el `README.md` del vídeo y en el índice `videos/README.md`.
