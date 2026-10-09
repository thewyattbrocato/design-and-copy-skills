## What's wrong with the three comments

1. **"Good job!"** gives no information. It praises without naming what worked, and it hides the two things the student should change: `SELECT *` and the subquery that runs three times slower than a join. A student who reads this has no reason to revisit the query.

2. **"Your query is wrong. See the solution."** doesn't say what is wrong, so the student can't tell which part failed. It also sends them to the answer instead of the reasoning, so they'll copy the solution without learning why INNER JOIN drops customers with no orders. The tone is dismissive, which discourages students who are already struggling.

3. **"Great effort. Needs improvement on joins. 6/10"** names the wrong problem. The joins are correct; the issues are the single-letter aliases and unclear output column names. The score has no breakdown, so the student can't tell what cost points. A 6/10 on a correct query will look arbitrary unless the rubric explains it.

The common failure is that none of the comments are **specific** (pointing at the exact clause), **explained** (saying why it matters), or **actionable** (giving a next step).

## Rewrites

**1. Good job / SELECT * / subquery**

> Your rows are correct, so the logic is sound. Two things to tighten:
>
> - `SELECT *` pulls every column. List the ones you need. It makes your intent clear to a reader and avoids surprises when the table changes.
> - The subquery can be a plain `JOIN`. On the sample data your version runs about 3x slower. Rewrite it as a join and time both. Which one is faster, and what do you think the database is doing differently?

**2. Missing customers**

> The requirement is every customer, including those with no orders. `INNER JOIN` keeps only customers that match at least one order, so zero-order customers are dropped. Check your output for a customer who has never ordered. If they're missing, that's the bug.
>
> Which join keeps all rows from the customers table? Once you switch, think about what `COUNT` should return for a customer with no orders. (Hint: `COUNT(*)` counts the row a `LEFT JOIN` produces for a missing match. `COUNT(o.order_id)` doesn't.)

**3. Aliases / 6/10**

> Your query returns the correct result, and the structure is clean. The readability needs work:
>
> - Single-letter aliases like `a` and `b` make joins hard to follow. Use short names that say what the table is, like `c` for customers and `o` for orders.
> - Rename the output columns so someone reading the results understands them. `count` becomes `order_count`, and so on.
>
> Score breakdown: correctness, full marks. Readability, partial credit for the alias and column-name issues above. Fixing those would raise the score.

The third rewrite assumes the 6/10 comes from readability. If your rubric weights something else, the breakdown should say that instead. If the score doesn't match the rubric, it's better to fix the grade than to attach a critique that doesn't explain it.

## Principles you could use for the TA guide

- **Point to the exact clause or line**, not the whole query.
- **Say why it matters**, so the student learns the concept.
- **End with a question or a check** the student can run themselves.
- **Praise the specific thing that works**, then name what to change.
- **Tie every score to named criteria**, so a number always has a reason.
