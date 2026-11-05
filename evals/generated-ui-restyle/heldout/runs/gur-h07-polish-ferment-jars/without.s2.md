Here's the restyle. Props, data and the button are unchanged. The big changes are:
- The violet gradients are gone, replaced by a warm kitchen-counter palette: cream, stone, brine green and turmeric.
- Progress is now a jar that fills with brine instead of a generic bar.
- The hover-scale effects are gone.
- I rewrote the header copy to match the new voice. Swap it back if you'd rather keep the old text.

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
    <div className="min-h-screen bg-[#f3ede1] px-6 pb-28 pt-10 text-stone-800 md:px-10 md:pt-14">
      <header className="mb-10 border-b-2 border-dashed border-stone-300 pb-6">
        <p className="text-xs font-semibold uppercase tracking-[0.2em] text-emerald-800">Brinewell</p>
        <h1 className="mt-2 font-serif text-4xl font-bold tracking-tight text-stone-900 md:text-5xl">
          On the counter
        </h1>
        <p className="mt-2 text-stone-600">
          {jars.length} {jars.length === 1 ? "jar" : "jars"} bubbling away. Keep an eye on the lids.
        </p>
      </header>

      <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 xl:grid-cols-3">
        {jars.map((jar) => {
          const pct = Math.min(100, Math.max(0, (jar.day / jar.targetDays) * 100));
          return (
            <article
              key={jar.id}
              className="rounded-xl border border-stone-300 bg-[#fffaf0] p-5 shadow-sm transition hover:-translate-y-0.5 hover:border-stone-400 hover:shadow-md"
            >
              <div className="flex gap-4">
                {/* Jar that fills with brine as the ferment progresses */}
                <div className="flex w-12 shrink-0 flex-col items-center" aria-hidden="false">
                  <div className="h-2 w-9 rounded-sm bg-stone-500" />
                  <div
                    role="progressbar"
                    aria-valuemin={0}
                    aria-valuemax={jar.targetDays}
                    aria-valuenow={jar.day}
                    aria-label={`${jar.name}: day ${jar.day} of ${jar.targetDays}`}
                    className="relative mt-0.5 h-20 w-12 overflow-hidden rounded-b-2xl rounded-t-md border-2 border-stone-400 bg-white/70"
                  >
                    <div
                      className="absolute inset-x-0 bottom-0 bg-amber-400/80 transition-all"
                      style={{ height: `${pct}%` }}
                    />
                    <div className="absolute bottom-2 left-2 h-1.5 w-1.5 rounded-full bg-white/60" />
                    <div className="absolute bottom-5 right-2.5 h-1 w-1 rounded-full bg-white/60" />
                  </div>
                </div>

                <div className="min-w-0 flex-1">
                  <div className="flex items-start justify-between gap-2">
                    <h2 className="truncate font-serif text-xl font-bold text-stone-900">{jar.name}</h2>
                    <span className="shrink-0 rounded-md border border-emerald-800/20 bg-emerald-100 px-2 py-0.5 text-[11px] font-semibold uppercase tracking-wide text-emerald-900">
                      Active
                    </span>
                  </div>
                  <p className="mt-0.5 text-sm text-stone-500">Started {jar.startedOn}</p>
                  <p className="mt-3 text-sm text-stone-700">
                    <span className="font-serif text-3xl font-bold tabular-nums text-stone-900">{jar.day}</span>
                    <span className="text-stone-500"> / {jar.targetDays} days</span>
                  </p>
                </div>
              </div>

              <dl className="mt-4 grid grid-cols-2 divide-x divide-stone-200 rounded-lg border border-stone-200 bg-white/60 text-sm">
                <div className="px-3 py-2">
                  <dt className="text-xs uppercase tracking-wide text-stone-500">Salt</dt>
                  <dd className="mt-0.5 font-semibold tabular-nums">{jar.saltPercent}%</dd>
                </div>
                <div className="px-3 py-2">
                  <dt className="text-xs uppercase tracking-wide text-stone-500">Next burp</dt>
                  <dd className="mt-0.5 font-semibold text-red-800">{jar.nextBurp}</dd>
                </div>
              </dl>

              {jar.notes && (
                <p className="mt-4 border-l-2 border-amber-500 pl-3 text-sm italic text-stone-600">{jar.notes}</p>
              )}
            </article>
          );
        })}
      </div>

      <button
        onClick={onAdd}
        className="fixed bottom-8 right-8 rounded-lg bg-emerald-900 px-5 py-3 font-semibold text-amber-50 shadow-lg ring-1 ring-emerald-950/20 transition hover:bg-emerald-800 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-amber-500 focus-visible:ring-offset-2 focus-visible:ring-offset-[#f3ede1] active:translate-y-px"
      >
        + Add New Jar
      </button>
    </div>
  );
}
```

Notes:
- The `bg-[#f3ede1]` cream is an arbitrary value, so it needs no config. Everything else is stock Tailwind.
- `font-serif` uses your system serif stack. If you load a brand font later, set it as the Tailwind `serif` family and the headings will pick it up.
- The page has bottom padding so the floating button never covers the last card.
- The "Next burp" value is red so it stands out as the thing to act on. I also added `role="progressbar"` to the jar for screen readers.
