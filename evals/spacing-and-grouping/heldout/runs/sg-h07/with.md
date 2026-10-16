I couldn't save the file because the Write tool is disabled in this session. I haven't opened the page in a browser either. The full HTML is below, so you can save it as `studio-bookings.html`.

**Layout:**
- **Filters:** one tinted strip across the top with date, room and engineer, plus Reset and New booking. The controls work as a single unit, so they get one background.
- **Schedule:** one surface with 10 hourly rows, 09:00 to 18:00, separated by hairline rules. Each row shows time, title and client, engineer, and a status tag (Booked, Hold or Free). Rows are clickable and keyboard-selectable.
- **Summary:** a sticky 300px column holding the selected booking: status, client, time, room, engineer, contact, estimated total, notes, and Reschedule and Cancel buttons. It updates when you pick a row.
- **Spacing:** every gap comes from a 4px scale (4, 8, 12, 16, 24, 32). Space inside a group is smaller than space between groups, and there are no cards nested inside cards.
- **Narrow screens:** below 800px the summary drops under the schedule and the engineer column is hidden.

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
    --bg: #f4f5f7; --surface: #ffffff; --tint: #eceef2; --line: #dde0e6;
    --text: #1b1f27; --muted: #626b7a;
    --accent: #2f5fd0; --accent-bg: #e8eefc;
    --ok: #1f7a4d; --ok-bg: #e2f3ea;
    --hold: #94600a; --hold-bg: #fbf0d9;
    --off: #8a93a2;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 14px; line-height: 20px; color: var(--text);
  }
  * { box-sizing: border-box; }
  body { margin: 0; background: var(--bg); }
  .app { max-width: 1120px; margin: 0 auto; padding: var(--s5); display: grid; gap: var(--s4); }

  header { display: flex; align-items: baseline; justify-content: space-between; gap: var(--s4); }
  h1 { margin: 0; font-size: 18px; line-height: 24px; font-weight: 650; }
  .meta { color: var(--muted); font-size: 13px; }

  .filters { display: flex; flex-wrap: wrap; align-items: flex-end; gap: var(--s4);
    padding: var(--s3) var(--s4); background: var(--tint); border-radius: 6px; }
  .field { display: grid; gap: var(--s1); }
  .field label { font-size: 12px; line-height: 16px; font-weight: 600; color: var(--muted);
    text-transform: uppercase; letter-spacing: .04em; }
  select, input[type=date], button { font: inherit; color: inherit; height: 32px; padding: 0 var(--s3);
    border: 1px solid var(--line); border-radius: 4px; background: var(--surface); }
  select { min-width: 150px; }
  button { cursor: pointer; padding: 0 var(--s4); font-weight: 600; }
  button.primary { background: var(--accent); border-color: var(--accent); color: #fff; }
  button:focus-visible, select:focus-visible, input:focus-visible, .slot:focus-visible { outline: 2px solid var(--accent); outline-offset: 1px; }
  .filters .spacer { flex: 1; }

  .main { display: grid; grid-template-columns: minmax(0, 1fr) 300px; gap: var(--s5); align-items: start; }
  h2 { margin: 0; font-size: 12px; line-height: 16px; font-weight: 600; color: var(--muted);
    text-transform: uppercase; letter-spacing: .04em; }
  .section-head { display: flex; justify-content: space-between; align-items: baseline; padding-bottom: var(--s2); }

  .schedule { margin: 0; padding: 0; list-style: none; background: var(--surface);
    border: 1px solid var(--line); border-radius: 6px; overflow: hidden; }
  .slot { display: grid; grid-template-columns: 56px minmax(0, 1fr) 96px 88px; align-items: center; gap: var(--s3);
    min-height: 44px; padding: var(--s2) var(--s4); border-top: 1px solid var(--line);
    border-left: 3px solid transparent; cursor: pointer; }
  .slot:first-child { border-top: 0; }
  .slot:hover { background: #f8f9fb; }
  .slot[aria-selected=true] { background: var(--accent-bg); border-left-color: var(--accent); }
  .time { font-variant-numeric: tabular-nums; font-weight: 600; }
  .what { display: grid; min-width: 0; }
  .what b { font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .what span, .eng { color: var(--muted); font-size: 13px; line-height: 18px; }
  .slot.free .what b { color: var(--off); font-weight: 400; }
  .eng { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .tag { justify-self: end; font-size: 12px; line-height: 16px; font-weight: 600; padding: 2px var(--s2); border-radius: 3px; }
  .tag.ok { color: var(--ok); background: var(--ok-bg); }
  .tag.hold { color: var(--hold); background: var(--hold-bg); }
  .tag.free { color: var(--muted); background: var(--tint); }

  aside { position: sticky; top: var(--s5); background: var(--surface); border: 1px solid var(--line);
    border-radius: 6px; padding: var(--s4); display: grid; gap: var(--s4); }
  .title { display: grid; gap: var(--s1); }
  .title h3 { margin: 0; font-size: 16px; line-height: 22px; font-weight: 650; }
  dl { margin: 0; display: grid; grid-template-columns: 88px 1fr; gap: var(--s2) var(--s3); }
  dt { color: var(--muted); }
  dd { margin: 0; }
  .total { display: flex; justify-content: space-between; align-items: baseline; padding-top: var(--s3); border-top: 1px solid var(--line); }
  .total strong { font-size: 18px; line-height: 24px; font-variant-numeric: tabular-nums; }
  .notes { margin: 0; color: var(--muted); font-size: 13px; line-height: 18px; }
  .actions { display: flex; gap: var(--s2); }
  .actions button { flex: 1; }

  @media (max-width: 800px) {
    .app { padding: var(--s4); }
    .main { grid-template-columns: 1fr; gap: var(--s4); }
    aside { position: static; }
    .slot { grid-template-columns: 52px minmax(0, 1fr) 80px; }
    .slot .eng { display: none; }
  }
</style>
</head>
<body>
<div class="app">
  <header>
    <h1>Studio Bookings</h1>
    <span class="meta">6 booked · 1 hold · 3 open</span>
  </header>

  <form class="filters" aria-label="Filters" onsubmit="return false">
    <div class="field"><label for="date">Date</label><input id="date" type="date" value="2026-10-15"></div>
    <div class="field"><label for="room">Room</label>
      <select id="room"><option>All rooms</option><option selected>Studio A · Live room</option>
        <option>Studio B · Mix suite</option><option>Studio C · Vocal booth</option></select></div>
    <div class="field"><label for="eng">Engineer</label>
      <select id="eng"><option selected>Any engineer</option><option>Maya Ortiz</option>
        <option>Dev Patel</option><option>Lena Fischer</option></select></div>
    <span class="spacer"></span>
    <button type="reset">Reset</button>
    <button class="primary" type="submit">New booking</button>
  </form>

  <div class="main">
    <section aria-labelledby="sched-h">
      <div class="section-head"><h2 id="sched-h">Thu, Oct 15 · Studio A</h2><span class="meta">09:00 – 19:00</span></div>
      <ul class="schedule" role="listbox" aria-label="Day schedule">
        <li class="slot" role="option" tabindex="0" aria-selected="false" data-id="0"><span class="time">09:00</span><span class="what"><b>Strings overdub</b><span>Harlow Quartet</span></span><span class="eng">Maya Ortiz</span><span class="tag ok">Booked</span></li>
        <li class="slot" role="option" tabindex="0" aria-selected="false" data-id="1"><span class="time">10:00</span><span class="what"><b>Strings overdub</b><span>Harlow Quartet</span></span><span class="eng">Maya Ortiz</span><span class="tag ok">Booked</span></li>
        <li class="slot free" role="option" tabindex="0" aria-selected="false" data-id="2"><span class="time">11:00</span><span class="what"><b>Open</b></span><span class="eng">—</span><span class="tag free">Free</span></li>
        <li class="slot" role="option" tabindex="0" aria-selected="true" data-id="3"><span class="time">12:00</span><span class="what"><b>Drum tracking</b><span>The Late Edition</span></span><span class="eng">Dev Patel</span><span class="tag ok">Booked</span></li>
        <li class="slot" role="option" tabindex="0" aria-selected="false" data-id="4"><span class="time">13:00</span><span class="what"><b>Drum tracking</b><span>The Late Edition</span></span><span class="eng">Dev Patel</span><span class="tag ok">Booked</span></li>
        <li class="slot" role="option" tabindex="0" aria-selected="false" data-id="5"><span class="time">14:00</span><span class="what"><b>Drum tracking</b><span>The Late Edition</span></span><span class="eng">Dev Patel</span><span class="tag ok">Booked</span></li>
        <li class="slot" role="option" tabindex="0" aria-selected="false" data-id="6"><span class="time">15:00</span><span class="what"><b>Hold: podcast pilot</b><span>Northside Audio</span></span><span class="eng">Lena Fischer</span><span class="tag hold">Hold</span></li>
        <li class="slot free" role="option" tabindex="0" aria-selected="false" data-id="7"><span class="time">16:00</span><span class="what"><b>Open</b></span><span class="eng">—</span><span class="tag free">Free</span></li>
        <li class="slot" role="option" tabindex="0" aria-selected="false" data-id="8"><span class="time">17:00</span><span class="what"><b>Vocal session</b><span>J. Alvarez</span></span><span class="eng">Maya Ortiz</span><span class="tag ok">Booked</span></li>
        <li class="slot free" role="option" tabindex="0" aria-selected="false" data-id="9"><span class="time">18:00</span><span class="what"><b>Open</b></span><span class="eng">—</span><span class="tag free">Free</span></li>
      </ul>
    </section>

    <aside aria-labelledby="sum-h" aria-live="polite">
      <h2 id="sum-h">Selected booking</h2>
      <div class="title">
        <h3 id="s-title">Drum tracking</h3>
        <span class="tag ok" id="s-tag" style="justify-self:start">Booked</span>
      </div>
      <dl>
        <dt>Client</dt><dd id="s-client">The Late Edition</dd>
        <dt>Time</dt><dd id="s-time">12:00 – 15:00 (3 h)</dd>
        <dt>Room</dt><dd>Studio A · Live room</dd>
        <dt>Engineer</dt><dd id="s-eng">Dev Patel</dd>
        <dt>Contact</dt><dd>booking@lateedition.example</dd>
      </dl>
      <div class="total"><span class="meta">Estimated total</span><strong id="s-total">$540</strong></div>
      <p class="notes" id="s-notes">Full kit, 12 mics. Load-in from 11:30 via rear door.</p>
      <div class="actions"><button type="button">Reschedule</button><button type="button">Cancel</button></div>
    </aside>
  </div>
</div>

<script>
  const data = {
    0: ["Strings overdub","Harlow Quartet","09:00 – 11:00 (2 h)","Maya Ortiz","$360","ok","Booked","Four players, room mics only."],
    3: ["Drum tracking","The Late Edition","12:00 – 15:00 (3 h)","Dev Patel","$540","ok","Booked","Full kit, 12 mics. Load-in from 11:30 via rear door."],
    6: ["Hold: podcast pilot","Northside Audio","15:00 – 16:00 (1 h)","Lena Fischer","$120","hold","Hold","Awaiting deposit. Releases at 12:00 today."],
    8: ["Vocal session","J. Alvarez","17:00 – 18:00 (1 h)","Maya Ortiz","$150","ok","Booked","Bring reference track."]
  };
  const group = { 1:0, 2:null, 4:3, 5:3, 7:null, 9:null };
  const $ = id => document.getElementById(id);
  document.querySelectorAll('.slot').forEach(el => {
    const select = () => {
      document.querySelectorAll('.slot').forEach(s => s.setAttribute('aria-selected', s === el));
      const id = +el.dataset.id;
      const d = data[id in data ? id : group[id]];
      if (!d) {
        $('s-title').textContent = 'Open slot'; $('s-client').textContent = '—';
        $('s-time').textContent = el.querySelector('.time').textContent + ' (1 h)';
        $('s-eng').textContent = 'Unassigned'; $('s-total').textContent = '$0';
        $('s-tag').className = 'tag free'; $('s-tag').textContent = 'Free';
        $('s-notes').textContent = 'No booking. Use New booking to reserve this slot.';
        return;
      }
      $('s-title').textContent = d[0]; $('s-client').textContent = d[1];
      $('s-time').textContent = d[2]; $('s-eng').textContent = d[3];
      $('s-total').textContent = d[4];
      $('s-tag').className = 'tag ' + d[5]; $('s-tag').textContent = d[6];
      $('s-notes').textContent = d[7];
    };
    el.addEventListener('click', select);
    el.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); select(); } });
  });
</script>
</body>
</html>
```

The date, room and engineer filters are visual only and don't filter the list. The only script is the row-selection handler that updates the summary. If you re-enable Write, I can save the file directly.
