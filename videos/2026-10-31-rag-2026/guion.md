# Guion — "¿RAG ha muerto? Cómo funciona y qué se usa de verdad en 2026"

- **Formato:** vídeo sin cara, explicativo animado, 1920×1080
- **Duración objetivo:** ~7:30 (≈1.100 palabras a 150 ppm)
- **Estado:** borrador v1, pendiente de aprobación
- **Visuales:** descritos de forma neutra; se adaptan a la dirección de estilo elegida (`docs/estilo/identidad.md`)

---

### Escena 1 — Gancho (0:00–0:20)
**Voz:** "Los creadores de Claude Code empezaron con una base de datos vectorial, el corazón del RAG clásico, y la quitaron. Desde entonces medio internet dice que el RAG ha muerto. Spoiler: no ha muerto. Ha cambiado de forma. Y si construyes con IA, te interesa saber en qué se ha convertido."
**Visual:** una caja "base de datos vectorial" se tacha; aparece el texto "¿RAG ha muerto?"; el signo de interrogación se convierte en una flecha que gira hacia "ha cambiado".
**Fuente:** https://smartscope.blog/en/ai-development/practices/rag-debate-agentic-search-code-exploration/

### Escena 2 — El problema (0:20–0:50)
**Voz:** "Un modelo de lenguaje sabe muchísimo, pero no sabe nada de lo tuyo: tus contratos, tu documentación interna, el correo de ayer. Puedes pegárselo todo en el prompt, pero cuando son miles de documentos eso es caro y lento. RAG, generación aumentada con recuperación, resuelve justo eso: antes de responder, el sistema busca los trozos relevantes y se los pasa al modelo."
**Visual:** un modelo (forma simple, no un cerebro ni un robot) rodeado de documentos que no puede alcanzar; aparece una "mano" de búsqueda que trae 3 fichas al modelo.

### Escena 3 — RAG clásico en cuatro pasos (0:50–2:00)
**Voz:** "El RAG clásico funciona así. Uno: trocear. Partes tus documentos en fragmentos de unos cientos de palabras. Dos: convertir cada trozo en un vector, una lista de números que representa su significado. Textos que hablan de lo mismo quedan cerca en ese espacio. Tres: cuando llega una pregunta, también la conviertes en vector y buscas los trozos más cercanos. Cuatro: le das esos trozos al modelo junto con la pregunta y le pides que responda usando solo eso. Ventaja enorme: si mañana cambia un documento, lo actualizas en la base de datos y el sistema ya lo sabe. Sin reentrenar nada."
**Visual:** cuatro pasos numerados que se construyen uno a uno: documento → tijeras → fragmentos → puntos en un plano 2D (agrupados por tema) → la pregunta cae como un punto nuevo y se iluminan sus 3 vecinos → los 3 fragmentos entran al modelo → sale la respuesta con citas.

### Escena 4 — Por qué falla el RAG ingenuo (2:00–2:45)
**Voz:** "Y en la práctica, falla. Un trozo suelto pierde su contexto: 'los ingresos crecieron un 3 %'… ¿de qué empresa? ¿De qué trimestre? La búsqueda por significado se equivoca con nombres exactos, códigos de producto o identificadores. Y hay preguntas que ningún trozo responde solo: '¿cuáles son los temas principales de estos mil informes?' o preguntas que necesitan encadenar varios pasos. Para cada uno de estos fallos ha aparecido una solución."
**Visual:** tres tarjetas de fallo que aparecen con una marca roja: "trozo sin contexto", "nombres exactos", "preguntas globales o multipaso". Se quedan en pantalla como índice de lo que viene.

### Escena 5 — Arreglar la búsqueda: híbrida + reranker (2:45–3:45)
**Voz:** "Primer arreglo, y el que más rinde: búsqueda híbrida. Combinas la búsqueda por significado con la búsqueda clásica por palabras clave, la de toda la vida, BM25. Una encuentra lo parecido, la otra lo exacto, y fusionas los dos rankings. Hoy es el estándar en producción. Segundo arreglo: el reranker. Recuperas, por ejemplo, veinte candidatos rápido, y un modelo más preciso los lee uno a uno junto a la pregunta y se queda con los cinco mejores. Es como pasar de buscar en Google a que un experto te filtre los resultados."
**Visual:** dos columnas de resultados (vectores | palabras clave) que se funden en una sola lista; luego un embudo: 20 fichas entran, 5 salen ordenadas.
**Fuente:** https://daily.dev/agentic-ai-hub/rag-retrieval.md/ · https://www.callmissed.com/en/blog/rag-best-practices-2026

