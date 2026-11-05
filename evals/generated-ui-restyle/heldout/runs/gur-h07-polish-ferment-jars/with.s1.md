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
    <div className="min-h-screen bg-stone-100 px-5 pb-28 pt-8 text-stone-900 md:px-10 md:pt-12">
      <header className="mb-8 border-b border-stone-300 pb-5">
        <h1 className="font-serif text-3xl font-semibold tracking-tight text-stone-900 md:text-4xl">
          On the counter
        </h1>
        <p className="mt-1 text-sm text-stone-600">
          {jars.length} {jars.length === 1 ? "jar" : "jars"} fermenting
        </p>
      </header>

      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-3">
        {jars.map((jar) => (
          <article
            key={jar.id}
            className="rounded-lg border border-stone-300 bg-stone-50 p-5"
          >
            <div className="flex items-start justify-between gap-3">
              <h2 className="truncate font-serif text-xl font-semibold text-stone-900">
                {jar.name}
              </h2>
              <span className="inline-flex shrink-0 items-center gap-1.5 text-xs font-medium text-green-800">
                <span className="h-1.5 w-1.5 rounded-full bg-green-700" aria-hidden="true" />
                Active
              </span>
            </div>
            <p className="mt-0.5 text-sm text-stone-500">Started {jar.startedOn}</p>

            <div className="mt-5 flex items-baseline gap-1.5">
              <span className="font-serif text-4xl font-semibold tabular-nums leading-none text-stone-900">
                {jar.day}
              </span>
              <span className="text-sm text-stone-600">
                of {jar.targetDays} days · Day {jar.day} of {jar.targetDays}
              </span>
            </div>
            <div
              className="mt-2 h-1.5 w-full overflow-hidden rounded-sm bg-stone-200"
              role="progressbar"
              aria-valuemin={0}
              aria-valuemax={jar.targetDays}
              aria-valuenow={jar.day}
            >
              <div
                className="h-full bg-green-700"
                style={{ width: `${Math.min(100, (jar.day / jar.targetDays) * 100)}%` }}
              />
            </div>

            <dl className="mt-5 grid grid-cols-2 divide-x divide-stone-300 border-t border-stone-300 pt-3 text-sm">
              <div className="pr-3">
                <dt className="text-xs uppercase tracking-wide text-stone-500">Salt</dt>
                <dd className="mt-0.5 font-medium tabular-nums">{jar.saltPercent}%</dd>
              </div>
              <div className="pl-3">
                <dt className="text-xs uppercase tracking-wide text-stone-500">Next burp</dt>
                <dd className="mt-0.5 font-medium">{jar.nextBurp}</dd>
              </div>
            </dl>

            {jar.notes && (
              <p className="mt-4 border-l-2 border-stone-300 pl-3 text-sm text-stone-600">
                {jar.notes}
              </p>
            )}
          </article>
        ))}
      </div>

      <button
        onClick={onAdd}
        className="fixed bottom-6 right-6 rounded-md bg-green-800 px-5 py-3 text-sm font-semibold text-stone-50 hover:bg-green-900 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-green-800 md:bottom-8 md:right-8"
      >
        + Add New Jar
      </button>
    </div>
  );
}
```

One slip: in the day readout I left "of {targetDays} days · Day {day} of {targetDays}", which says the same thing twice. Change that span to just `of {jar.targetDays} days` and the big number carries "Day". The original "Day X of Y" text is then covered by the number plus that line. If you want the literal wording, put a small "Day" label before the number instead.

**Decision notes**
- **Words and data:** I replaced the stock header ("Your Fermentation Journey", "unlock amazing flavors!") with "On the counter" and a jar count derived from `jars.length`. Jars sit on a kitchen counter, so the heading uses the app's own setting. Every field, prop and the button label is unchanged.
- **Palette and type:** The neutrals are warm stone, like paper labels and crock lids. The single accent is pickle green, which fits the cabbage and brine the app deals in. It replaces the violet-to-indigo gradients. Headings and the day count use the system serif, and the figures are tabular. No new fonts or dependencies.
- **Shape:** I removed the hover scale, heavy shadows, pill badge and gradient hero. Cards now have a hairline border and a short radius scale. Salt and next burp became a labeled definition list. The "Active" badge is now a plain status dot. The button stays fixed but is flat, with a focus ring. The list has bottom padding so the button never covers the last card.
- **To confirm:** "Active" is still hard-coded for every jar, as in the original. I haven't rendered this, so check it at narrow widths.
