## What's wrong with them

| Comment | Problem |
|---|---|
| 1. "Good job!" | It praises a query that has two real problems and names neither. The student learns nothing and may repeat `SELECT *` and the subquery. |
| 2. "Your query is wrong. See the solution." | It doesn't say what is wrong, where, or why. The student has to compare against the solution and work out the difference alone. That is the very skill the exercise is meant to build. |
| 3. "Great effort. Needs improvement on joins. 6/10" | The join was fine. The actual issue is readability: aliases and output column names. "Effort" praises the person, not the work. "6/10" has no stated basis, so the student can't tell what would earn a 9. |

All three share the same gaps. They don't say what the query did, they don't name the specific thing to change, and they don't tell the student what to do next.

## Rewrites

Each one follows the same order: what happened, the principle in one sentence, then the better move.

**1. Correct rows, but `SELECT *` and a subquery**

> Your query returns exactly the right rows, so the logic is correct. On the sample data it runs about 3x slower than a join version, though. A subquery can make the database do extra work that a join avoids, and `SELECT *` pulls columns you don't use. Try rewriting it as a join and list only the columns the question asks for. Then compare the run times.

**2. `INNER JOIN` drops customers with no orders**

> Your query returns every customer who has ordered, but customers with zero orders are missing. The exercise asked for all customers. `INNER JOIN` keeps only rows that match on both sides, so customers with no orders disappear. Change it to a `LEFT JOIN` from customers to orders. Also check your count: `COUNT(*)` would show 1 for a customer with no orders, while `COUNT(o.order_id)` correctly shows 0. Rerun it and check that the zero-order customers appear.

**3. Correct and clean, but `a`/`b` aliases and confusing output columns**

> Your result is correct and the query is well structured. The join logic is solid. The weak spot is readability. With `a` and `b`, a reader has to look back at the `FROM` clause to know which table each column comes from. The output headers are also hard to interpret. Use short aliases that hint at the table, like `c` for customers and `o` for orders. Give output columns names a reader would understand, like `AS order_count`. Someone else should be able to read this query and its result without asking you what they mean.

I dropped the score from #3 because it didn't say what it measured. If your program needs scores, publish a short rubric, for example correctness, performance, and readability. Then the TA can say which part cost the points.

## Likely root cause

TAs probably write these comments because they have little time and no template, not because they don't care. A cheap fix is a three-line comment template: what the query did, the one thing to change and why, and what to try next. Add a short list of common issues, like `INNER` vs `LEFT JOIN`, `SELECT *`, and aliasing, with pre-written explanations to adapt. A TA could then write comments like the ones above in about a minute each.
