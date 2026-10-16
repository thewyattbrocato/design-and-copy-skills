I couldn't save the file. The Write tool is disabled in this session, and Read and Skill are the only tools I have. The full HTML is below, so you can save it as `studio-booking.html` and open it. I haven't opened it in a browser, so the layout is untested.

Design choices:
- **Filters:** one tinted strip across the top, since the controls work as a unit.
- **Schedule:** a single bordered list with hairline rules between the 10 slots. Each slot is a button.
- **Summary:** a side column of small groups separated by space, with one rule between groups.
- **Spacing:** every gap and padding comes from a 4/8/12/16/24/32 px scale. Space inside a group is smaller than space between groups.
- **Interaction:** clicking a slot updates the summary, and the 14:00 slot is selected on load.
- **Narrow screens:** below 820 px the summary stacks under the schedule.

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
    --bg: #f3f4f6; --surface: #fff; --tint: #e9ecf0; --line: #dde1e6;
    --text: #1b1f24; --muted: #5f6b7a; --accent: #2457d6; --accent-bg: #e8eefc;
    --booked: #2457d6; --hold: #b26a00; --open: #5f6b7a; --blocked: #8a929e;
    --radius: 4px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 13px; line-height: 20px; color: var(--text);
  }
  * { box-sizing: border-box; }
  body { margin: 0; background: var(--bg); }
  .app { max-width: 1120px; margin: 0 auto; padding: var(--s5); display: grid; gap: var(--s4); }
  header { display: flex; align-items: baseline; justify-content: space-between; gap: var(--s4); }
  h1 { margin: 0; font-size: 18px; line-height: 24px; font-weight: 650; }
  h2 { margin: 0; font-size: 11px; line-height: 16px; letter-spacing: .06em; text-transform: uppercase; color: var(--muted); font-weight: 600; }
  .meta { color: var(--muted); }

  .filters { display: flex; flex-wrap: wrap; align-items: flex-end; gap: var(--s4); padding: var(--s3) var(--s4); background: var(--tint); border-radius: var(--radius); }
  .field { display: grid; gap: var(--s1); }
  .field label { font-size: 11px; line-height: 16px; font-weight: 600; color: var(--muted); }
  select, input[type=date], button { font: inherit; color: inherit; height: 32px; padding: 0 var(--s3); border: 1px solid var(--line); border-radius: var(--radius); background: var(--surface); }
  select { min-width: 150px; }
  button { cursor: pointer; padding: 0 var(--s4); }
  button.primary { background: var(--accent); border-color: var(--accent); color: #fff; font-weight: 600; }
  .filters .spacer { flex: 1; }
  :focus-visible { outline: 2px solid var(--accent); outline-offset: 1px; }

  .main { display: grid; grid-template-columns: minmax(0, 1fr) 300px; gap: var(--s5); align-items: start; }

  .schedule { background: var(--surface); border: 1px solid var(--line); border-radius: var(--radius); }
  .schedule-head { display: flex; justify-content: space-between; align-items: center; padding: var(--s3) var(--s4); border-bottom: 1px solid var(--line); }
  .legend { display: flex; gap: var(--s3); color: var(--muted); font-size: 12px; }
  .legend span::before { content: ""; display: inline-block; width: 8px; height: 8px; border-radius: 50%; margin-right: var(--s1); background: var(--c); }
  ul { list-style: none; margin: 0; padding: 0; }
  .slot { display: grid; grid-template-columns: 96px minmax(0, 1fr) auto; align-items: center; column-gap: var(--s4); width: 100%; min-height: 44px; height: auto; padding: var(--s2) var(--s4); border: 0; border-radius: 0; border-top: 1px solid var(--line); background: transparent; text-align: left; }
  li:first-child .slot { border-top: 0; }
  .slot:hover { background: #f7f8fa; }
  .slot[aria-pressed=true] { background: var(--accent-bg); box-shadow: inset 3px 0 0 var(--accent); }
  .time { font-variant-numeric: tabular-nums; color: var(--muted); }
  .what { display: grid; min-width: 0; }
  .what strong { font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .what span { color: var(--muted); font-size: 12px; line-height: 16px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .slot.open .what strong, .slot.blocked .what strong { color: var(--muted); font-weight: 400; }
  .badge { font-size: 11px; line-height: 16px; font-weight: 600; padding: 0 var(--s2); border-radius: 8px; color: var(--c); border: 1px solid currentColor; }

  aside { display: grid; gap: var(--s4); }
  .summary { background: var(--surface); border: 1px solid var(--line); border-radius: var(--radius); padding: var(--s4); display: grid; gap: var(--s4); }
  .summary-title { display: grid; gap: var(--s1); }
  .summary-title .name { font-size: 16px; line-height: 24px; font-weight: 650; }
  dl { margin: 0; display: grid; grid-template-columns: auto 1fr; gap: var(--s1) var(--s4); }
  dt { color: var(--muted); }
  dd { margin: 0; text-align: right; font-variant-numeric: tabular-nums; }
  .group { display: grid; gap: var(--s2); }
  .group + .group { padding-top: var(--s4); border-top: 1px solid var(--line); }
  .notes { margin: 0; }
  .actions { display: flex; gap: var(--s2); }
  .actions button { flex: 1; }
  .total dd { font-weight: 650; }

  @media (max-width: 820px) {
    .app { padding: var(--s4); }
    .main { grid-template-columns: 1fr; }
    .filters .spacer { display: none; }
  }
</style>
</head>
<body>
<div class="app">
  <header>
    <h1>Studio Bookings</h1>
    <span class="meta">4 booked · 2 holds · 3 open · 1 blocked</span>
  </header>

  <form class="filters" onsubmit="return false">
    <div class="field"><label for="date">Date</label><input id="date" type="date" value="2026-10-15"></div>
    <div class="field"><label for="room">Room</label>
      <select id="room"><option>Studio A — Tracking</option><option>Studio B — Mix</option><option>Studio C — Vocal</option><option>All rooms</option></select></div>
    <div class="field"><label for="eng">Engineer</label>
      <select id="eng"><option>Any engineer</option><option>Dana Ortiz</option><option>Marcus Lee</option><option>Priya Nair</option></select></div>
    <div class="spacer"></div>
    <button type="reset">Reset</button>
    <button class="primary" type="submit">New booking</button>
  </form>

  <div class="main">
    <section class="schedule" aria-labelledby="sched-h">
      <div class="schedule-head">
        <h2 id="sched-h">Thu 15 Oct · Studio A</h2>
        <div class="legend">
          <span style="--c:var(--booked)">Booked</span>
          <span style="--c:var(--hold)">Hold</span>
          <span style="--c:var(--open)">Open</span>
        </div>
      </div>
      <ul id="slots"></ul>
    </section>

    <aside>
      <section class="summary" aria-live="polite">
        <div class="group summary-title">
          <h2>Selected booking</h2>
          <div class="name" id="s-client"></div>
          <div class="meta" id="s-project"></div>
        </div>
        <div class="group">
          <dl>
            <dt>Status</dt><dd id="s-status"></dd>
            <dt>Time</dt><dd id="s-time"></dd>
            <dt>Room</dt><dd>Studio A</dd>
            <dt>Engineer</dt><dd id="s-eng"></dd>
          </dl>
        </div>
        <div class="group">
          <dl class="total">
            <dt>Rate</dt><dd id="s-rate"></dd>
            <dt>Total</dt><dd id="s-total"></dd>
          </dl>
        </div>
        <div class="group">
          <h2>Notes</h2>
          <p class="notes" id="s-notes"></p>
        </div>
        <div class="actions">
          <button>Reschedule</button>
          <button class="primary" id="s-action">Check in</button>
        </div>
      </section>
    </aside>
  </div>
</div>

<script>
  const slots = [
    ["09:00","10:00","booked","Harbor Lights","EP tracking — drums","Dana Ortiz",90,"Bring own snare. Click track at 112 bpm."],
    ["10:00","11:00","booked","Harbor Lights","EP tracking — bass","Dana Ortiz",90,"Same setup as previous hour; no teardown."],
    ["11:00","12:00","hold","M. Okafor","Vocal demo","Priya Nair",75,"Hold expires 17:00 today pending deposit."],
    ["12:00","13:00","blocked","Maintenance","Console recalibration","—",0,"Internal block. Do not book."],
    ["13:00","14:00","open","Available","","—",90,""],
    ["14:00","15:00","booked","Velvet Static","Mixing session","Marcus Lee",110,"Stems delivered via shared drive. Reference track attached."],
    ["15:00","16:00","booked","Velvet Static","Mixing session","Marcus Lee",110,"Revisions to chorus vocals."],
    ["16:00","17:00","hold","Juno & Co.","Podcast pilot","Priya Nair",75,"Awaiting confirmation of guest count."],
    ["17:00","18:00","open","Available","","—",90,""],
    ["18:00","19:00","open","Available","","—",90,""]
  ];
  const label = {booked:"Booked",hold:"Hold",open:"Open",blocked:"Blocked"};
  const color = {booked:"var(--booked)",hold:"var(--hold)",open:"var(--open)",blocked:"var(--blocked)"};
  const list = document.getElementById("slots");
  const $ = id => document.getElementById(id);

  function select(i) {
    const [a,b,st,client,proj,eng,rate,notes] = slots[i];
    list.querySelectorAll(".slot").forEach((el,j) => el.setAttribute("aria-pressed", j===i));
    $("s-client").textContent = client;
    $("s-project").textContent = proj || "No project";
    $("s-status").textContent = label[st];
    $("s-time").textContent = a + "–" + b;
    $("s-eng").textContent = eng;
    $("s-rate").textContent = rate ? "$" + rate + " / hr" : "—";
    $("s-total").textContent = rate ? "$" + rate : "—";
    $("s-notes").textContent = notes || "No notes.";
    $("s-action").textContent = st==="open" ? "Book slot" : st==="hold" ? "Confirm" : "Check in";
  }

  slots.forEach((s,i) => {
    const li = document.createElement("li");
    li.innerHTML = `<button class="slot ${s[2]}" aria-pressed="false" style="--c:${color[s[2]]}">
      <span class="time">${s[0]}–${s[1]}</span>
      <span class="what"><strong>${s[3]}</strong>${s[4] ? `<span>${s[4]} · ${s[5]}</span>` : ""}</span>
      <span class="badge">${label[s[2]]}</span></button>`;
    li.firstElementChild.addEventListener("click", () => select(i));
    list.appendChild(li);
  });
  select(5);
</script>
</body>
</html>
```

The filters are visual only. The date, room and engineer controls don't change the schedule, and the slot data is hardcoded sample data. If you enable Write, I can save the file. I can also wire the filters to the data.
