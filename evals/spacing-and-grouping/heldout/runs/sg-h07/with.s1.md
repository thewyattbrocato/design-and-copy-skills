I couldn't save the file. The Write tool is disabled in this session, and I have no other way to create files. I've included the full single-file layout below so you can save it as `index.html` yourself.

I didn't open it in a browser, so I haven't seen it rendered.

- **Filters:** one tinted bar across the top holds date, room and engineer, with Reset and "+ New booking" on the right.
- **Schedule:** a single list with 10 hourly slots from 09:00 to 19:00. Each row shows the time, the title with client and engineer, and a status tag (Confirmed, Hold, Blocked or Open). The selected row has an accent bar.
- **Summary:** the side panel updates when you click a slot. It shows the booking's time, room, client, engineer, rate and total, plus notes and actions. Open slots show "Book slot" and "Hold" instead.
- **Spacing:** every gap is a multiple of 4 px, and gaps inside a group are smaller than gaps between groups. The list has hairline dividers, and the only card-like surfaces are the list and the summary panel.
- **Other details:** it uses system fonts only, follows light and dark mode, and stacks to one column below 800 px.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Studio Bookings</title>
<style>
  :root {
    --s1: 4px; --s2: 8px; --s3: 12px; --s4: 16px; --s5: 24px;
    --bg: #f4f5f7; --surface: #fff; --ink: #1b1f27; --muted: #5d6675;
    --rule: #e1e4ea; --tint: #eceef3; --accent: #2b5fd9; --accent-soft: #e6edfc;
    --ok: #1f7a4d; --ok-bg: #e3f4ea; --hold: #94600a; --hold-bg: #fbefd5;
    --busy: #5d6675; --busy-bg: #eceef3;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 14px; line-height: 20px; color: var(--ink);
  }
  @media (prefers-color-scheme: dark) {
    :root { --bg:#14161b; --surface:#1d2027; --ink:#e8eaef; --muted:#98a1b0; --rule:#2d323c;
      --tint:#262a33; --accent:#7ea2f5; --accent-soft:#23304f; --ok:#6fd3a0; --ok-bg:#1b3328;
      --hold:#f0c36d; --hold-bg:#3a2f17; --busy:#98a1b0; --busy-bg:#262a33; }
  }
  * { box-sizing: border-box; }
  body { margin: 0; background: var(--bg); }
  .app { max-width: 1120px; margin: 0 auto; padding: var(--s5); display: grid; gap: var(--s5); }
  header { display: flex; align-items: baseline; justify-content: space-between; gap: var(--s4); }
  h1 { margin: 0; font-size: 18px; line-height: 24px; font-weight: 650; }
  h2 { margin: 0; font-size: 12px; line-height: 16px; font-weight: 600; letter-spacing: .06em; text-transform: uppercase; color: var(--muted); }
  .meta { color: var(--muted); }

  .filters { display: flex; flex-wrap: wrap; align-items: flex-end; gap: var(--s4);
    background: var(--tint); border-radius: 8px; padding: var(--s3) var(--s4); }
  .field { display: grid; gap: var(--s1); }
  .field label { font-size: 12px; line-height: 16px; color: var(--muted); }
  select, input[type=date], button { font: inherit; color: inherit; height: 32px; padding: 0 var(--s3);
    border: 1px solid var(--rule); border-radius: 6px; background: var(--surface); }
  select { min-width: 160px; }
  button { cursor: pointer; padding: 0 var(--s4); }
  button.primary { background: var(--accent); border-color: var(--accent); color: #fff; font-weight: 600; }
  button:focus-visible, select:focus-visible, input:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
  .filters .spacer { flex: 1; }

  .main { display: grid; grid-template-columns: minmax(0,1fr) 300px; gap: var(--s5); align-items: start; }
  @media (max-width: 800px) { .main { grid-template-columns: 1fr; } }

  .schedule { display: grid; gap: var(--s2); }
  .sched-head { display: flex; justify-content: space-between; align-items: baseline; }
  .list { list-style: none; margin: 0; padding: 0; background: var(--surface);
    border: 1px solid var(--rule); border-radius: 8px; overflow: hidden; }
  .list li + li { border-top: 1px solid var(--rule); }
  .slot { display: grid; grid-template-columns: 96px minmax(0,1fr) auto; align-items: center; gap: var(--s4);
    width: 100%; height: auto; min-height: 44px; padding: var(--s2) var(--s4);
    border: 0; border-radius: 0; background: transparent; text-align: left; }
  .slot:hover { background: var(--tint); }
  .slot[aria-pressed=true] { background: var(--accent-soft); box-shadow: inset 3px 0 0 var(--accent); }
  .time { font-variant-numeric: tabular-nums; color: var(--muted); }
  .what { display: grid; min-width: 0; }
  .what b { font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .what span { color: var(--muted); font-size: 12px; line-height: 16px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .slot.open .what b { font-weight: 400; color: var(--muted); }
  .tag { font-size: 12px; line-height: 16px; padding: 2px var(--s2); border-radius: 999px; font-weight: 600; }
  .t-ok { color: var(--ok); background: var(--ok-bg); }
  .t-hold { color: var(--hold); background: var(--hold-bg); }
  .t-busy { color: var(--busy); background: var(--busy-bg); }
  .t-open { color: var(--muted); border: 1px dashed var(--rule); padding: 1px var(--s2); font-weight: 400; }

  aside { background: var(--surface); border: 1px solid var(--rule); border-radius: 8px;
    padding: var(--s4); display: grid; gap: var(--s5); }
  .sum-top { display: grid; gap: var(--s1); justify-items: start; }
  .sum-top .title { font-size: 16px; line-height: 24px; font-weight: 650; }
  dl { margin: 0; display: grid; grid-template-columns: auto 1fr; gap: var(--s2) var(--s4); }
  dt { color: var(--muted); }
  dd { margin: 0; text-align: right; font-variant-numeric: tabular-nums; }
  .total { border-top: 1px solid var(--rule); padding-top: var(--s3); font-weight: 650; }
  .note { margin: 0; color: var(--muted); }
  .actions { display: flex; gap: var(--s2); }
  .actions button { flex: 1; }
</style>
</head>
<body>
<div class="app">
  <header>
    <h1>Studio Bookings</h1>
    <span class="meta">Harbor Lane Recording · 3 rooms · 4 engineers</span>
  </header>

  <form class="filters" aria-label="Filters" onsubmit="return false">
    <div class="field"><label for="f-date">Date</label><input id="f-date" type="date" value="2026-10-28"></div>
    <div class="field"><label for="f-room">Room</label>
      <select id="f-room"><option>All rooms</option><option selected>Studio A – Live Room</option><option>Studio B – Mix Suite</option><option>Studio C – Vocal Booth</option></select></div>
    <div class="field"><label for="f-eng">Engineer</label>
      <select id="f-eng"><option>Any engineer</option><option>Dana Okafor</option><option>Marcus Lee</option><option>Priya Nair</option><option>Tom Reyes</option></select></div>
    <div class="spacer"></div>
    <button type="reset">Reset</button>
    <button type="submit" class="primary">+ New booking</button>
  </form>

  <div class="main">
    <section class="schedule" aria-labelledby="sched-h">
      <div class="sched-head">
        <h2 id="sched-h">Wed 28 Oct · Studio A</h2>
        <span class="meta">6 booked · 1 hold · 3 open</span>
      </div>
      <ul class="list" id="list"></ul>
    </section>
    <aside aria-live="polite" id="summary"></aside>
  </div>
</div>

<script>
  const slots = [
    ["09:00","10:00","Drum tracking","Ember & Oak · Dana Okafor","ok","Confirmed",180,"Full kit, 8 mics. Drums set up from 08:30."],
    ["10:00","11:00","Drum tracking","Ember & Oak · Dana Okafor","ok","Confirmed",180,"Continuation of previous block."],
    ["11:00","12:00","Available","","open","Open",0,""],
    ["12:00","13:00","Setup / lunch","Studio hold · Marcus Lee","busy","Blocked",0,"Maintenance: patch bay check."],
    ["13:00","14:00","Guitar overdubs","J. Alvarez · Marcus Lee","ok","Confirmed",150,"Two amps, ribbon mic on cab."],
    ["14:00","15:00","Guitar overdubs","J. Alvarez · Marcus Lee","ok","Confirmed",150,"Bring second guitar for tuning change."],
    ["15:00","16:00","Podcast session","Night Signal · Priya Nair","hold","Hold",120,"Deposit pending, expires today 12:00."],
    ["16:00","17:00","Available","","open","Open",0,""],
    ["17:00","18:00","Available","","open","Open",0,""],
    ["18:00","19:00","String quartet","Calder Quartet · Tom Reyes","ok","Confirmed",220,"Four players, close + room mics."]
  ];
  const tagCls = {ok:"t-ok",hold:"t-hold",busy:"t-busy",open:"t-open"};
  const list = document.getElementById("list"), summary = document.getElementById("summary");
  let sel = 0;
  const esc = s => s.replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));

  function renderList(){
    list.innerHTML = slots.map((s,i) => `
      <li><button type="button" class="slot ${s[4]==="open"?"open":""}" data-i="${i}" aria-pressed="${i===sel}">
        <span class="time">${s[0]}–${s[1]}</span>
        <span class="what"><b>${esc(s[2])}</b>${s[3]?`<span>${esc(s[3])}</span>`:""}</span>
        <span class="tag ${tagCls[s[4]]}">${s[5]}</span>
      </button></li>`).join("");
  }
  function renderSummary(){
    const s = slots[sel];
    if (s[4]==="open"){
      summary.innerHTML = `
        <div class="sum-top"><h2>Selected slot</h2><div class="title">${s[0]}–${s[1]}</div><span class="meta">Studio A – Live Room</span></div>
        <p class="note">This slot is open. Rate: $150/hr.</p>
        <div class="actions"><button class="primary">Book slot</button><button>Hold</button></div>`;
      return;
    }
    const [who, eng] = s[3].split(" · ");
    summary.innerHTML = `
      <div class="sum-top"><h2>Selected booking</h2><div class="title">${esc(s[2])}</div>
        <span class="tag ${tagCls[s[4]]}">${s[5]}</span></div>
      <dl><dt>Time</dt><dd>${s[0]}–${s[1]}</dd><dt>Room</dt><dd>Studio A</dd>
        <dt>Client</dt><dd>${esc(who)}</dd><dt>Engineer</dt><dd>${esc(eng||"—")}</dd></dl>
      ${s[6] ? `<dl><dt>Rate</dt><dd>$${s[6]}/hr</dd><dt>Duration</dt><dd>1 hr</dd>
        <dt class="total">Total</dt><dd class="total">$${s[6]}</dd></dl>` : ""}
      <p class="note">${esc(s[7])}</p>
      <div class="actions"><button class="primary">Edit</button><button>Cancel</button></div>`;
  }
  list.addEventListener("click", e => {
    const b = e.target.closest(".slot"); if (!b) return;
    sel = +b.dataset.i; renderList(); renderSummary();
    list.querySelector(`[data-i="${sel}"]`).focus();
  });
  renderList(); renderSummary();
</script>
</body>
</html>
```

If you re-enable Write, I can save it to `/tmp/eval-gen/index.html` and adjust it from there.
