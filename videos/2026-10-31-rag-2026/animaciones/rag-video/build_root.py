#!/usr/bin/env python3
"""Genera index.html (composición raíz) a partir de las duraciones reales de la voz.

Cada escena del guion tiene su mp3 y su words.json en ../../audio/voice/.
Las escenas largas se reparten en varias subcomposiciones (SPLITS): el corte
se hace en un instante de la voz, en segundos locales de la escena.
Uso: python3 build_root.py  (reescribe index.html y timeline.json)

Cambio de voz: las animaciones se escribieron con los tiempos de la voz de
referencia (AUTHORING, la voz «Daniel» en ../../audio/voice-daniel/). Si la voz
actual (../../audio/voice/) dice el mismo texto, el script calcula para cada
composición un mapa tiempo de referencia -> tiempo actual (un ancla por palabra)
y lo inyecta entre /* warp:start */ y /* warp:end */: una línea de tiempo
exterior que mueve la original a trozos lineales. Los números de las
composiciones siguen en tiempo de referencia: no hay que tocarlos.
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
VOICE = HERE / "../../audio/voice"
AUTHORING = HERE / "../../audio/voice-daniel"   # voz con la que se escribieron los tiempos
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

def words_of(folder, scene):
    return json.loads((folder / f"scene-{scene}.words.json").read_text())


def interp(x, xs, ys):
    """Interpolación lineal a trozos (xs creciente)."""
    if x <= xs[0]:
        return ys[0] + (x - xs[0])
    for i in range(1, len(xs)):
        if x <= xs[i]:
            f = (x - xs[i - 1]) / (xs[i] - xs[i - 1]) if xs[i] > xs[i - 1] else 0
            return ys[i - 1] + f * (ys[i] - ys[i - 1])
    return ys[-1] + (x - xs[-1])


def layout(folder, splits):
    scenes, t = [], LEAD
    for scene, parts in splits.items():
        voice = round(words_of(folder, scene)["duration"], 2)
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
    return scenes, round(t, 2)


def word_times(folder, scene):
    return [w["start"] for w in words_of(folder, scene)["words"]]


# Los cortes de SPLITS están en tiempo de la voz de referencia: se trasladan a la voz actual.
cur_splits = {}
for scene, parts in SPLITS.items():
    a, c = word_times(AUTHORING, scene), word_times(VOICE, scene)
    assert len(a) == len(c), f"escena {scene}: la voz actual no dice el mismo texto ({len(a)} vs {len(c)} palabras)"
    cur_splits[scene] = [(cid, round(interp(local, a, c), 2) if i else 0) for i, (cid, local) in enumerate(parts)]

ref_scenes, _ = layout(AUTHORING, SPLITS)
scenes, TOTAL = layout(VOICE, cur_splits)

# Mapa de tiempos por composición: (tiempo de referencia, tiempo actual), un ancla por palabra.
WARP_JS = """/* warp:start (generado por build_root.py: no editar) */
      window.__timelines = window.__timelines || {{}};
      const warp = gsap.timeline({{ paused: true }});
      const W = {anchors};
      for (let i = 0; i < W.length - 1; i++) {{
        warp.fromTo(tl, {{ time: W[i][0] }}, {{ time: W[i + 1][0], duration: W[i + 1][1] - W[i][1], ease: "none", immediateRender: false }}, W[i][1]);
      }}
      window.__timelines["{cid}"] = warp;
      /* warp:end */"""
import re
for ref, cur in zip(ref_scenes, scenes):
    a, c = word_times(AUTHORING, ref["scene"]), word_times(VOICE, cur["scene"])
    pts = [(0.0, 0.0)]
    for ta, tc in zip(a, c):
        la, lc = ta + ref["word_to_local"], tc + cur["word_to_local"]
        if 0 < la < ref["duration"] and 0 < lc < cur["duration"]:
            pts.append((round(la, 3), round(lc, 3)))
    pts.append((ref["duration"], cur["duration"]))
    clean = [pts[0]]
    for p in pts[1:]:
        if p[0] - clean[-1][0] >= 0.05 and p[1] - clean[-1][1] >= 0.05:
            clean.append(p)
    clean[-1] = pts[-1]
    f = HERE / "compositions" / f"{cur['id']}.html"
    html = f.read_text()
    block = WARP_JS.format(anchors=json.dumps([list(p) for p in clean], separators=(",", ":")), cid=cur["id"])
    if "/* warp:start" in html:
        html = re.sub(r"/\* warp:start.*?/\* warp:end \*/", lambda m: block, html, flags=re.S)
    else:
        old = re.search(r'window\.__timelines = window\.__timelines \|\| \{\};\s*window\.__timelines\["' + cur["id"] + r'"\] = tl;', html)
        assert old, f"{f.name}: no encuentro el registro de la línea de tiempo"
        html = html[:old.start()] + block + html[old.end():]
    f.write_text(html)

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
