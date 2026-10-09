I couldn't save `studio-booking.html` because the Write tool is disabled in this session. I haven't previewed the page in a browser either. Below is the full file. Save it as `studio-booking.html` and open it. If you re-enable Write, I'll write it straight to the working directory.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Studio Bookings</title>
<style>
  :root {
    /* 4px base scale */
    --s1: 4px; --s2: 8px; --s3: 12px; --s4: 16px; --s5: 24px; --s6: 32px;
    --bg: #f4f5f7; --surface: #ffffff; --tint: #eceef2; --line: #dfe2e8;
    --text: #1c2029; --muted: #626a79;
    --accent: #2a5bd7; --accent-bg: #e8eefc;
    --booked: #2a5bd7; --hold: #b7791f; --block: #8a909c; --free: #1f7a4d;
    --radius: 4px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 13px; line-height: 20px; color: var(--text);
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #14161b; --surface: #1c1f26; --tint: #242832; --line: #2f3440;
      --text: #e8eaef; --muted: #98a0b0; --accent: #7aa2ff; --accent-bg: #202c4a;
      --booked: #7aa2ff; --hold: #e0a84a; --block: #7d8493; --free: #55c08a;
    }
  }
  * { box-sizing: border-box; }
  body { margin: 0; background: var(--bg); }
  .app { max-width: 1120px; margin: 0 auto; padding: var(--s5); display: grid; gap: var(--s4); }

  header.top { display: flex; align-items: baseline; justify-content: space-between; }
  h1 { margin: 0; font-size: 16px; line-height: 24px; font-weight: 650; }
  .top .meta { color: var(--muted); }

  /* Filters: one tinted strip, since the controls read as one unit */
  .filters { display: flex; flex-wrap: wrap; align-items: end; gap: var(--s4);
    padding: var(--s3) var(--s4); background: var(--tint); border-radius: var(--radius); }
  .field { display: grid; gap: var(--s1); }
  .field label {
    font-size: 11px; line-height: 16px; letter-spacing: .04em;
    text-transform: uppercase; color: var(--muted); font-weight: 600;
  }
  .filters .actions { margin-left: auto; display: flex; gap: var(--s2); }
  select, input[type=date], button {
    font: inherit; color: inherit; height: 28px; padding: 0 var(--s3);
    background: var(--surface); border: 1px solid var(--line); border-radius: var(--radius);
  }
  select { min-width: 148px; }
  button { cursor: pointer; padding: 0 var(--s4); }
  button.primary { background: var(--accent); border-color: var(--accent); color: #fff; font-weight: 600; }
  :focus-visible { outline: 2px solid var(--accent); outline-offset: 1px; }

  .main { display: grid; grid-template-columns: minmax(0, 1fr) 300px; gap: var(--s5); align-items: start; }

  /* Schedule */
  .section-head { display: flex; align-items: baseline; justify-content: space-between; padding-bottom: var(--s2); }
  h2 { margin: 0; font-size: 13px; font-weight: 650; }
  .legend { display: flex; gap: var(--s3); color: var(--muted); font-size: 12px; }
  .dot { display: inline-block; width: 8px; height: 8px; border-radius: 50%; margin-right: var(--s1); background: var(--c); }

  .schedule { list-style: none; margin: 0; padding: 0; background: var(--surface);
    border: 1px solid var(--line); border-radius: var(--radius); }
  .slot + .slot { border-top: 1px solid var(--line); }
  .slot button {
    all: unset; box-sizing: border-box; display: grid;
    grid-template-columns: 96px minmax(0, 1fr) 120px 88px;
    align-items: center; gap: var(--s3); width: 100%; min-height: 40px;
    padding: var(--s2) var(--s4); cursor: pointer; border-left: 3px solid transparent;
  }
  .slot button:hover { background: var(--bg); }
  .slot button:focus-visible { outline: 2px solid var(--accent); outline-offset: -2px; }
  .slot[aria-selected=true] button { background: var(--accent-bg); border-left-color: var(--accent); }
  .time { font-variant-numeric: tabular-nums; color: var(--muted); }
  .who { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .who small { color: var(--muted); font-size: 12px; margin-left: var(--s2); }
  .eng { color: var(--muted); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .status { justify-self: end; font-size: 12px; font-weight: 600; color: var(--c); }
  .status::before { content: ""; display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: var(--c); margin-right: var(--s1); }
  .s-booked { --c: var(--booked); } .s-hold { --c: var(--hold); }
  .s-block { --c: var(--block); }   .s-free { --c: var(--free); }
  .free .who, .free .eng { color: var(--muted); }

  /* Summary: one surface; groups separated by space and hairlines */
  aside { background: var(--surface); border: 1px solid var(--line); border-radius: var(--radius);
    padding: var(--s4); display: grid; gap: var(--s4); position: sticky; top: var(--s5); }
  aside header { display: grid; gap: var(--s1); }
  aside h2 { font-size: 15px; line-height: 20px; }
  aside .sub { color: var(--muted); }
  dl { margin: 0; display: grid; gap: var(--s2); }
  dl > div { display: grid; grid-template-columns: 84px 1fr; gap: var(--s2); }
  dt { color: var(--muted); } dd { margin: 0; }
  .group { display: grid; gap: var(--s2); padding-top: var(--s4); border-top: 1px solid var(--line); }
  .group h3 { margin: 0; font-size: 11px; line-height: 16px; letter-spacing: .04em; text-transform: uppercase; color: var(--muted); font-weight: 600; }
  .total { display: flex; justify-content: space-between; font-weight: 650; padding-top: var(--s2); border-top: 1px solid var(--line); }
  .btns { display: flex; gap: var(--s2); padding-top: var(--s4); border-top: 1px solid var(--line); }
  .btns button { flex: 1; height: 32px; }

  @media (max-width: 860px) {
    .app { padding: var(--s4); }
    .main { grid-template-columns: 1fr; gap: var(--s4); }
    aside { position: static; }
    .slot button { grid-template-columns: 72px minmax(0, 1fr) 80px; }
    .eng { display: none; }
    .filters .actions { margin-left: 0; }
  }
</style>
</head>
<body>
<div class="app">

  <header class="top">
    <h1>Studio Bookings</h1>
    <span class="meta">Mon 5 Oct 2026 · 7 of 10 slots taken</span>
  </header>

  <form class="filters" aria-label="Filters" onsubmit="return false">
    <div class="field"><label for="f-date">Date</label>
      <input id="f-date" type="date" value="2026-10-05"></div>
    <div class="field"><label for="f-room">Room</label>
      <select id="f-room">
        <option>Studio A — Live room</option>
        <option>Studio B — Mix suite</option>
        <option>Studio C — Vocal booth</option>
      </select></div>
    <div class="field"><label for="f-eng">Engineer</label>
      <select id="f-eng">
        <option>Any engineer</option><option>Priya Nair</option>
        <option>Tomás Reyes</option><option>Dana Whitfield</option>
      </select></div>
    <div class="actions">
      <button type="reset">Reset</button>
      <button type="submit" class="primary">Apply</button>
    </div>
  </form>

  <div class="main">
    <section aria-labelledby="sched-h">
      <div class="section-head">
        <h2 id="sched-h">Studio A · Day schedule</h2>
        <div class="legend" aria-label="Legend">
          <span><i class="dot" style="--c:var(--booked)"></i>Booked</span>
          <span><i class="dot" style="--c:var(--hold)"></i>Hold</span>
          <span><i class="dot" style="--c:var(--block)"></i>Blocked</span>
          <span><i class="dot" style="--c:var(--free)"></i>Free</span>
        </div>
      </div>

      <ul class="schedule" role="listbox" aria-label="Time slots">
        <li class="slot" role="option" aria-selected="false"><button type="button">
          <span class="time">09:00–10:00</span><span class="who">Hollow Pines<small>Tracking</small></span><span class="eng">Priya Nair</span><span class="status s-booked">Booked</span></button></li>
        <li class="slot" role="option" aria-selected="false"><button type="button">
          <span class="time">10:00–11:00</span><span class="who">Hollow Pines<small>Tracking</small></span><span class="eng">Priya Nair</span><span class="status s-booked">Booked</span></button></li>
        <li class="slot free" role="option" aria-selected="false"><button type="button">
          <span class="time">11:00–12:00</span><span class="who">Available</span><span class="eng">—</span><span class="status s-free">Free</span></button></li>
        <li class="slot" role="option" aria-selected="false"><button type="button">
          <span class="time">12:00–13:00</span><span class="who">Room reset<small>Maintenance</small></span><span class="eng">House staff</span><span class="status s-block">Blocked</span></button></li>
        <li class="slot" role="option" aria-selected="true"><button type="button">
          <span class="time">13:00–14:00</span><span class="who">Marlo &amp; The Static<small>Vocals</small></span><span class="eng">Tomás Reyes</span><span class="status s-booked">Booked</span></button></li>
        <li class="slot" role="option" aria-selected="false"><button type="button">
          <span class="time">14:00–15:00</span><span class="who">Marlo &amp; The Static<small>Vocals</small></span><span class="eng">Tomás Reyes</span><span class="status s-booked">Booked</span></button></li>
        <li class="slot" role="option" aria-selected="false"><button type="button">
          <span class="time">15:00–16:00</span><span class="who">J. Okafor<small>Podcast</small></span><span class="eng">Dana Whitfield</span><span class="status s-hold">Hold</span></button></li>
        <li class="slot free" role="option" aria-selected="false"><button type="button">
          <span class="time">16:00–17:00</span><span class="who">Available</span><span class="eng">—</span><span class="status s-free">Free</span></button></li>
        <li class="slot" role="option" aria-selected="false"><button type="button">
          <span class="time">17:00–18:00</span><span class="who">Velvet Season<small>Overdubs</small></span><span class="eng">Priya Nair</span><span class="status s-booked">Booked</span></button></li>
        <li class="slot free" role="option" aria-selected="false"><button type="button">
          <span class="time">18:00–19:00</span><span class="who">Available</span><span class="eng">—</span><span class="status s-free">Free</span></button></li>
      </ul>
    </section>

    <aside aria-labelledby="sum-h" aria-live="polite">
      <header>
        <h2 id="sum-h">Marlo &amp; The Static</h2>
        <span class="sub">Booking #4821 · <span class="status s-booked" style="font-size:inherit">Booked</span></span>
      </header>

      <dl>
        <div><dt>Date</dt><dd>Mon 5 Oct 2026</dd></div>
        <div><dt>Time</dt><dd>13:00–15:00 (2 h)</dd></div>
        <div><dt>Room</dt><dd>Studio A — Live room</dd></div>
        <div><dt>Engineer</dt><dd>Tomás Reyes</dd></div>
      </dl>

      <div class="group">
        <h3>Session</h3>
        <dl>
          <div><dt>Type</dt><dd>Vocal tracking</dd></div>
          <div><dt>Contact</dt><dd>marlo@thestatic.example</dd></div>
          <div><dt>Notes</dt><dd>Needs ribbon mic and headphone mix for 3.</dd></div>
        </dl>
      </div>

      <div class="group">
        <h3>Billing</h3>
        <dl>
          <div><dt>Room</dt><dd>2 × $85 = $170</dd></div>
          <div><dt>Engineer</dt><dd>2 × $40 = $80</dd></div>
          <div><dt>Deposit</dt><dd>Paid · −$50</dd></div>
        </dl>
        <div class="total"><span>Balance due</span><span>$200</span></div>
      </div>

      <div class="btns">
        <button type="button">Reschedule</button>
        <button type="button">Cancel</button>
      </div>
    </aside>
  </div>
</div>

<script>
  const slots = document.querySelectorAll('.slot');
  slots.forEach(li => li.querySelector('button').addEventListener('click', () => {
    slots.forEach(s => s.setAttribute('aria-selected', s === li));
  }));
</script>
</body>
</html>
```

**Layout**
- **Filters:** a single tinted strip across the top holds Date, Room and Engineer, with Reset and Apply pushed to the right. It uses a tint rather than a card because the controls read as one unit.
- **Schedule:** ten one-hour slots from 09:00 to 19:00. Each is a 40px row separated by hairlines, with time, client and session type, engineer, and a status dot and label. The legend sits in the section header.
- **Summary:** a sticky 300px side panel for the selected booking. It has a title block, then a details list, then Session and Billing groups divided by hairlines, then the action buttons. It is one surface with no nested cards.

**Spacing**
- All gaps and padding come from a 4px scale (4, 8, 12, 16, 24).
- Space inside a group is smaller than space between groups: 8px between rows in a list, 16px between groups.
- Parent containers own the gaps, using `gap` instead of margins on each child.

**Behaviour**
- Clicking a row moves the selected highlight. The summary text stays on the sample booking, because I didn't wire up per-slot data.
- Status uses a dot and a text label, so it doesn't depend on colour alone. There is a dark-mode variant.
- Below 860px the panel stacks under the schedule and the engineer column is hidden.