### Escena 6 — Darle contexto a cada trozo (3:45–4:30)
**Voz:** "Tercer arreglo, para los trozos huérfanos: recuperación contextual. Antes de indexar, un modelo escribe una frase que sitúa cada trozo: 'esto es del informe de Acme del segundo trimestre de 2023'. Parece poca cosa, pero Anthropic midió que, combinada con búsqueda híbrida, reduce los fallos de recuperación un 49 %, y con reranker, un 67 %. Hay una alternativa más barata, el late chunking, que genera los vectores viendo el documento entero antes de trocearlo."
**Visual:** el trozo "los ingresos crecieron un 3 %" recibe una etiqueta encima con su contexto; barra que baja de 5,7 % a 2,9 % y luego a 1,9 % de fallos.
**Fuente:** https://anthropic.com/news/contextual-retrieval · https://arxiv.org/html/2504.19754v1

### Escena 7 — GraphRAG: cuando importan las relaciones (4:30–5:20)
**Voz:** "Para las preguntas globales está GraphRAG, que popularizó Microsoft. En vez de solo trocear, extrae entidades y relaciones: personas, empresas, productos y cómo se conectan. Construye un grafo y lo agrupa en comunidades con resúmenes. Así puede responder '¿cuáles son los grandes temas?' o '¿qué proveedores dependen de esta pieza?'. El precio: construir y mantener ese grafo es bastante más caro. Úsalo cuando las relaciones sean el corazón del problema, no por moda."
**Visual:** los fragmentos se convierten en nodos con nombres; aparecen aristas; se forman 3 grupos coloreados con una etiqueta-resumen cada uno.
**Fuente:** https://futureagi.com/blog/rag-architecture-llm-2025/ · https://timewell.jp/en/columns/ai-rag-agi

### Escena 8 — Agentic RAG: buscar razonando (5:20–6:15)
**Voz:** "Y el gran cambio de estos dos años: el RAG agéntico. El RAG clásico es una tubería: buscas una vez y respondes. En el agéntico, la búsqueda es una herramienta que el modelo usa cuando quiere. Piensa, busca, mira lo que ha encontrado, decide si le basta, reformula y vuelve a buscar, en documentos, en una base de datos o en la web. Es lo que hace un buen investigador. Ojo con una cosa: hay que darle una condición de parada, o se queda buscando para siempre."
**Visual:** la tubería recta de la escena 3 se dobla y se convierte en un bucle: pensar → buscar → evaluar → (¿suficiente?) → responder; alrededor del bucle aparecen herramientas: documentos, SQL, web.
**Fuente:** https://c3.unu.edu/projects/ai/deepresearch/demo_research-report_searchengine1.html

### Escena 9 — ¿Y el contexto largo? (6:15–6:55)
**Voz:** "Volvamos al principio. Hoy hay modelos con un millón de tokens de contexto, y los agentes de programación como Claude Code ya no usan una base de datos vectorial: exploran el código con búsquedas de texto, abren archivos y deciden qué leer. Eso es lo que la gente llama 'la muerte del RAG'. Pero fíjate: siguen recuperando información antes de responder. Lo que ha muerto es la base de datos vectorial como paso obligatorio. Y meter un millón de tokens en cada pregunta sigue costando muchísimo más que recuperar cinco trozos buenos."
**Visual:** una ventana de contexto gigante llenándose de páginas, con un contador de coste subiendo; al lado, cinco fichas bien elegidas con un coste diminuto.
**Fuente:** https://akitaonrails.com/en/2026/04/06/rag-is-dead-long-context/ · https://www.callmissed.com/blog/rag-best-practices-2026 · https://hamel.dev/blog/posts/evals-faq/is-rag-dead.html

### Escena 10 — Cómo elegir (6:55–7:25)
**Voz:** "Mi recomendación práctica. ¿Pocos documentos? Mételos en el contexto y olvídate. ¿Una base de conocimiento grande tipo FAQ o documentación? RAG con búsqueda híbrida y reranker: es lo que mejor relación esfuerzo-resultado tiene. ¿Muchas relaciones entre entidades? GraphRAG. ¿Tareas de varios pasos? Agentic RAG. Y sobre todo: empieza por lo más simple y sube de nivel solo cuando midas que te hace falta."
**Visual:** árbol de decisión de 4 ramas que se construye rama a rama; la rama "empieza simple" se resalta con el color de acento.
**Fuente:** https://gitcode.csdn.net/6a29183410ee7a33f27a54d3.html

### Escena 11 — Cierre (7:25–7:40)
**Voz:** "El RAG no ha muerto, ha madurado. Si quieres que en el próximo vídeo montemos uno de estos paso a paso, dímelo en los comentarios."
**Visual:** el "¿RAG ha muerto?" de la escena 1 vuelve y se transforma en "RAG ha madurado"; firma del canal.

---

## Notas para revisión

- Las cifras de la escena 6 (35 % / 49 % / 67 %, de 5,7 % a 1,9 %) vienen del benchmark de Anthropic de 2024: miden fallos de recuperación en el top-20, no la calidad final de la respuesta.
- "Bastante más caro" en GraphRAG es intencionadamente vago: una fuente habla de 3–5× pero no es primaria.
- La cita de la escena 1 viene de un artículo de terceros que recoge la frase del equipo de Claude Code; conviene enlazarla en la descripción.
- Las opiniones ("mi recomendación") son tuyas: cámbialas si no las compartes.
