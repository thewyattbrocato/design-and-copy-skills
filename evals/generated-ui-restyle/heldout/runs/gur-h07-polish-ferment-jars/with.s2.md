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
    <div className="min-h-screen bg-stone-100 px-5 pb-28 pt-10 text-stone-900 md:px-10 md:pt-14">
      <header className="mb-10 max-w-5xl border-b border-stone-300 pb-6">
        <p className="text-xs font-medium uppercase tracking-widest text-emerald-800">Brinewell</p>
        <h1 className="mt-2 font-serif text-4xl tracking-tight text-stone-900">On the counter</h1>
        <p className="mt-1 text-stone-600">
          {jars.length} {jars.length === 1 ? "jar" : "jars"} fermenting
        </p>
      </header>

      <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 xl:grid-cols-3">
        {jars.map((jar) => (
          <article
            key={jar.id}
            className="rounded-lg border border-stone-300 bg-stone-50 p-5 transition-colors hover:border-emerald-800"
          >
            <div className="flex items-baseline justify-between gap-3">
              <h2 className="truncate font-serif text-xl text-stone-900">{jar.name}</h2>
              <span className="shrink-0 text-xs font-medium uppercase tracking-wider text-emerald-800">Active</span>
            </div>
            <p className="mt-0.5 text-sm text-stone-600">Started {jar.startedOn}</p>

            <div className="mt-5 flex items-baseline justify-between text-sm">
              <span className="tabular-nums text-stone-900">
                <span className="font-serif text-2xl">{jar.day}</span>
                <span className="text-stone-600"> / {jar.targetDays} days</span>
              </span>
            </div>
            <div className="mt-2 h-1.5 w-full overflow-hidden rounded-sm bg-stone-200">
              <div
                className="h-full bg-emerald-800"
                style={{ width: `${Math.min(100, (jar.day / jar.targetDays) * 100)}%` }}
              />
            </div>

            <dl className="mt-5 grid grid-cols-2 divide-x divide-stone-300 border-t border-stone-300 pt-4 text-sm">
              <div>
                <dt className="text-xs uppercase tracking-wider text-stone-600">Salt</dt>
                <dd className="mt-0.5 font-medium tabular-nums">{jar.saltPercent}%</dd>
              </div>
              <div className="pl-4">
                <dt className="text-xs uppercase tracking-wider text-stone-600">Next burp</dt>
                <dd className="mt-0.5 font-medium">{jar.nextBurp}</dd>
              </div>
            </dl>

            {jar.notes && (
              <p className="mt-4 border-l-2 border-amber-600 pl-3 font-serif text-sm italic text-stone-700">
                {jar.notes}
              </p>
            )}
          </article>
        ))}
      </div>

      <button
        onClick={onAdd}
        className="fixed bottom-6 right-6 rounded-md bg-emerald-900 px-5 py-3 text-sm font-semibold text-stone-50 shadow-md transition-colors hover:bg-emerald-800 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-emerald-900 md:bottom-8 md:right-8"
      >
        + Add New Jar
      </button>
    </div>
  );
}
```

**Decision notes**
- **Tells removed:** violet-to-indigo gradients, the hero banner, hover scale and heavy shadows, "unlock amazing flavors" copy, and the gray-box stat tiles.
- **Palette:** warm stone, like a kitchen counter and crock-lid ceramic. One deep pickle-green accent (emerald-800/900) is used for progress, the status and the button. Amber appears only on the notes rule, like a masking-tape label on a jar.
- **Type and shape:** a system serif (`font-serif`) for jar names, the day count and notes, so the jars read like labels. Sans is used for data. The cards are flat with hairline borders, and the stats are a small label/value list.
- **Copy:** the banner is now a plain header, "On the counter", with a jar count computed from `jars`. Props, fields and the button are unchanged.

**To confirm:** the "Active" label is shown for every jar, as in your original. If jars can be finished, you'll want it to follow real status. I haven't rendered this, so check it at narrow widths.
