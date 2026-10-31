# Claude Video Studio

Base de conocimiento y espacio de trabajo para crear vídeos de YouTube con Claude Code: edición, animaciones, vídeos sin cara y publicación.

La idea: abrir Claude Code (o un proyecto de Claude) sobre este repositorio y usarlo como fuente de verdad. Aquí vive la investigación sobre herramientas, los flujos de trabajo de cada caso de uso y el histórico de cada vídeo que hagamos (guion, resumen, decisiones, enlace publicado).

## Qué herramienta para cada caso

| Caso de uso | Herramienta principal | Complementos | Coste extra |
|---|---|---|---|
| Vídeo hablado: quitar silencios, errores y muletillas | [video-use](https://github.com/browser-use/video-use) | Palmier Pro / Velorn para retoque visual | ElevenLabs (transcripción) |
| Animaciones y efectos mientras explicas | video-use + HyperFrames o Remotion | — | ElevenLabs |
| Vídeo sin cara (explicativo animado + voz en off) | [HyperFrames](https://github.com/heygen-com/hyperframes) o [Remotion](https://www.remotion.dev/docs/ai/skills) | ElevenLabs TTS para la voz | ElevenLabs |
| Publicar en YouTube | MCP de YouTube (Data API v3) | — | Gratis (cuota de API de Google) |

Todo funciona con la suscripción de Claude; lo único que se paga aparte es ElevenLabs.

## Plugin `video-studio` para Claude Code

El repo es también un marketplace de plugins. Instálalo una vez y las skills estarán disponibles en cualquier proyecto:

```bash
claude plugin marketplace add SantipBarber/claude-video-studio
claude plugin install video-studio@claude-video-studio
```

| Skill | Para qué |
|---|---|
| `elegir-herramienta-video` | Decide qué herramienta usar según el tipo de vídeo y cómo instalarla |
| `video-hablado` | Edita tomas con video-use: cortes, subtítulos, animaciones sincronizadas |
| `video-sin-cara` | Investigación → guion por escenas → voz → animación → render |
| `identidad-visual` | Aplica la identidad del canal y evita la estética típica de vídeo hecho con IA |
| `publicar-youtube` | Título, descripción, capítulos, miniatura y subida como privado |

## Estructura

```
CLAUDE.md                    Instrucciones para Claude al trabajar en este repo
.claude-plugin/              Marketplace de plugins
plugins/video-studio/        Plugin con las skills
docs/
  estilo/identidad.md        Identidad visual del canal (paleta, tipografía, movimiento)
  herramientas.md            Catálogo de herramientas investigadas (oct 2026)
  clonify.md                 Por qué Clonify no sirve para esto
  recursos-abiertos.md       Hugging Face, documentación, iconos, fuentes, audio (con licencias)
  workflows/
    01-video-hablado.md      Cortar tomas con video-use
    02-animaciones.md        Añadir animaciones sobre tu explicación
    03-video-sin-cara.md     Vídeo explicativo animado con voz en off
    04-publicar-youtube.md   Subida, título, descripción, miniatura
videos/
  README.md                  Índice de vídeos
  _plantilla/                Copiar para cada vídeo nuevo
```

## Cómo empezar un vídeo nuevo

1. Copia `videos/_plantilla/` a `videos/AAAA-MM-DD-slug/`.
2. Abre Claude Code en la raíz del repo y dile qué vídeo quieres. Claude leerá `CLAUDE.md` y el workflow correspondiente.
3. Al terminar, Claude actualiza el `README.md` del vídeo y el índice `videos/README.md`.

> Los archivos de vídeo pesados (raw, renders) **no se suben** al repo; ver `.gitignore`.
