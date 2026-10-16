I couldn't save the file because the Write tool is disabled in this session. The full page is below. Save it as `studio-booking.html` and open it in a browser.

It's one file with inline CSS and JS, system fonts and no external assets. I haven't opened it in a browser, so the layout is untested.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Studio Bookings</title>
<style>
  :root {
    --s1: 4px; --s2: 8px; --s3: 12px; --s4: 16px; --s5: 24px; --s6: 32px;
    --bg: #f4f5f7; --surface: #fff; --tint: #eaecf0;
    --ink: #1b1f27; --muted: #5d6675; --rule: #dfe2e8;
    --accent: #2a5bd7; --accent-bg: #e8eefc;
    --ok: #1d7a46; --warn: #a15c00; --off: #7a8190;
    font: 13px/1.4 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
    color: var(--ink);
  }
  * { box-sizing: border-box; }
  body { margin: 0; background: var(--bg); }
  .app { max-width: 1100px; margin: 0 auto; padding: var(--s5); display: grid; gap: var(--s5); }

  header { display: flex; align-items: baseline; justify-content: space-between; gap: var(--s4); }
  h1 { margin: 0; font-size: 18px; }
  h2 { margin: 0; font-size: 11px; letter-spacing: .06em; text-transform: uppercase; color: var(--muted); }
  .stats { display: flex; gap: var(--s5); color: var(--muted); }
  .stats b { color: var(--ink); font-variant-numeric: tabular-nums; }

  /* filters: one tinted region, since the controls must read as one unit */
  .filters { display: flex; flex-wrap: wrap; align-items: flex-end; gap: var(--s4);
    background: var(--tint); padding: var(--s3) var(--s4); border-radius: 6px; }
  .field { display: grid; gap: var(--s1); }
  .field label { font-size: 11px; color: var(--muted); }
  input, select, button { font: inherit; color: inherit; }
  input, select { height: 32px; padding: 0 var(--s3); background: var(--surface);
    border: 1px solid var(--rule); border-radius: 4px; min-width: 160px; }
  .filters .spacer { flex: 1; }
  .btn { height: 32px; padding: 0 var(--s4); border: 1px solid var(--rule); background: var(--surface);
    border-radius: 4px; cursor: pointer; }
  .btn.primary { background: var(--accent); border-color: var(--accent); color: #fff; }
  :is(input, select, button):focus-visible { outline: 2px solid var(--accent); outline-offset: 1px; }

  .main { display: grid; grid-template-columns: minmax(0, 1fr) 300px; gap: var(--s5); align-items: start; }

  .schedule { display: grid; gap: var(--s2); }
  .schedule-head { display: flex; justify-content: space-between; align-items: baseline; }
  .rows { margin: 0; padding: 0; list-style: none; background: var(--surface);
    border: 1px solid var(--rule); border-radius: 6px; overflow: hidden; }
  .rows li + li { border-top: 1px solid var(--rule); }
  .row { width: 100%; display: grid; grid-template-columns: 96px minmax(0, 1fr) 120px 88px;
    gap: var(--s4); align-items: center; padding: var(--s2) var(--s4); min-height: 44px;
    border: 0; border-left: 3px solid transparent; background: none; text-align: left; cursor: pointer; }
  .row:hover { background: var(--bg); }
  .row[aria-pressed="true"] { background: var(--accent-bg); border-left-color: var(--accent); }
  .row.dim { opacity: .35; }
  .time { font-variant-numeric: tabular-nums; font-weight: 600; }
  .what { display: grid; min-width: 0; }
  .what span:first-child { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .sub, .eng { color: var(--muted); font-size: 12px; }
  .free .what span:first-child { color: var(--off); }
  .tag { justify-self: end; font-size: 11px; font-weight: 600; }
  .tag::before { content: ""; display: inline-block; width: 6px; height: 6px; border-radius: 50%;
    background: currentColor; margin-right: var(--s1); vertical-align: 1px; }
  .confirmed { color: var(--ok); } .hold { color: var(--warn); } .open { color: var(--off); }

  /* summary: space and headings only, no nested boxes */
  .summary { background: var(--surface); border: 1px solid var(--rule); border-radius: 6px;
    padding: var(--s4); display: grid; gap: var(--s5); position: sticky; top: var(--s5); }
  .block { display: grid; gap: var(--s2); }
  .summary h3 { margin: 0; font-size: 16px; }
  dl { margin: 0; display: grid; grid-template-columns: auto 1fr; gap: var(--s1) var(--s4); }
  dt { color: var(--muted); } dd { margin: 0; text-align: right; font-variant-numeric: tabular-nums; }
  dt.total, dd.total { border-top: 1px solid var(--rule); padding-top: var(--s2); font-weight: 600; }
  .actions { display: flex; gap: var(--s2); }
  .actions .btn { flex: 1; }
  .notes { margin: 0; color: var(--muted); }

  @media (max-width: 800px) {
    .app { padding: var(--s4); gap: var(--s4); }
    .main { grid-template-columns: 1fr; }
    .summary { position: static; }
    .row { grid-template-columns: 80px minmax(0, 1fr) 80px; }
    .eng { display: none; }
  }
</style>
</head>
<body>
<div class="app">
  <header>
    <h1>Studio Bookings</h1>
    <div class="stats">
      <span>Booked <b id="st-booked">0</b>/10</span>
      <span>Holds <b id="st-holds">0</b></span>
      <span>Revenue <b id="st-rev">$0</b></span>
    </div>
  </header>

  <section class="filters" aria-label="Filters">
    <div class="field"><label for="f-date">Date</label>
      <input id="f-date" type="date" value="2026-10-15"></div>
    <div class="field"><label for="f-room">Room</label>
      <select id="f-room"><option value="">All rooms</option><option>Studio A</option><option>Studio B</option><option>Vocal Booth</option></select></div>
    <div class="field"><label for="f-eng">Engineer</label>
      <select id="f-eng"><option value="">All engineers</option><option>Maya Ortiz</option><option>Dev Patel</option><option>Jonas Reid</option></select></div>
    <span class="spacer"></span>
    <button class="btn" id="reset" type="button">Reset</button>
    <button class="btn primary" type="button">New booking</button>
  </section>

  <div class="main">
    <section class="schedule" aria-labelledby="sch-h">
      <div class="schedule-head">
        <h2 id="sch-h">Day schedule</h2>
        <span class="sub" id="day-label"></span>
      </div>
      <ul class="rows" id="rows"></ul>
    </section>

    <aside class="summary" aria-live="polite" id="summary"></aside>
  </div>
</div>

<script>
  const RATE = { "Studio A": 120, "Studio B": 90, "Vocal Booth": 60 };
  const slots = [
    ["09:00","Studio A","Maya Ortiz","Halden Quartet","Tracking — strings","confirmed"],
    ["10:00","Studio A","Maya Ortiz","Halden Quartet","Tracking — strings","confirmed"],
    ["11:00","Vocal Booth","Dev Patel","Ines Calloway","Vocal overdubs","confirmed"],
    ["12:00",null],
    ["13:00","Studio B","Jonas Reid","North Pier","Mixing session","hold"],
    ["14:00","Studio B","Jonas Reid","North Pier","Mixing session","confirmed"],
    ["15:00","Studio A","Dev Patel","Low Tide Radio","Drum tracking","confirmed"],
    ["16:00","Studio A","Dev Patel","Low Tide Radio","Drum tracking","hold"],
    ["17:00",null],
    ["18:00","Vocal Booth","Maya Ortiz","Sam Okafor","Podcast VO","confirmed"]
  ].map(([time, room, eng, client, project, status], i) => ({ id: i, time, room, eng, client, project, status: status || "open" }));

  const $ = id => document.getElementById(id);
  const end = t => String(+t.slice(0,2) + 1).padStart(2, "0") + ":00";
  const cap = w => w[0].toUpperCase() + w.slice(1);
  let selected = 0;

  function matches(s) {
    const r = $("f-room").value, e = $("f-eng").value;
    if (!s.room) return !r && !e;
    return (!r || s.room === r) && (!e || s.eng === e);
  }

  function renderRows() {
    $("rows").innerHTML = slots.map(s => `
      <li><button class="row ${s.room ? "" : "free"} ${matches(s) ? "" : "dim"}" data-id="${s.id}" aria-pressed="${s.id === selected}">
        <span class="time">${s.time}–${end(s.time)}</span>
        <span class="what"><span>${s.room ? s.client : "Available"}</span><span class="sub">${s.room ? s.project + " · " + s.room : "Open slot"}</span></span>
        <span class="eng">${s.eng || ""}</span>
        <span class="tag ${s.status}">${cap(s.status)}</span>
      </button></li>`).join("");
  }

  function renderSummary() {
    const s = slots[selected];
    $("summary").innerHTML = s.room ? `
      <div class="block"><h2>Selected booking</h2>
        <h3>${s.client}</h3>
        <span class="sub">${s.project}</span></div>
      <div class="block"><dl>
        <dt>Time</dt><dd>${s.time}–${end(s.time)}</dd>
        <dt>Room</dt><dd>${s.room}</dd>
        <dt>Engineer</dt><dd>${s.eng}</dd>
        <dt>Status</dt><dd class="${s.status}">${cap(s.status)}</dd></dl></div>
      <div class="block"><dl>
        <dt>Rate</dt><dd>$${RATE[s.room]}/hr</dd>
        <dt>Engineer fee</dt><dd>$40</dd>
        <dt class="total">Total</dt><dd class="total">$${RATE[s.room] + 40}</dd></dl></div>
      <p class="notes">Client supplies own instruments. Load-in from 30 min before start.</p>
      <div class="actions"><button class="btn">Reschedule</button><button class="btn primary">${s.status === "hold" ? "Confirm" : "Edit"}</button></div>`
    : `
      <div class="block"><h2>Selected booking</h2><h3>${s.time}–${end(s.time)} is open</h3>
        <span class="sub">No booking in this slot.</span></div>
      <div class="actions"><button class="btn primary">Book this slot</button></div>`;
  }

  function renderStats() {
    const b = slots.filter(s => s.room);
    $("st-booked").textContent = b.length;
    $("st-holds").textContent = b.filter(s => s.status === "hold").length;
    $("st-rev").textContent = "$" + b.filter(s => s.status === "confirmed").reduce((n, s) => n + RATE[s.room] + 40, 0);
  }

  function renderDate() {
    const d = new Date($("f-date").value + "T12:00:00");
    $("day-label").textContent = isNaN(d) ? "" : d.toLocaleDateString(undefined, { weekday: "long", month: "short", day: "numeric" });
  }

  $("rows").addEventListener("click", e => {
    const b = e.target.closest(".row"); if (!b) return;
    selected = +b.dataset.id; renderRows(); renderSummary();
  });
  ["f-room","f-eng"].forEach(id => $(id).addEventListener("change", renderRows));
  $("f-date").addEventListener("change", renderDate);
  $("reset").addEventListener("click", () => {
    $("f-room").value = ""; $("f-eng").value = ""; $("f-date").value = "2026-10-15"; renderRows(); renderDate();
  });

  renderRows(); renderSummary(); renderStats(); renderDate();
</script>
</body>
</html>
```

**Layout**
- **Header:** the title plus three live counts: booked slots, holds and confirmed revenue.
- **Filters:** date, room and engineer sit on one tinted bar, with Reset and New booking on the right. A tint is the only grouping device here because these controls need to read as one unit.
- **Schedule:** 10 hourly slots from 09:00 to 18:00 in a single list. Hairlines separate the rows, and each row is a button at least 44px tall. A row shows time, client, project and room, engineer, and a status marker (confirmed, hold or open). Choosing a room or engineer dims the rows that don't match.
- **Summary:** a sticky 300px column for the selected booking. Its sections are separated by space and headings rather than nested boxes, and the pricing block ends in a ruled total. Open slots show a "Book this slot" prompt instead.

**Spacing**
- Every gap and padding comes from a 4px-based scale.
- Spacing inside a group is smaller than spacing between groups.
- The row density is compact on purpose, since this is a daily-use tool.

**Behavior**
- Below 800px the summary stacks under the schedule and the engineer column hides.
- The bookings are made-up sample data, defined in the `slots` array in the script.
