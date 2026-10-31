---
name: elegir-herramienta-video
description: Decide qué herramienta usar para un vídeo (editar tomas, añadir animaciones, vídeo sin cara, shorts, publicar en YouTube) y explica cómo usarla. Úsala al empezar cualquier vídeo o cuando el usuario pregunte "¿con qué hago esto?".
---

# Elegir la herramienta de vídeo

Antes de recomendar, haz como mucho dos preguntas si no está claro:
1. ¿Hay grabación propia (cámara o voz) o el vídeo parte de cero?
2. ¿Necesita revisión visual en un timeline o basta con el resultado final?

## Árbol de decisión

```
¿Hay metraje grabado con alguien hablando?
├─ Sí → ¿Solo limpiar (silencios, errores, muletillas, subtítulos)?
│       ├─ Sí → video-use                         → skill video-hablado
│       └─ No, también animaciones encima
│              → video-use + HyperFrames/Remotion → skill video-hablado (sección animaciones)
│       ¿Quiere retocar a mano en un timeline?
│              → añadir Palmier Pro (macOS 26 + Apple Silicon) o Velorn
│
└─ No → ¿Explicativo/diagramas/motion graphics/short?
        → HyperFrames (por defecto) o Remotion + voz ElevenLabs → skill video-sin-cara
        ¿La voz la graba el usuario? → limpiarla antes con video-use

Siempre al final → skill publicar-youtube
Siempre que haya animaciones → skill identidad-visual
```

## HyperFrames vs Remotion

| Elige | Cuando |
|---|---|
| **HyperFrames** | Diagramas, tipografía animada, escenas tipo explicador. Se escribe en HTML/CSS, itera rápido, preview en vivo. Apache 2.0. |
| **Remotion** | Animaciones muy programáticas, gráficos de datos, plantillas reutilizables en React. Gratis para individuos y equipos de ≤3. |

## Alternativas según restricción

| Restricción | Opción |
|---|---|
| Coste cero, sin APIs | auto-editor + Whisper local (o videocut-skills) en lugar de video-use |
| Ya usa Final Cut | fcp-mcp-server (rough cut por FCPXML) |
| Ya usa Premiere | premiere-pro-mcp (experimental) |
| Ya usa DaVinci | davinci-resolve-mcp (requiere Resolve **Studio**) |
| Quiere todo en la nube | Descript MCP, OpusClip MCP o invideo MCP (de pago) |

## Instalación rápida

```bash
# Edición de tomas
brew install ffmpeg
git clone https://github.com/browser-use/video-use ~/tools/video-use
ln -s ~/tools/video-use ~/.claude/skills/video-use   # + ELEVENLABS_API_KEY en .env

# Animación
claude plugin marketplace add heygen-com/hyperframes   # Node 22+ y FFmpeg
npx skills add remotion-dev/skills

# Editor con MCP (con la app abierta)
claude mcp add --transport http palmier-pro http://127.0.0.1:19789/mcp
```

## Reglas

- Comprueba en la web precios y requisitos si la información tiene más de unos meses: este ecosistema cambia cada mes.
- Recomienda una sola opción principal y como mucho una alternativa; no listes todo el catálogo.
- Si el trabajo está en el repo `claude-video-studio`, el detalle de cada herramienta está en `docs/herramientas.md` y los flujos en `docs/workflows/`.
