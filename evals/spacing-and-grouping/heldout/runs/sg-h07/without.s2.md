I couldn't save the file because the Write tool is disabled in this session. Here is the complete file instead. Save it as `booking-panel.html` and open it in a browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Studio Bookings</title>
<style>
  :root {
    --bg: #f4f5f7; --panel: #fff; --ink: #1b1f27; --muted: #6a7282; --line: #dfe3e9;
    --accent: #2f5fd0; --accent-soft: #e6edfb;
    --confirmed: #1f7a4d; --confirmed-bg: #e3f4ea;
    --pending: #9a6200; --pending-bg: #fdf0d5;
    --hold: #6b4bb3; --hold-bg: #eee8fa;
    --open: #8a92a1;
    --radius: 6px;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #14161a; --panel: #1c1f25; --ink: #e8eaee; --muted: #9099a8; --line: #2c313a;
      --accent: #7ba0f5; --accent-soft: #232f4d;
      --confirmed: #5fd093; --confirmed-bg: #17301f;
      --pending: #f0b84e; --pending-bg: #3a2d12;
      --hold: #b9a3f0; --hold-bg: #2a2342;
      --open: #707888;
    }
  }
  * { box-sizing: border-box; }
  body {
    margin: 0; background: var(--bg); color: var(--ink);
    font: 13px/1.4 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  }
  .app { max-width: 1180px; margin: 0 auto; padding: 14px; display: grid; gap: 12px; }
  header { display: flex; align-items: baseline; justify-content: space-between; }
  h1 { font-size: 16px; margin: 0; font-weight: 650; }
  .sub { color: var(--muted); font-size: 12px; }
  .panel { background: var(--panel); border: 1px solid var(--line); border-radius: var(--radius); }

  /* Filters */
  .filters { display: flex; flex-wrap: wrap; gap: 12px; align-items: end; padding: 10px 12px; }
  .field { display: grid; gap: 3px; }
  .field label { font-size: 11px; text-transform: uppercase; letter-spacing: .05em; color: var(--muted); }
  select, input[type=date], button {
    font: inherit; color: var(--ink); background: var(--panel);
    border: 1px solid var(--line); border-radius: 4px; padding: 5px 8px; height: 30px;
  }
  button { cursor: pointer; }
  button:hover { border-color: var(--accent); }
  button.primary { background: var(--accent); border-color: var(--accent); color: #fff; font-weight: 600; }
  :focus-visible { outline: 2px solid var(--accent); outline-offset: 1px; }
  .filters .spacer { flex: 1; }
  .daynav { display: flex; gap: 4px; }

  /* Main grid */
  .main { display: grid; grid-template-columns: minmax(0, 1fr) 300px; gap: 12px; align-items: start; }
  @media (max-width: 820px) { .main { grid-template-columns: 1fr; } }

  /* Schedule */
  .sched-head { display: flex; justify-content: space-between; align-items: center; padding: 9px 12px; border-bottom: 1px solid var(--line); }
  .sched-head strong { font-size: 13px; }
  .legend { display: flex; gap: 10px; font-size: 11px; color: var(--muted); }
  .dot { display: inline-block; width: 8px; height: 8px; border-radius: 50%; margin-right: 4px; }
  .cols, .slot {
    display: grid; grid-template-columns: 78px 92px minmax(0, 1.4fr) minmax(0, 1fr) 84px;
    gap: 8px; align-items: center; padding: 0 12px;
  }
  .cols { font-size: 11px; text-transform: uppercase; letter-spacing: .05em; color: var(--muted); height: 26px; border-bottom: 1px solid var(--line); }
  ul { list-style: none; margin: 0; padding: 0; }
  .slot { height: 44px; border-bottom: 1px solid var(--line); cursor: pointer; border-left: 3px solid transparent; }
  .slot:last-child { border-bottom: 0; }
  .slot:hover { background: color-mix(in srgb, var(--accent-soft) 50%, transparent); }
  .slot[aria-selected=true] { background: var(--accent-soft); border-left-color: var(--accent); }
  .time { font-variant-numeric: tabular-nums; font-weight: 600; }
  .time small { display: block; font-weight: 400; color: var(--muted); font-size: 11px; }
  .room, .eng { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .client { overflow: hidden; }
  .client b, .client span { display: block; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .client span { color: var(--muted); font-size: 12px; }
  .slot.open .client b, .slot.open .eng, .slot.open .room { color: var(--open); font-weight: 400; }
  .badge { justify-self: end; font-size: 11px; font-weight: 600; padding: 2px 7px; border-radius: 10px; white-space: nowrap; }
  .b-confirmed { color: var(--confirmed); background: var(--confirmed-bg); }
  .b-pending { color: var(--pending); background: var(--pending-bg); }
  .b-hold { color: var(--hold); background: var(--hold-bg); }
  .b-open { color: var(--open); border: 1px dashed var(--line); }
  @media (max-width: 560px) {
    .cols { display: none; }
    .slot { grid-template-columns: 62px 1fr auto; height: 52px; }
    .slot .room, .slot .eng { display: none; }
  }

  /* Summary */
  aside { position: sticky; top: 12px; }
  .sum-head { padding: 12px; border-bottom: 1px solid var(--line); display: grid; gap: 4px; }
  .sum-head .badge { justify-self: start; }
  .sum-head h2 { margin: 0; font-size: 15px; }
  dl { margin: 0; padding: 4px 12px; display: grid; grid-template-columns: 84px 1fr; }
  dt, dd { margin: 0; padding: 6px 0; border-bottom: 1px solid var(--line); }
  dt { color: var(--muted); font-size: 12px; }
  dd { font-variant-numeric: tabular-nums; }
  dt:nth-last-of-type(1), dd:last-of-type { border-bottom: 0; }
  .notes { margin: 0 12px 12px; padding: 8px 10px; background: var(--bg); border-radius: 4px; font-size: 12px; color: var(--muted); }
  .actions { display: flex; gap: 6px; padding: 0 12px 12px; }
  .actions button { flex: 1; }
</style>
</head>
<body>
<div class="app">
  <header>
    <h1>Studio Bookings</h1>
    <span class="sub">Control panel · 4 rooms · 5 engineers</span>
  </header>

  <section class="panel filters" aria-label="Filters">
    <div class="field">
      <label for="f-date">Date</label>
      <div class="daynav">
        <button type="button" aria-label="Previous day">‹</button>
        <input id="f-date" type="date" value="2026-10-15">
        <button type="button" aria-label="Next day">›</button>
      </div>
    </div>
    <div class="field">
      <label for="f-room">Room</label>
      <select id="f-room">
        <option>All rooms</option><option>Studio A – Live Room</option>
        <option>Studio B – Mix Suite</option><option>Studio C – Vocal Booth</option><option>Studio D – Podcast</option>
      </select>
    </div>
    <div class="field">
      <label for="f-eng">Engineer</label>
      <select id="f-eng">
        <option>All engineers</option><option>Dana Reyes</option><option>Marcus Lee</option>
        <option>Priya Nair</option><option>Tom Okafor</option><option>Sam Whitfield</option>
      </select>
    </div>
    <div class="spacer"></div>
    <button type="button">Reset</button>
    <button type="button" class="primary">+ New booking</button>
  </section>

  <div class="main">
    <section class="panel" aria-label="Day schedule">
      <div class="sched-head">
        <strong>Thursday, Oct 15 · 7 of 10 slots booked</strong>
        <div class="legend">
          <span><i class="dot" style="background:var(--confirmed)"></i>Confirmed</span>
          <span><i class="dot" style="background:var(--pending)"></i>Pending</span>
          <span><i class="dot" style="background:var(--hold)"></i>Hold</span>
        </div>
      </div>
      <div class="cols" aria-hidden="true"><span>Time</span><span>Room</span><span>Client / project</span><span>Engineer</span><span style="text-align:right">Status</span></div>
      <ul id="slots" role="listbox" aria-label="Time slots"></ul>
    </section>

    <aside class="panel" aria-label="Selected booking" aria-live="polite">
      <div class="sum-head">
        <span class="badge" id="s-badge"></span>
        <h2 id="s-title"></h2>
        <span class="sub" id="s-sub"></span>
      </div>
      <dl id="s-details"></dl>
      <p class="notes" id="s-notes"></p>
      <div class="actions">
        <button type="button">Reschedule</button>
        <button type="button" class="primary" id="s-primary">Confirm</button>
      </div>
    </aside>
  </div>
</div>

<script>
  const S = [
    ["09:00","10:00","Studio A","Neon Harbor","Album tracking – drums","Dana Reyes","confirmed","$180/hr",4,"Kit mics pre-set from yesterday."],
    ["10:00","11:00","Studio A","Neon Harbor","Album tracking – bass","Dana Reyes","confirmed","$180/hr",4,"Bring DI + amp. Load-in 09:45."],
    ["11:00","12:00","Studio C","Lucia Marsh","Vocal overdubs","Priya Nair","pending","$95/hr",1,"Deposit not yet received."],
    ["12:00","13:00",null],
    ["13:00","14:00","Studio B","Kite & Crow","Mixing – single","Marcus Lee","confirmed","$120/hr",2,"Stems delivered via shared drive."],
    ["14:00","15:00","Studio B","Kite & Crow","Mixing – single","Marcus Lee","confirmed","$120/hr",2,"Continuation of 13:00 session."],
    ["15:00","16:00","Studio D","Late Shift Pod","Episode 42 recording","Tom Okafor","hold","$70/hr",3,"Held until Oct 16 noon."],
    ["16:00","17:00",null],
    ["17:00","18:00","Studio A","Ruben Cole","Guitar re-amp","Sam Whitfield","pending","$180/hr",1,"Awaiting engineer confirmation."],
    ["18:00","19:00",null]
  ];
  const label = {confirmed:"Confirmed", pending:"Pending", hold:"Hold", open:"Open"};
  const list = document.getElementById("slots");
  const $ = id => document.getElementById(id);

  S.forEach((s, i) => {
    const open = !s[2], st = open ? "open" : s[6];
    const li = document.createElement("li");
    li.className = "slot" + (open ? " open" : "");
    li.setAttribute("role", "option");
    li.tabIndex = 0;
    li.innerHTML = `<span class="time">${s[0]}<small>to ${s[1]}</small></span>
      <span class="room">${open ? "—" : s[2]}</span>
      <span class="client"><b>${open ? "Available" : s[3]}</b>${open ? "" : `<span>${s[4]}</span>`}</span>
      <span class="eng">${open ? "—" : s[5]}</span>
      <span class="badge b-${st}">${label[st]}</span>`;
    li.onclick = () => select(i);
    li.onkeydown = e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); select(i); } };
    list.appendChild(li);
  });

  function select(i) {
    [...list.children].forEach((el, j) => el.setAttribute("aria-selected", i === j));
    const s = S[i], open = !s[2], st = open ? "open" : s[6];
    $("s-badge").className = "badge b-" + st;
    $("s-badge").textContent = label[st];
    $("s-title").textContent = open ? "Open slot" : s[3];
    $("s-sub").textContent = open ? "Nothing booked" : s[4];
    const rows = open
      ? [["Date","Thu, Oct 15"],["Time",`${s[0]} – ${s[1]}`],["Room","Any available"]]
      : [["Date","Thu, Oct 15"],["Time",`${s[0]} – ${s[1]}`],["Room",s[2]],["Engineer",s[5]],
         ["Rate",s[7]],["Headcount",s[8] + (s[8] > 1 ? " people" : " person")]];
    $("s-details").innerHTML = rows.map(r => `<dt>${r[0]}</dt><dd>${r[1]}</dd>`).join("");
    $("s-notes").textContent = open ? "Click “New booking” to fill this slot." : s[9];
    $("s-primary").textContent = open ? "Book slot" : st === "confirmed" ? "Check in" : "Confirm";
  }
  select(2);
</script>
</body>
</html>
```

I haven't opened it in a browser, so the layout is untested.

- **Filters:** a bar across the top with a date picker and prev/next day buttons, room and engineer selects, Reset, and a "New booking" button. These controls are layout only. They don't filter the list yet.
- **Schedule:** 10 one-hour slots from 09:00 to 19:00. Each row shows time, room, client and project, engineer, and a status badge (confirmed, pending, hold, or open). The header has a color legend and a booked count. The cell content is placeholder data.
- **Summary:** a sticky side panel for the selected slot. It shows the status, client, a detail list, notes, and Reschedule and Confirm buttons. Clicking a row, or pressing Enter or Space on it, updates the panel. The 11:00 slot is selected when the page loads.
- **Styling:** system fonts only, no external assets, with light and dark themes that follow the OS setting. Below 820px the summary moves under the schedule. Below 560px the room and engineer columns are hidden.

If you enable Write, I can save it to the working directory.
