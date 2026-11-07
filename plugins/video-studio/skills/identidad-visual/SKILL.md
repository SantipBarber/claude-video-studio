---
name: identidad-visual
description: Aplica la identidad visual del canal (paleta, tipografías, movimiento, firma) a animaciones, escenas y miniaturas para que sean visuales, potentes y modernas, no genéricas. Úsala siempre que generes una animación, escena, overlay o miniatura.
---

# Identidad visual

## Fuente de verdad

Lee `docs/estilo/identidad.md` del repo `haividio`. Si existe `docs/estilo/tokens.css`, impórtalo en las composiciones de HyperFrames, o tradúcelo a constantes en Remotion. Si la identidad todavía está "pendiente de elegir dirección", pregunta al usuario cuál usar antes de animar.

## Antes de entregar cualquier escena, revisa

- [ ] Solo colores de la paleta, y el acento solo para lo importante (≤ 10 % de la pantalla).
- [ ] Solo las tipografías de la guía; nada de Inter, Poppins ni Roboto.
- [ ] Nada genérico de plantilla: mejor datos y recursos reales (docs/recursos-abiertos.md) que iconos de relleno.
- [ ] Ritmo de movimiento coherente con la dirección elegida, sin el mismo fade+slide repetido en todo.
- [ ] ≤ 8 palabras de texto en pantalla a la vez.
- [ ] La firma del canal aparece donde toca (intro, cabecera de capítulo, transición).
- [ ] Legible en móvil: texto ≥ 42 px en 1080p y contraste suficiente.

## Miniaturas

Mismo fondo y acento que el vídeo, máximo 4 palabras, un único elemento visual dominante. Genera 2 variantes para que el usuario elija.

## Evolución

Si el usuario corrige algo del estilo ("menos rojo", "más lento"), propón actualizar `docs/estilo/identidad.md` para que la corrección valga también para los siguientes vídeos.
