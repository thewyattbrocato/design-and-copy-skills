```tsx
type Jar = {
  id: string;
  name: string;
  startedOn: string;
  day: number;
  targetDays: number;
  saltPercent: number;
  nextBurp: string;
  notes?: string;
};

export function JarList({ jars, onAdd }: { jars: Jar[]; onAdd: () => void }) {
  return (
    <div className="min-h-screen bg-[#f4efe4] px-6 pb-28 pt-10 text-[#2b2a22] md:px-10 md:pt-14">
      <header className="mb-10 border-b border-[#d9cfb8] pb-6">
        <p className="text-xs font-semibold uppercase tracking-[0.14em] text-[#6b634f]">Brinewell</p>
        <h1 className="mt-2 font-serif text-4xl tracking-tight md:text-5xl">On the counter</h1>
        <p className="mt-2 text-sm tabular-nums text-[#6b634f]">
          {jars.length} {jars.length === 1 ? "jar" : "jars"} fermenting
        </p>
      </header>

      <ul className="grid grid-cols-1 gap-5 sm:grid-cols-2 xl:grid-cols-3">
        {jars.map((jar) => {
          const ready = jar.day >= jar.targetDays;
          const pct = Math.min(100, (jar.day / jar.targetDays) * 100);
          return (
            <li
              key={jar.id}
              className="rounded-lg border border-[#d9cfb8] bg-[#fbf8f1] p-5 transition-colors hover:border-[#3f5b2e]"
            >
              <div className="flex items-start justify-between gap-3">
                <h2 className="truncate font-serif text-xl text-[#2b2a22]">{jar.name}</h2>
                <span
                  className={
                    ready
                      ? "shrink-0 rounded bg-[#3f5b2e] px-2 py-0.5 text-xs font-semibold text-white"
                      : "shrink-0 rounded border border-[#cfc4aa] px-2 py-0.5 text-xs font-medium text-[#6b634f]"
                  }
                >
                  {ready ? "Ready" : "Fermenting"}
                </span>
              </div>
              <p className="mt-1 text-sm text-[#6b634f]">Started {jar.startedOn}</p>

              <div className="mt-5 flex items-baseline justify-between">
                <p className="tabular-nums">
                  <span className="font-serif text-3xl">Day {jar.day}</span>
                  <span className="ml-1 text-sm text-[#6b634f]">of {jar.targetDays}</span>
                </p>
              </div>
              <div
                role="progressbar"
                aria-valuemin={0}
                aria-valuemax={jar.targetDays}
                aria-valuenow={jar.day}
                aria-label={`${jar.name} fermentation progress`}
                className="mt-2 h-1.5 w-full overflow-hidden rounded-full bg-[#e3dac4]"
              >
                <div className="h-full rounded-full bg-[#3f5b2e]" style={{ width: `${pct}%` }} />
              </div>

              <dl className="mt-5 grid grid-cols-2 divide-x divide-[#d9cfb8] border-t border-[#d9cfb8] pt-4 text-sm">
                <div>
                  <dt className="text-xs uppercase tracking-wider text-[#6b634f]">Salt</dt>
                  <dd className="mt-0.5 font-medium tabular-nums">{jar.saltPercent}%</dd>
                </div>
                <div className="pl-4">
                  <dt className="text-xs uppercase tracking-wider text-[#6b634f]">Next burp</dt>
                  <dd className="mt-0.5 font-medium">{jar.nextBurp}</dd>
                </div>
              </dl>

              {jar.notes && (
                <p className="mt-4 border-t border-dashed border-[#d9cfb8] pt-3 text-sm text-[#5a5342]">
                  {jar.notes}
                </p>
              )}
            </li>
          );
        })}
      </ul>

      <button
        onClick={onAdd}
        className="fixed bottom-6 right-6 rounded-md bg-[#3f5b2e] px-5 py-3 text-sm font-semibold text-white shadow-md transition-colors hover:bg-[#33491f] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#3f5b2e] md:bottom-8 md:right-8"
      >
        + Add New Jar
      </button>
    </div>
  );
}
```

**Decision notes**
- **Tells removed:** violet-to-indigo gradients, the hero banner with cheerful copy, `hover:scale-105`, heavy shadows, gray-on-white cards, and an "Active" badge that was the same on every jar.
- **Palette:** The neutrals are warm parchment and cream, like a kitchen counter or a crock label. The one accent is a deep brine green, used for progress, the primary button and the "Ready" state.
- **Type and numbers:** Headings use the system serif stack, so there's no new font dependency. Numbers are tabular. Day count is the largest thing on each card, since it's what people check.
- **Words:** The banner is now a plain header, "On the counter", with a jar count. The count comes from `jars.length`. The status badge now reads "Fermenting" or "Ready", derived from `day >= targetDays`.

**To confirm**
- The "Ready" badge is new behavior I derived from `day` and `targetDays`. If you'd rather keep a static badge, swap it back.
- I haven't rendered it, so check it in the browser, especially at narrow widths.
