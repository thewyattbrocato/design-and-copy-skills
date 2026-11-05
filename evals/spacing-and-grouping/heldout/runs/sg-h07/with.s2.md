I couldn't save this to disk because the Write tool is disabled in this session, and I have no other way to create files. The full file is below. Save it as `studio-booking.html`. I haven't opened it in a browser.

The layout works like this:
- **Filters:** one tinted bar across the top with date (with prev/next buttons), room and engineer, plus Reset and New booking on the right.
- **Schedule:** a single bordered list of 10 hourly slots from 09:00 to 18:00. Rows are divided by hairlines, with a colored status bar and a quiet status label on each row.
- **Summary:** a sticky side panel for the selected booking. Clicking or pressing Enter on a row updates it.
- **Spacing:** every gap comes from a 4px scale (4, 8, 12, 16, 24, 32). The rows are compact (48px), but the gaps between the page sections are larger than the gaps inside them.
- **Status labels:** they are tinted text with no border, so they don't look like the buttons beside them.
- **Narrow screens:** below 860px the summary stacks under the schedule.

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
    --bg: #f3f4f6; --surface: #ffffff; --tint: #e9ecf0; --line: #dde0e6;
    --text: #1b1f27; --muted: #5d6573; --accent: #2f5fd0; --accent-soft: #e6edfc;
    --booked: #2f5fd0; --held: #b26a00; --open: #2b7a4b; --blocked: #6b7280;
    --font: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    --mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  }
  * { box-sizing: border-box; margin: 0; }
  body { font: 13px/20px var(--font); color: var(--text); background: var(--bg); padding: var(--s5); }
  .app { max-width: 1120px; margin: 0 auto; display: grid; gap: var(--s4); }

  header { display: flex; align-items: baseline; justify-content: space-between; gap: var(--s4); }
  h1 { font-size: 18px; line-height: 24px; font-weight: 650; }
  .sub { color: var(--muted); }
  .tally { display: flex; gap: var(--s4); color: var(--muted); font-variant-numeric: tabular-nums; }
  .tally b { color: var(--text); font-weight: 650; }

  .filters { display: flex; flex-wrap: wrap; align-items: flex-end; gap: var(--s3) var(--s4);
    padding: var(--s3) var(--s4); background: var(--tint); border-radius: 6px; }
  .field { display: grid; gap: var(--s1); }
  .field > span { font-size: 11px; line-height: 16px; font-weight: 600; text-transform: uppercase;
    letter-spacing: .04em; color: var(--muted); }
  select, input[type=date] { font: inherit; color: var(--text); height: 32px; padding: 0 var(--s3);
    min-width: 168px; background: var(--surface); border: 1px solid var(--line); border-radius: 4px; }
  .date-step { display: flex; gap: var(--s1); }
  .date-step input { min-width: 148px; }
  button { font: inherit; font-weight: 600; color: var(--text); height: 32px; padding: 0 var(--s4);
    background: var(--surface); border: 1px solid var(--line); border-radius: 4px; cursor: pointer; }
  button.icon { padding: 0; width: 32px; }
  button.primary { background: var(--accent); border-color: var(--accent); color: #fff; }
  button:hover { border-color: #b9bfca; }
  button.primary:hover { background: #2652b9; }
  .spacer { flex: 1; }
  :focus-visible { outline: 2px solid var(--accent); outline-offset: 1px; }

  .main { display: grid; grid-template-columns: minmax(0, 1fr) 320px; gap: var(--s5); align-items: start; }
  h2 { font-size: 11px; line-height: 16px; font-weight: 600; text-transform: uppercase;
    letter-spacing: .04em; color: var(--muted); }
  .list-head { display: flex; justify-content: space-between; align-items: baseline; padding-bottom: var(--s2); }
  .legend { display: flex; gap: var(--s3); color: var(--muted); font-size: 12px; }
  .legend i { display: inline-block; width: 8px; height: 8px; border-radius: 50%; margin-right: var(--s1); }

  .schedule { list-style: none; padding: 0; background: var(--surface);
    border: 1px solid var(--line); border-radius: 6px; overflow: hidden; }
  .slot { display: grid; grid-template-columns: 64px 4px minmax(0, 1fr) auto; align-items: center;
    column-gap: var(--s3); min-height: 48px; padding: var(--s2) var(--s4);
    border-top: 1px solid var(--line); cursor: pointer; }
  .slot:first-child { border-top: 0; }
  .slot:hover { background: #f8f9fb; }
  .slot[aria-selected=true] { background: var(--accent-soft); }
  .slot:focus-visible { outline-offset: -2px; }
  .time { font: 12px/16px var(--mono); color: var(--muted); font-variant-numeric: tabular-nums; }
  .bar { align-self: stretch; border-radius: 2px; background: var(--c); }
  .what { min-width: 0; }
  .what strong { display: block; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .what span { color: var(--muted); font-size: 12px; line-height: 16px; }
  .slot.open .what strong { color: var(--muted); font-weight: 500; }

  .status { font-size: 11px; line-height: 16px; font-weight: 600; color: var(--c);
    background: color-mix(in srgb, var(--c) 12%, transparent); padding: 0 var(--s2); border-radius: 8px; }
  .booked { --c: var(--booked); } .held { --c: var(--held); }
  .open { --c: var(--open); } .blocked { --c: var(--blocked); }

  aside { background: var(--surface); border: 1px solid var(--line); border-radius: 6px;
    padding: var(--s4); display: grid; gap: var(--s4); position: sticky; top: var(--s4); }
  .sum-title { display: grid; gap: var(--s1); }
  .sum-title h3 { font-size: 16px; line-height: 22px; font-weight: 650; }
  .sum-title .row { display: flex; gap: var(--s2); align-items: center; color: var(--muted); }
  dl { display: grid; grid-template-columns: 88px 1fr; gap: var(--s2) var(--s3); }
  dt { color: var(--muted); } dd { font-variant-numeric: tabular-nums; }
  .group { display: grid; gap: var(--s2); }
  .actions { display: flex; gap: var(--s2); padding-top: var(--s4); border-top: 1px solid var(--line); }
  .actions button { flex: 1; padding: 0 var(--s3); }

  @media (max-width: 860px) {
    body { padding: var(--s3); }
    .main { grid-template-columns: 1fr; }
    aside { position: static; }
    header { flex-direction: column; align-items: flex-start; gap: var(--s1); }
  }
</style>
</head>
<body>
<div class="app">

  <header>
    <div>
      <h1>Studio Bookings</h1>
      <div class="sub">Thursday, 29 Oct 2026</div>
    </div>
    <div class="tally" aria-label="Day totals">
      <span><b>5</b> booked</span><span><b>2</b> held</span><span><b>2</b> open</span><span><b>1</b> blocked</span>
    </div>
  </header>

  <form class="filters" aria-label="Filters" onsubmit="return false">
    <label class="field">
      <span>Date</span>
      <div class="date-step">
        <button type="button" class="icon" aria-label="Previous day">‹</button>
        <input type="date" value="2026-10-29">
        <button type="button" class="icon" aria-label="Next day">›</button>
      </div>
    </label>
    <label class="field">
      <span>Room</span>
      <select>
        <option>Studio A – Live Room</option>
        <option>Studio B – Mix Suite</option>
        <option>Studio C – Vocal Booth</option>
      </select>
    </label>
    <label class="field">
      <span>Engineer</span>
      <select>
        <option>All engineers</option>
        <option>Maya Okafor</option>
        <option>Dev Patel</option>
        <option>Lena Strauss</option>
      </select>
    </label>
    <div class="spacer"></div>
    <button type="button">Reset</button>
    <button type="button" class="primary">New booking</button>
  </form>

  <div class="main">
    <section aria-labelledby="sched">
      <div class="list-head">
        <h2 id="sched">Studio A · Day schedule</h2>
        <div class="legend">
          <span><i style="background:var(--booked)"></i>Booked</span>
          <span><i style="background:var(--held)"></i>Held</span>
          <span><i style="background:var(--open)"></i>Open</span>
          <span><i style="background:var(--blocked)"></i>Blocked</span>
        </div>
      </div>

      <ul class="schedule" role="listbox" aria-label="Time slots">
        <li class="slot blocked" tabindex="0" role="option" data-state="Blocked" data-title="Maintenance" data-client="—" data-eng="Facilities" data-time="09:00 – 10:00" data-dur="1 h" data-rate="—" data-notes="Monthly console and monitor calibration.">
          <span class="time">09:00</span><span class="bar"></span>
          <div class="what"><strong>Maintenance</strong><span>Facilities</span></div>
          <span class="status">Blocked</span>
        </li>
        <li class="slot booked" tabindex="0" role="option" data-state="Booked" data-title="Harbor Lights – Drum tracking" data-client="Harbor Lights" data-eng="Maya Okafor" data-time="10:00 – 12:00" data-dur="2 h" data-rate="$180 / h" data-notes="Kit mics pre-set from Tuesday. Client bringing own snare.">
          <span class="time">10:00</span><span class="bar"></span>
          <div class="what"><strong>Harbor Lights – Drum tracking</strong><span>Maya Okafor · 2 h</span></div>
          <span class="status">Booked</span>
        </li>
        <li class="slot booked" tabindex="0" role="option" aria-selected="true" data-state="Booked" data-title="Harbor Lights – Drum tracking" data-client="Harbor Lights" data-eng="Maya Okafor" data-time="10:00 – 12:00" data-dur="2 h" data-rate="$180 / h" data-notes="Kit mics pre-set from Tuesday. Client bringing own snare.">
          <span class="time">11:00</span><span class="bar"></span>
          <div class="what"><strong>Harbor Lights – Drum tracking</strong><span>Maya Okafor · continued</span></div>
          <span class="status">Booked</span>
        </li>
        <li class="slot open" tabindex="0" role="option" data-state="Open" data-title="Available" data-client="—" data-eng="Unassigned" data-time="12:00 – 13:00" data-dur="1 h" data-rate="$180 / h" data-notes="Free slot. Use New booking to reserve.">
          <span class="time">12:00</span><span class="bar"></span>
          <div class="what"><strong>Available</strong><span>Unassigned</span></div>
          <span class="status">Open</span>
        </li>
        <li class="slot held" tabindex="0" role="option" data-state="Held" data-title="Vocal overdubs (tentative)" data-client="Nora Vale" data-eng="Dev Patel" data-time="13:00 – 15:00" data-dur="2 h" data-rate="$150 / h" data-notes="Hold expires today 17:00 unless deposit is received.">
          <span class="time">13:00</span><span class="bar"></span>
          <div class="what"><strong>Vocal overdubs (tentative)</strong><span>Nora Vale · Dev Patel · 2 h</span></div>
          <span class="status">Held</span>
        </li>
        <li class="slot held" tabindex="0" role="option" data-state="Held" data-title="Vocal overdubs (tentative)" data-client="Nora Vale" data-eng="Dev Patel" data-time="13:00 – 15:00" data-dur="2 h" data-rate="$150 / h" data-notes="Hold expires today 17:00 unless deposit is received.">
          <span class="time">14:00</span><span class="bar"></span>
          <div class="what"><strong>Vocal overdubs (tentative)</strong><span>Nora Vale · continued</span></div>
          <span class="status">Held</span>
        </li>
        <li class="slot booked" tabindex="0" role="option" data-state="Booked" data-title="Mixdown – “Static Bloom”" data-client="Kiln Records" data-eng="Lena Strauss" data-time="15:00 – 18:00" data-dur="3 h" data-rate="$140 / h" data-notes="Stems delivered. Reference track in shared folder.">
          <span class="time">15:00</span><span class="bar"></span>
          <div class="what"><strong>Mixdown – “Static Bloom”</strong><span>Lena Strauss · 3 h</span></div>
          <span class="status">Booked</span>
        </li>
        <li class="slot booked" tabindex="0" role="option" data-state="Booked" data-title="Mixdown – “Static Bloom”" data-client="Kiln Records" data-eng="Lena Strauss" data-time="15:00 – 18:00" data-dur="3 h" data-rate="$140 / h" data-notes="Stems delivered. Reference track in shared folder.">
          <span class="time">16:00</span><span class="bar"></span>
          <div class="what"><strong>Mixdown – “Static Bloom”</strong><span>Lena Strauss · continued</span></div>
          <span class="status">Booked</span>
        </li>
        <li class="slot booked" tabindex="0" role="option" data-state="Booked" data-title="Mixdown – “Static Bloom”" data-client="Kiln Records" data-eng="Lena Strauss" data-time="15:00 – 18:00" data-dur="3 h" data-rate="$140 / h" data-notes="Stems delivered. Reference track in shared folder.">
          <span class="time">17:00</span><span class="bar"></span>
          <div class="what"><strong>Mixdown – “Static Bloom”</strong><span>Lena Strauss · continued</span></div>
          <span class="status">Booked</span>
        </li>
        <li class="slot open" tabindex="0" role="option" data-state="Open" data-title="Available" data-client="—" data-eng="Unassigned" data-time="18:00 – 19:00" data-dur="1 h" data-rate="$200 / h" data-notes="Evening rate applies.">
          <span class="time">18:00</span><span class="bar"></span>
          <div class="what"><strong>Available</strong><span>Unassigned</span></div>
          <span class="status">Open</span>
        </li>
      </ul>
    </section>

    <aside aria-labelledby="sumh" aria-live="polite">
      <div class="sum-title">
        <h2 id="sumh">Selected booking</h2>
        <h3 id="s-title">Harbor Lights – Drum tracking</h3>
        <div class="row"><span class="status booked" id="s-state">Booked</span><span id="s-time">10:00 – 12:00</span></div>
      </div>

      <dl>
        <dt>Client</dt><dd id="s-client">Harbor Lights</dd>
        <dt>Engineer</dt><dd id="s-eng">Maya Okafor</dd>
        <dt>Room</dt><dd>Studio A – Live Room</dd>
        <dt>Session</dt><dd id="s-dur">2 h</dd>
        <dt>Rate</dt><dd id="s-rate">$180 / h</dd>
      </dl>

      <div class="group">
        <h2>Notes</h2>
        <p id="s-notes">Kit mics pre-set from Tuesday. Client bringing own snare.</p>
      </div>

      <div class="actions">
        <button type="button">Reschedule</button>
        <button type="button">Cancel</button>
        <button type="button" class="primary">Edit</button>
      </div>
    </aside>
  </div>
</div>

<script>
  const slots = document.querySelectorAll('.slot');
  const $ = id => document.getElementById(id);
  function select(el) {
    slots.forEach(s => s.setAttribute('aria-selected', s === el));
    const d = el.dataset;
    $('s-title').textContent = d.title;
    $('s-time').textContent = d.time;
    $('s-client').textContent = d.client;
    $('s-eng').textContent = d.eng;
    $('s-dur').textContent = d.dur;
    $('s-rate').textContent = d.rate;
    $('s-notes').textContent = d.notes;
    $('s-state').textContent = d.state;
    $('s-state').className = 'status ' + d.state.toLowerCase();
  }
  slots.forEach(s => {
    s.addEventListener('click', () => select(s));
    s.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); select(s); }
    });
  });
</script>
</body>
</html>
```

The filters are visual only. Changing the date, room or engineer doesn't change the schedule, and the buttons in the summary don't do anything yet. The header tally is hard-coded to match the sample data.
