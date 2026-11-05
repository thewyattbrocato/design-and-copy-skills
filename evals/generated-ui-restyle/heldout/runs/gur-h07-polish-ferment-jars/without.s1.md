Here's the restyled component. Props, data and the button are unchanged. The only copy I changed is the header text.

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
    <div className="min-h-screen bg-[#f3ecdc] px-5 pb-32 pt-8 text-stone-900 md:px-10 md:pt-12">
      <header className="mx-auto mb-10 max-w-6xl border-b-2 border-stone-900/80 pb-6">
        <p className="text-xs font-semibold uppercase tracking-[0.2em] text-lime-800">Brinewell</p>
        <h1 className="mt-2 font-serif text-4xl font-bold tracking-tight md:text-5xl">On the counter</h1>
        <p className="mt-2 max-w-xl text-stone-600">
          Everything bubbling away in your kitchen, and when it needs you next.
        </p>
      </header>

      <div className="mx-auto grid max-w-6xl grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-2 xl:grid-cols-3">
        {jars.map((jar) => {
          const pct = Math.min(100, (jar.day / jar.targetDays) * 100);
          return (
            <article
              key={jar.id}
              className="overflow-hidden rounded-xl border-2 border-stone-900/80 bg-[#fffaf0] shadow-[4px_4px_0_0_rgba(41,37,36,0.8)] motion-safe:transition motion-safe:hover:-translate-y-0.5 motion-safe:hover:shadow-[6px_6px_0_0_rgba(41,37,36,0.8)]"
            >
              {/* lid */}
              <div className="h-3 border-b-2 border-stone-900/80 bg-lime-800" />

              <div className="p-5">
                <div className="flex items-start justify-between gap-3">
                  <h2 className="truncate font-serif text-2xl font-bold">{jar.name}</h2>
                  <span className="shrink-0 rounded-full border border-lime-800/40 bg-lime-100 px-2.5 py-0.5 text-xs font-semibold text-lime-900">
                    Active
                  </span>
                </div>
                <p className="mt-1 text-sm text-stone-500">Started {jar.startedOn}</p>

                <div
                  role="progressbar"
                  aria-valuemin={0}
                  aria-valuemax={jar.targetDays}
                  aria-valuenow={Math.min(jar.day, jar.targetDays)}
                  aria-label={`${jar.name} progress`}
                  className="mt-5 h-3 w-full overflow-hidden rounded-sm border border-stone-900/70 bg-stone-200"
                >
                  <div className="h-full bg-amber-500" style={{ width: `${pct}%` }} />
                </div>
                <p className="mt-2 text-sm text-stone-600">
                  Day <span className="font-bold tabular-nums text-stone-900">{jar.day}</span> of{" "}
                  <span className="tabular-nums">{jar.targetDays}</span>
                </p>

                <dl className="mt-5 grid grid-cols-2 divide-x divide-dashed divide-stone-400 border-y border-dashed border-stone-400 text-sm">
                  <div className="py-3 pr-3">
                    <dt className="text-xs font-semibold uppercase tracking-wider text-stone-500">Salt</dt>
                    <dd className="mt-0.5 font-serif text-xl font-bold tabular-nums">{jar.saltPercent}%</dd>
                  </div>
                  <div className="py-3 pl-4">
                    <dt className="text-xs font-semibold uppercase tracking-wider text-stone-500">Next burp</dt>
                    <dd className="mt-0.5 font-serif text-xl font-bold text-amber-700">{jar.nextBurp}</dd>
                  </div>
                </dl>

                {jar.notes && (
                  <p className="mt-4 border-l-4 border-amber-400 pl-3 text-sm leading-relaxed text-stone-700">
                    {jar.notes}
                  </p>
                )}
              </div>
            </article>
          );
        })}
      </div>

      <button
        onClick={onAdd}
        className="fixed bottom-6 right-6 rounded-full border-2 border-stone-900/80 bg-lime-800 px-6 py-3.5 font-semibold text-[#fffaf0] shadow-[4px_4px_0_0_rgba(41,37,36,0.8)] outline-none motion-safe:transition hover:bg-lime-900 focus-visible:ring-4 focus-visible:ring-amber-400 active:translate-x-0.5 active:translate-y-0.5 active:shadow-[2px_2px_0_0_rgba(41,37,36,0.8)] md:bottom-8 md:right-8"
      >
        + Add New Jar
      </button>
    </div>
  );
}
```

What changed:
- **Palette:** The violet and indigo gradients are gone. It's now a warm parchment background with olive lids and amber for brine and progress. It reads as kitchen counter instead of SaaS.
- **Cards:** Each card looks like a jar label. It has a green lid strip, a chunky border, and a hard offset shadow. The `hover:scale-105` is now a small lift that respects reduced-motion settings.
- **Type:** Headings and key numbers (salt, next burp) use Tailwind's built-in `font-serif`, so there's no new font or dependency. Numbers are tabular.
- **Stats:** The two gray boxes are now a dashed-divider `dl`, like a recipe card. "Next burp" is in amber so it stands out.
- **Notes:** The italic gray text is now a quoted note with an amber left rule.
- **Header:** The gradient hero is now a plain masthead with a rule underneath. The heading reads "On the counter", and the tagline is toned down. Change it back if you want the old wording.
- **Button:** Same label and handler, now solid olive with a matching offset shadow and a visible focus ring.
- **Small fixes:** The progress bar has `role="progressbar"` with ARIA values. The page has bottom padding so the floating button doesn't cover the last card.
