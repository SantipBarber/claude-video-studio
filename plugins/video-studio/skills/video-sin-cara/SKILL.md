---
name: video-sin-cara
description: Produce vídeos sin cara (explicativos animados, divulgación técnica, shorts) desde cero - investigación, guion por escenas, voz en off, animaciones con HyperFrames o Remotion, render y subtítulos.
---

# Vídeo sin cara

## Fases (no saltes la aprobación)

1. **Investigación.** Busca fuentes actuales del tema; anota las URLs en el guion. Todo dato concreto (cifras, nombres, fechas) necesita fuente.
2. **Guion por escenas** en `guion.md`, con este formato:

   ```markdown
   ### Escena N — Título (mm:ss–mm:ss)
   **Voz:** texto exacto que se locuta.
   **Visual:** qué se ve y cómo se mueve.
   **Fuente:** URL (si hay datos).
   ```

   Ritmo: ~150 palabras por minuto en español. Gancho en los primeros 15 s. Una idea por escena.
3. **Aprobación del guion** por el usuario. Sin ella, no generes voz ni animaciones.
4. **Voz.** ElevenLabs TTS (voz elegida en `docs/estilo/identidad.md`) o grabación del usuario limpiada con video-use. Genera una pista por escena para poder ajustar sin rehacer todo.
5. **Animación.** Una composición por escena, con duración igual a la de su pista de voz. Aplica la skill `identidad-visual` en todas. Prueba primero 1 escena y enséñala antes de hacer el resto.
6. **Montaje y render.** Une escenas, voz, música (opcional, -18 dB bajo la voz) y subtítulos. Exporta 1920×1080 a 30 fps (o 1080×1920 para shorts).
7. **Publicación.** Prepara `publicacion.md` y pasa a la skill `publicar-youtube`.

## Consejos

- Mejor diagramas que se construyen paso a paso al ritmo de la voz que textos largos en pantalla.
- Máximo ~8 palabras de texto en pantalla a la vez.
- Reutiliza componentes de vídeos anteriores (`videos/*/animaciones/`).
