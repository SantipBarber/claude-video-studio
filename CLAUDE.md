# Instrucciones para Claude

Este repositorio es la base de conocimiento y el espacio de trabajo de Santi para producir vídeos de YouTube con Claude Code. Idioma de trabajo: español.

## Antes de empezar cualquier vídeo

1. Lee `README.md` (tabla de herramientas) y `docs/herramientas.md`.
2. Identifica el caso de uso y lee el workflow correspondiente en `docs/workflows/`.
3. Revisa `videos/README.md` por si hay vídeos anteriores relacionados (reutiliza estilo, escenas, guiones).
4. Si hay animaciones o miniatura, aplica `docs/estilo/identidad.md` (skill `identidad-visual` del plugin `plugins/video-studio`).
5. Crea la carpeta del vídeo copiando `videos/_plantilla/` → `videos/AAAA-MM-DD-slug/`.

## Reglas

- Propón el plan (guion, estructura, herramientas) y espera aprobación antes de renderizar o cortar.
- Nunca subas a YouTube sin confirmación explícita. Sube siempre como **privado** o **no listado** salvo que se pida lo contrario.
- No subas al repo archivos de vídeo/audio pesados (raw, renders). Solo guiones, código de animaciones, subtítulos (.srt), miniaturas finales y notas.
- Las claves (ElevenLabs, Google OAuth) van en `.env`, nunca en git.
- Las herramientas evolucionan rápido: si algo de `docs/herramientas.md` tiene más de unos meses, verifica en la web antes de dar por bueno un precio, requisito o comando.

## Al terminar un vídeo

- Completa `videos/<carpeta>/README.md`: resumen, guion final, herramientas usadas, decisiones, problemas, enlace de YouTube.
- Añade una línea al índice `videos/README.md`.
- Si aprendiste algo útil sobre una herramienta (un fallo, un truco, un cambio de precio), actualízalo en `docs/`.
