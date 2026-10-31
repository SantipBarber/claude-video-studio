---
name: video-hablado
description: Edita vídeos con alguien hablando a cámara o en voz (talking-head, tutoriales, entrevistas) con video-use - quitar silencios, errores, muletillas y repeticiones, corregir color, subtítulos y animaciones sincronizadas con lo que se dice.
---

# Vídeo hablado con video-use

## Comprobar requisitos

```bash
which ffmpeg && ls ~/.claude/skills/video-use && grep -q ELEVENLABS_API_KEY ~/tools/video-use/.env && echo OK
```

Si falta algo, instálalo (ver skill `elegir-herramienta-video`) y pide al usuario la clave de ElevenLabs. Nunca la escribas en el repo.

## Flujo

1. **Inventario.** Lista las tomas de la carpeta, su duración y de qué tratan (tras transcribir).
2. **Propón una estrategia** y espera aprobación: duración objetivo, qué se elimina, orden, estilo de subtítulos, look de color, animaciones previstas.
3. **Edita con video-use.** Corta por palabras y silencios; con tomas repetidas, quédate con la más fluida.
4. **Animaciones (opcional).** Ánclalas a frases concretas de la transcripción: "cuando dice X, aparece Y". Genera cada una con HyperFrames o Remotion aplicando la skill `identidad-visual`.
5. **Autorrevisión.** Revisa cada corte (saltos de imagen, chasquidos, subtítulos que tapan) antes de enseñar el resultado.
6. **Entrega** `edit/final.mp4` y resume qué se cortó y por qué.

## Peticiones típicas

- "Quita las pausas de más de 0,7 s pero deja respirar las frases importantes."
- "Subtítulos de 3 palabras, abajo, sin mayúsculas."
- "Cuando digo 'base de datos vectorial', pon el diagrama de embeddings 4 segundos."

## Al terminar

Guarda en la carpeta del vídeo del repo: `subtitulos.srt`, el código de las animaciones y notas de decisiones. Nada de MP4 ni WAV en git.
