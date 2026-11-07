---
name: publicar-youtube
description: Prepara y sube un vídeo a YouTube - título, descripción con capítulos, tags, miniatura y subida como privado u oculto con la CLI youtubeuploader (YouTube Data API v3). Úsala cuando un vídeo esté terminado o el usuario pida publicar.
---

# Publicar en YouTube

## Preparar (`publicacion.md`)

- **Título:** ≤ 60 caracteres, promesa clara, sin clickbait engañoso. Propón 3 opciones.
- **Descripción:** 2 líneas de gancho, resumen, capítulos (`00:00 Intro`…) sacados del guion o la transcripción, fuentes y enlaces.
- **Tags:** 5–10 relevantes.
- **Miniatura:** 1280×720, máximo 4 palabras, con la identidad visual del canal (skill `identidad-visual`).

## Subir

1. Comprueba que `youtubeuploader -version` funciona y que existen las credenciales fuera del repositorio (`~/.config/youtubeuploader/`). Si no, guía la configuración con `docs/workflows/04-publicar-youtube.md`.
2. Prepara `publicacion.json` (título, descripción con capítulos, etiquetas, idioma) a partir de `publicacion.md`.
3. **Pide confirmación explícita** antes de subir.
4. Sube con `-privacy private` (o `unlisted` si lo pide), con `-thumbnail` y `-caption` si los hay. Nunca público directamente.
5. Devuelve el enlace y pide al usuario que lo revise en YouTube Studio: que compruebe la visibilidad (un proyecto sin auditar puede dejarlo privado y bloqueado) y que declare el contenido sintético si hay voz clonada.

## Al terminar

Anota el enlace y la fecha en el `README.md` del vídeo y en el índice `videos/README.md`.
