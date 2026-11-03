"""Build the wide (16:9) loop engineering card from the one page exhibit.

The graph markup and its styles are lifted from loop-engineering.html, so
the two never drift apart. Run, then screenshot loop-engineering-wide.html
at 1600x900 with a 2x device scale.
"""
import re
from pathlib import Path

HERE = Path(__file__).parent
page = (HERE / "loop-engineering.html").read_text()

css = re.search(r"<style>(.*?)</style>", page, re.S).group(1)
start = page.index('<div class="graph">')
end = page.index('<div class="rulebar">')
graph = page[start:end].rstrip()

SCALE = 1.45
GW, GH = 728, 347

wide = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=1600">
<title>Loop Engineering · Andrew James Johnson</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
{css}
/* ---------- wide card: 1600 x 900 ---------- */
html,body{{background:var(--sheet)!important;padding:0!important;margin:0}}
.card{{width:1600px;height:900px;padding:46px 64px 36px;display:flex;flex-direction:column;overflow:hidden;background:var(--sheet)}}
.card > *{{flex-shrink:0}}
.top{{display:flex;justify-content:space-between;align-items:flex-start;gap:40px}}
.card .kicker{{font-size:12.5px;margin-top:0}}
.card h1{{font-size:46px;margin-top:6px}}
.card .lede{{font-size:17px;line-height:1.5;margin-top:10px;max-width:1240px}}
.chain{{font-family:var(--display);font-size:13.5px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--ink);margin-top:14px}}
.chain i{{font-style:normal;font-weight:400;color:var(--light);margin:0 10px}}
.chain span{{font-family:var(--text);font-weight:400;letter-spacing:0;text-transform:none;color:var(--grey);font-size:14px;margin-left:6px}}
.who{{text-align:right}}
.who .name{{font-size:23px}}
.who .title{{font-size:10.5px;margin-top:6px}}
.who .gh{{font-size:13px;color:var(--mid);margin-top:4px}}
.mid{{display:flex;gap:44px;margin-top:24px}}
.gwrap{{width:{GW * SCALE:.1f}px;height:{GH * SCALE:.1f}px;flex:0 0 auto}}
.gwrap .graph{{width:{GW}px;height:{GH}px;margin:0;transform:scale({SCALE});transform-origin:0 0}}
.ev{{flex:1;align-self:flex-start;margin-top:{10 * SCALE - 1:.1f}px;border-top:2px solid var(--ink);padding-top:12px}}
.ev h2{{font-size:15px}}
.ev .stat{{margin-top:17px}}
.ev .stat .v{{font-size:36px}}
.ev .stat .v small{{font-size:19px}}
.ev .stat .t{{font-size:13.6px;line-height:1.42;margin-top:6px}}
.bottom{{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;gap:40px;border-top:1px solid var(--rule);padding-top:12px}}
.card .chain{{border-top:0;padding-top:0}}
.ev .rulel{{font-family:var(--display);font-size:14px;font-weight:500;line-height:1.4;color:var(--ink);margin-top:18px;border-top:1px solid var(--rule);padding-top:12px}}
.bottom .big{{font-family:var(--display);font-size:19px;font-weight:500;color:var(--ink);line-height:1.3}}
.bottom .blue{{font-family:var(--display);font-size:19px;font-weight:600;color:var(--loop);line-height:1.3;margin-top:4px}}
.bottom .foot{{font-family:var(--display);font-size:11px;font-weight:500;letter-spacing:.16em;text-transform:uppercase;color:var(--light);white-space:nowrap;border:0;padding:0;margin:0}}
</style>
</head>
<body>
<div class="card">
  <div class="top">
    <div>
      <div class="kicker">Loop &amp; graph engineering</div>
      <h1>Same model. <span>Better system.</span></h1>
      <p class="lede">A better model alone changes little. The system around it does the work: a harness, a graph that joins the steps, and loops that learn from real results. Shown on clips built with Anthropic's Claude, but any system is data in, a decision, data out, and a check.</p>
      <div class="chain">Prompt<i>→</i>Agent<i>→</i>Harness<i>→</i>Loop<i>→</i>Graph<span>each one wraps the one before</span></div>
    </div>
  </div>

  <div class="mid">
    <div class="gwrap">
    {graph}
    </div>
    <section class="ev">
      <h2>Evidence, not confidence</h2>
      <div class="stat"><div class="v">6</div><div class="t">Reels a day is all Facebook shows a Page this size. The first two drew 94% of views, so the best clip now leads.</div></div>
      <div class="stat"><div class="v">33</div><div class="t">real past jobs rerun before an engine change ships. The first replay: 0 new failures.</div></div>
      <div class="stat"><div class="v">36<small>%</small></div><div class="t">of the time the AI critic agreed with my calls. So its gate stays in shadow until it reaches 70% across 12 calls.</div></div>
      <div class="stat"><div class="v">402</div><div class="t">gate refusals in 7 days, counted by rule. The top 3 now open every night's run, each with its rule.</div></div>
      <div class="rulel">Inner loops change numbers. Outer loops change rules. Only a person changes taste.</div>
    </section>
  </div>

  <div class="bottom">
    <div>
      <div class="big">A system like this, in any niche, running on its own 24/7, is where the value in AI lies.</div>
      <div class="blue">The more compute you own, the more loops you run, and the deeper each one goes.</div>
    </div>
    <div class="who">
      <div class="name"><b>Andrew</b> James Johnson</div>
      <div class="title">Applied AI &amp; Systems Builder</div>
      <div class="gh">github.com/andrewjamesjohnson</div>
    </div>
  </div>
</div>
</body>
</html>
"""
(HERE / "loop-engineering-wide.html").write_text(wide)
print("wrote loop-engineering-wide.html")
