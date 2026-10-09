I couldn't save the file. The Write tool is disabled in this session, and I have no other way to create files. Here is the full contents, so you can save it as `studio-booking.html`. I haven't opened it in a browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Studio Bookings</title>
<style>
  :root {
    --bg: #f4f5f7; --panel: #ffffff; --ink: #1b1f27; --muted: #667085; --line: #e2e5ea;
    --accent: #2f5bea; --accent-bg: #eaf0ff;
    --ok: #17803d; --ok-bg: #e4f5ea;
    --warn: #a15c00; --warn-bg: #fdf0d9;
    --off: #667085; --off-bg: #eef0f3;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #14161a; --panel: #1c1f25; --ink: #e8eaee; --muted: #9aa1ad; --line: #2c3038;
      --accent: #7a9bff; --accent-bg: #222c4a;
      --ok: #5fd08a; --ok-bg: #16301f; --warn: #f0b45a; --warn-bg: #3a2a10;
      --off: #9aa1ad; --off-bg: #262a31;
    }
  }
  * { box-sizing: border-box; }
  body { margin: 0; padding: 16px; background: var(--bg); color: var(--ink);
    font: 13px/1.4 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; }
  .app { max-width: 1100px; margin: 0 auto; display: grid; gap: 12px; }
  header { display: flex; align-items: baseline; justify-content: space-between; }
  h1 { font-size: 16px; margin: 0; }
  header span { color: var(--muted); font-size: 12px; }
  .panel { background: var(--panel); border: 1px solid var(--line); border-radius: 8px; }

  .filters { display: grid; grid-template-columns: repeat(3, 1fr) auto; gap: 12px; padding: 10px 12px; align-items: end; }
  label { display: grid; gap: 3px; font-size: 11px; font-weight: 600; color: var(--muted); text-transform: uppercase; letter-spacing: .04em; }
  select, input[type=date], button { font: inherit; color: var(--ink); background: var(--panel);
    border: 1px solid var(--line); border-radius: 6px; padding: 6px 8px; height: 32px; }
  select, input { text-transform: none; letter-spacing: 0; font-weight: 400; }
  button { cursor: pointer; }
  button:hover { background: var(--bg); }
  :focus-visible { outline: 2px solid var(--accent); outline-offset: 1px; }

  .main { display: grid; grid-template-columns: 1fr 300px; gap: 12px; align-items: start; }

  .sched-head, .slot { display: grid; grid-template-columns: 56px 100px 1fr 110px 86px; gap: 10px; align-items: center; padding: 0 12px; }
  .sched-head { height: 30px; font-size: 11px; font-weight: 600; color: var(--muted); text-transform: uppercase; letter-spacing: .04em; border-bottom: 1px solid var(--line); }
  .slot { width: 100%; height: 44px; border: 0; border-bottom: 1px solid var(--line); border-radius: 0; background: transparent; text-align: left; }
  .slot:last-child { border-bottom: 0; border-radius: 0 0 8px 8px; }
  .slot:hover { background: var(--bg); }
  .slot[aria-pressed=true] { background: var(--accent-bg); box-shadow: inset 3px 0 0 var(--accent); }
  .slot[hidden] { display: none; }
  .time { font-variant-numeric: tabular-nums; font-weight: 600; }
  .client { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .client small { display: block; color: var(--muted); font-size: 11px; }
  .open .client { color: var(--muted); font-style: italic; }
  .muted { color: var(--muted); }

  .tag { display: inline-block; padding: 1px 8px; border-radius: 99px; font-size: 11px; font-weight: 600; text-align: center; }
  .confirmed { color: var(--ok); background: var(--ok-bg); }
  .hold { color: var(--warn); background: var(--warn-bg); }
  .free { color: var(--off); background: var(--off-bg); }
  .empty { padding: 24px; text-align: center; color: var(--muted); }

  .summary { padding: 14px; position: sticky; top: 16px; }
  .summary h2 { font-size: 11px; margin: 0 0 8px; color: var(--muted); text-transform: uppercase; letter-spacing: .04em; }
  .summary .title { font-size: 15px; font-weight: 600; margin-bottom: 2px; }
  dl { display: grid; grid-template-columns: 80px 1fr; gap: 6px 10px; margin: 12px 0; }
  dt { color: var(--muted); }
  dd { margin: 0; font-variant-numeric: tabular-nums; }
  .total { display: flex; justify-content: space-between; padding-top: 10px; border-top: 1px solid var(--line); font-weight: 600; }
  .actions { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-top: 12px; }
  .actions .primary { background: var(--accent); border-color: var(--accent); color: #fff; }
  .notes { margin: 12px 0 0; padding: 8px 10px; background: var(--bg); border-radius: 6px; color: var(--muted); font-size: 12px; }

  @media (max-width: 820px) {
    .filters { grid-template-columns: 1fr 1fr; }
    .main { grid-template-columns: 1fr; }
    .summary { position: static; }
    .sched-head, .slot { grid-template-columns: 50px 80px 1fr 80px; }
    .sched-head span:nth-child(4), .slot > :nth-child(4) { display: none; }
  }
</style>
</head>
<body>
<div class="app">
  <header>
    <h1>Studio Bookings</h1>
    <span id="stats"></span>
  </header>

  <section class="panel filters" aria-label="Filters">
    <label>Date <input type="date" id="f-date" value="2026-10-05"></label>
    <label>Room
      <select id="f-room">
        <option value="">All rooms</option>
        <option>Studio A</option><option>Studio B</option><option>Live Room</option><option>Vocal Booth</option>
      </select>
    </label>
    <label>Engineer
      <select id="f-eng">
        <option value="">All engineers</option>
        <option>Maya Ortiz</option><option>Dev Patel</option><option>Sam Keller</option>
      </select>
    </label>
    <button type="button" id="reset">Reset</button>
  </section>

  <div class="main">
    <section class="panel" aria-label="Day schedule">
      <div class="sched-head"><span>Time</span><span>Room</span><span>Session</span><span>Engineer</span><span>Status</span></div>
      <div id="list"></div>
      <div class="empty" id="empty" hidden>No slots match these filters.</div>
    </section>

    <aside class="panel summary" aria-live="polite">
      <h2>Selected booking</h2>
      <div id="detail"></div>
    </aside>
  </div>
</div>

<script>
  const slots = [
    { t: "09:00", room: "Studio A",    who: "Northline — vocal tracking", type: "Tracking",  eng: "Maya Ortiz", s: "confirmed", rate: 95,  hrs: 2, contact: "j.hale@northline.example", note: "Bring 2 condenser mics; client arrives 08:45." },
    { t: "10:00", room: "Studio A",    who: "Northline — vocal tracking", type: "Tracking",  eng: "Maya Ortiz", s: "confirmed", rate: 95,  hrs: 2, contact: "j.hale@northline.example", note: "Continuation of 09:00 block." },
    { t: "11:00", room: "Vocal Booth", who: "Podcast: Low Tide ep. 41",   type: "Voiceover", eng: "Sam Keller", s: "confirmed", rate: 60,  hrs: 1, contact: "lowtide@example.com",      note: "Two hosts, one guest mic." },
    { t: "12:00", room: "Studio B",    who: "", type: "", eng: "", s: "free", rate: 80, hrs: 1 },
    { t: "13:00", room: "Live Room",   who: "The Parkers — band session", type: "Live",      eng: "Dev Patel",  s: "hold",      rate: 140, hrs: 3, contact: "mgmt@theparkers.example",  note: "Deposit pending. Release hold if unpaid by 12:00." },
    { t: "14:00", room: "Live Room",   who: "The Parkers — band session", type: "Live",      eng: "Dev Patel",  s: "hold",      rate: 140, hrs: 3, contact: "mgmt@theparkers.example",  note: "Drum kit pre-mic'd." },
    { t: "15:00", room: "Studio B",    who: "R. Amani — mixing",          type: "Mixing",    eng: "Maya Ortiz", s: "confirmed", rate: 80,  hrs: 2, contact: "r.amani@example.com",      note: "Stems delivered via shared drive." },
    { t: "16:00", room: "Studio B",    who: "R. Amani — mixing",          type: "Mixing",    eng: "Maya Ortiz", s: "confirmed", rate: 80,  hrs: 2, contact: "r.amani@example.com",      note: "Reference tracks on file." },
    { t: "17:00", room: "Vocal Booth", who: "", type: "", eng: "", s: "free", rate: 60, hrs: 1 },
    { t: "18:00", room: "Studio A",    who: "Kite & Key — overdubs",      type: "Tracking",  eng: "Sam Keller", s: "confirmed", rate: 95,  hrs: 1, contact: "kitekey@example.com",      note: "Guitar overdubs only." },
  ];
  const labels = { confirmed: "Confirmed", hold: "On hold", free: "Open" };
  const $ = id => document.getElementById(id);
  const money = n => "$" + n.toLocaleString();
  const end = t => String(+t.slice(0, 2) + 1).padStart(2, "0") + ":00";
  let selected = 0;

  $("list").innerHTML = slots.map((x, i) => `
    <button type="button" class="slot ${x.s === "free" ? "open" : ""}" data-i="${i}" aria-pressed="false">
      <span class="time">${x.t}</span>
      <span>${x.room}</span>
      <span class="client">${x.who || "Available"}${x.type ? `<small>${x.type}</small>` : ""}</span>
      <span class="${x.eng ? "" : "muted"}">${x.eng || "—"}</span>
      <span class="tag ${x.s}">${labels[x.s]}</span>
    </button>`).join("");

  function detail() {
    const x = slots[selected];
    if (x.s === "free") {
      $("detail").innerHTML = `
        <div class="title">Open slot</div>
        <div class="muted">${x.room} · ${x.t}–${end(x.t)}</div>
        <dl><dt>Rate</dt><dd>${money(x.rate)}/hr</dd></dl>
        <div class="actions"><button type="button" class="primary" style="grid-column:1/-1">Create booking</button></div>`;
      return;
    }
    $("detail").innerHTML = `
      <div class="title">${x.who}</div>
      <span class="tag ${x.s}">${labels[x.s]}</span>
      <dl>
        <dt>Date</dt><dd>${$("f-date").value}</dd>
        <dt>Time</dt><dd>${x.t}–${end(x.t)}</dd>
        <dt>Room</dt><dd>${x.room}</dd>
        <dt>Engineer</dt><dd>${x.eng}</dd>
        <dt>Type</dt><dd>${x.type}</dd>
        <dt>Contact</dt><dd>${x.contact}</dd>
        <dt>Block</dt><dd>${x.hrs} hr</dd>
      </dl>
      <div class="total"><span>Rate ${money(x.rate)}/hr</span><span>${money(x.rate * x.hrs)}</span></div>
      <p class="notes">${x.note}</p>
      <div class="actions"><button type="button">Reschedule</button><button type="button" class="primary">${x.s === "hold" ? "Confirm" : "Check in"}</button></div>`;
  }

  function apply() {
    const room = $("f-room").value, eng = $("f-eng").value;
    let shown = 0, booked = 0;
    document.querySelectorAll(".slot").forEach(el => {
      const x = slots[el.dataset.i];
      const ok = (!room || x.room === room) && (!eng || x.eng === eng);
      el.hidden = !ok;
      el.setAttribute("aria-pressed", String(+el.dataset.i === selected));
      if (ok) { shown++; if (x.s !== "free") booked++; }
    });
    $("empty").hidden = shown > 0;
    $("stats").textContent = `${shown} slots · ${booked} booked · ${shown - booked} open`;
    detail();
  }

  $("list").addEventListener("click", e => {
    const b = e.target.closest(".slot");
    if (b) { selected = +b.dataset.i; apply(); }
  });
  ["f-date", "f-room", "f-eng"].forEach(id => $(id).addEventListener("change", apply));
  $("reset").addEventListener("click", () => {
    $("f-date").value = "2026-10-05"; $("f-room").value = ""; $("f-eng").value = ""; apply();
  });
  apply();
</script>
</body>
</html>
```

**Layout**
- **Filters:** a bar across the top with date, room and engineer, plus a Reset button.
- **Schedule:** ten hourly slots from 09:00 to 18:00. Each row shows time, room, session, engineer and a status tag (Confirmed, On hold or Open).
- **Summary:** a sticky panel on the right, 300px wide. It shows the selected booking's details, the rate and total, notes, and actions. An open slot shows a "Create booking" action instead.
- **Small screens:** below 820px the summary stacks under the schedule and the engineer column is hidden.

**Behavior**
- Clicking a row selects it and updates the summary.
- The room and engineer filters hide non-matching rows, and the header counts update to match.
- The date filter changes only the date shown in the summary. All the data is for a single day.
- All the bookings are placeholder data, and the buttons don't do anything yet.

The page uses system fonts and has no external assets. It follows the system dark/light setting. It also has a small inline script for selection and filtering.
