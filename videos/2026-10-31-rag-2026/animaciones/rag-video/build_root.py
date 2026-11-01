#!/usr/bin/env python3
"""Genera index.html (composición raíz) a partir de las duraciones reales de la voz.

Cada escena del guion tiene su mp3 y su words.json en ../../audio/voice/.
Las escenas largas se reparten en varias subcomposiciones (SPLITS): el corte
se hace en un instante de la voz, en segundos locales de la escena.
Uso: python3 build_root.py  (reescribe index.html y timeline.json)
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
VOICE = HERE / "../../audio/voice"
GAP = 0.7      # silencio entre escenas
LEAD = 0.5     # el vídeo empieza medio segundo antes de la primera palabra
TAIL = 1.5     # cola tras la última palabra

# escena del guion -> [(id de la composición, inicio local en la voz)]
SPLITS = {
    "1": [("hook", 0)],
    "2": [("problem", 0)],
    "2b": [("openbook", 0)],
    "3a": [("twomoments", 0)],
    "3b": [("chunk", 0), ("embed", 18.3)],
    "3c": [("search", 0), ("topk", 7.4), ("generate", 18.2)],
    "4": [("failures", 0)],
    "5": [("hybrid", 0)],
    "6": [("contextual", 0)],
    "7": [("graphrag", 0)],
    "8": [("agentic", 0), ("warnings", 30.6)],
    "9": [("longcontext", 0)],
    "10": [("choose", 0)],
    "11": [("outro", 0)],
}

scenes, t = [], LEAD
for scene, parts in SPLITS.items():
    words = json.loads((VOICE / f"scene-{scene}.words.json").read_text())
    voice = round(words["duration"], 2)
    end = t + voice + (GAP if scene != "11" else TAIL)
    for i, (cid, local) in enumerate(parts):
        start = t + local if i else (0 if scene == "1" else t)
        stop = t + parts[i + 1][1] if i + 1 < len(parts) else end
        scenes.append({"id": cid, "scene": scene, "start": round(start, 2),
                       "duration": round(stop - start, 2),
                       # tiempo local en la composición = tiempo de la palabra en words.json + word_to_local
                       "word_to_local": round(t - start, 2)})
    scenes[-1]["voice"] = {"scene": scene, "start": round(t, 2), "duration": voice}
    t = end
TOTAL = round(t, 2)

tracker_from = next(s["start"] for s in scenes if s["id"] == "twomoments")
tracker_to = next(s["start"] + s["duration"] for s in scenes if s["id"] == "generate")
step_at = {i: next(s["start"] for s in scenes if s["id"] == cid)
           for i, cid in enumerate(["chunk", "embed", "search", "generate"])}

hosts = "\n".join(
    f'      <div id="scene-{s["id"]}" class="host" data-composition-id="{s["id"]}" '
    f'data-composition-src="compositions/{s["id"]}.html"\n'
    f'        data-start="{s["start"]}" data-duration="{s["duration"]}" data-track-index="1" '
    f'data-track-kind="graphics" data-width="1920" data-height="1080"></div>'
    for s in scenes)
voices = [s["voice"] for s in scenes if "voice" in s]
audios = "\n".join(
    f'      <audio id="voice-{v["scene"]}" class="clip" src="assets/audio/scene-{v["scene"]}.mp3" '
    f'data-start="{v["start"]}" data-duration="{v["duration"]}" data-track-index="{3 + i % 2}" data-volume="1"></audio>'
    for i, v in enumerate(voices))

html = f"""<!doctype html>
<html lang="es" data-resolution="landscape">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <script src="assets/gsap.min.js"></script>
    <style>
      @font-face {{ font-family: "Geist"; src: url("assets/fonts/geist-sans-latin-400-normal.woff2") format("woff2"); font-weight: 400; }}
      @font-face {{ font-family: "Geist"; src: url("assets/fonts/geist-sans-latin-500-normal.woff2") format("woff2"); font-weight: 500; }}
      @font-face {{ font-family: "Geist"; src: url("assets/fonts/geist-sans-latin-700-normal.woff2") format("woff2"); font-weight: 700; }}
      @font-face {{ font-family: "Geist"; src: url("assets/fonts/geist-sans-latin-800-normal.woff2") format("woff2"); font-weight: 800; }}
      @font-face {{ font-family: "Geist Mono"; src: url("assets/fonts/geist-mono-latin-400-normal.woff2") format("woff2"); font-weight: 400; }}
      @font-face {{ font-family: "Geist Mono"; src: url("assets/fonts/geist-mono-latin-500-normal.woff2") format("woff2"); font-weight: 500; }}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1920px; height: 1080px; overflow: hidden; background: #07080b; }}
      #root {{ position: relative; width: 1920px; height: 1080px; font-family: "Geist", sans-serif; color: #f4f5f7; }}
      #bg {{ position: absolute; inset: 0; background-image: radial-gradient(#1c2029 1.5px, transparent 1.5px); background-size: 40px 40px; }}
      .host {{ position: absolute; inset: 0; }}
      #tracker {{ position: absolute; left: 120px; top: 70px; display: flex; gap: 14px; z-index: 10; }}
      .step {{ font-family: "Geist Mono", monospace; font-size: 28px; color: #8b90a0; padding: 12px 22px; border: 2px solid #232733; border-radius: 999px; }}
      .step b {{ font-weight: 500; margin-right: 10px; }}
    </style>
  </head>
  <body>
    <!-- Vídeo completo de RAG (guion v2). GENERADO por build_root.py: no editar a mano. -->
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1920" data-height="1080">
      <div id="bg" class="clip" data-start="0" data-duration="{TOTAL}" data-track-index="0"></div>

{hosts}

      <!-- Firma del canal: barra de pasos 01–04, de la escena 3a al final de la 3c -->
      <div id="tracker" class="clip" data-start="{tracker_from}" data-duration="{round(tracker_to - tracker_from, 2)}" data-track-index="2">
        <div class="step" id="s1"><b>01</b>Trocear</div>
        <div class="step" id="s2"><b>02</b>Vectorizar</div>
        <div class="step" id="s3"><b>03</b>Buscar</div>
        <div class="step" id="s4"><b>04</b>Generar</div>
      </div>

{audios}
    </div>

    <script>
      const tl = gsap.timeline({{ paused: true }});
      const steps = ["#s1", "#s2", "#s3", "#s4"];
      const activate = (idx, at) => {{
        steps.forEach((s, i) => {{
          tl.to(s, {{
            color: i === idx ? "#11140a" : i < idx ? "#f4f5f7" : "#8b90a0",
            backgroundColor: i === idx ? "#d4ff3a" : "rgba(212,255,58,0)",
            borderColor: i === idx ? "#d4ff3a" : i < idx ? "#3a3f4d" : "#232733",
            duration: 0.35, ease: "power2.out",
          }}, at);
        }});
      }};
      // La barra nace en la escena 3a, cuando la voz dice «Un RAG tiene dos momentos».
      tl.from("#tracker .step", {{ autoAlpha: 0, y: -20, stagger: 0.08, duration: 0.5, ease: "power3.out" }}, {tracker_from + 0.4});
{chr(10).join(f'      activate({i}, {round(at + 0.2, 2)});' for i, at in step_at.items())}
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
"""
(HERE / "index.html").write_text(html)
(HERE / "timeline.json").write_text(json.dumps({"total": TOTAL, "scenes": scenes}, ensure_ascii=False, indent=1))
print(f"index.html: {len(scenes)} escenas, {TOTAL} s")
