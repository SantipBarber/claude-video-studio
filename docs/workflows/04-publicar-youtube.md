# Workflow 4 — Publicar en YouTube

Herramienta sugerida: [mrchevyceleb/youtube-mcp](https://github.com/mrchevyceleb/youtube-mcp) (MIT, YouTube Data API v3). Tiene pocos usuarios: **revisar el código antes de darle acceso al canal.** Alternativa gestionada: el toolkit de YouTube de Composio.

## Configuración (una vez)

1. En Google Cloud Console: crear proyecto → activar **YouTube Data API v3** → crear credenciales OAuth (app de escritorio).
2. Instalar el MCP siguiendo su README y registrarlo en Claude Code (`claude mcp add ...`).
3. Autenticar con la cuenta del canal.

## Uso

- `upload_video`: subida reanudable. **Siempre como privado o no listado** hasta revisar.
- `update_video`: título, descripción, tags.
- `set_thumbnail`: miniatura.

## Checklist antes de publicar

- [ ] Título y descripción revisados (`videos/<carpeta>/publicacion.md`)
- [ ] Miniatura final
- [ ] Subtítulos subidos o quemados
- [ ] Capítulos (timestamps) en la descripción
- [ ] Confirmación explícita de Santi para pasar a público
