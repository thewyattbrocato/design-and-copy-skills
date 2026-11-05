## What's wrong with them

None of the three tells the student what happened or what to do next.

1. **"Good job!"** is praise with no content. The student learns nothing, and the real problems (`SELECT *`, the subquery that runs about 3x slower) are never mentioned. It also tells them the approach is fine.
2. **"Your query is wrong. See the solution."** gives a verdict but no diagnosis. The student has to reverse-engineer the error from the solution. They'll likely copy it without understanding why `INNER JOIN` dropped customers, so they'll repeat the mistake on the next outer-join problem.
3. **"Great effort. Needs improvement on joins. 6/10"** is wrong on its facts: the joins were correct. It praises effort instead of the work. The score has no stated criteria. The real issues (aliases `a` and `b`, confusing output column names) go unnamed, and the comment points at the wrong skill.

## Rewrites

**1. Correct, but inefficient**

> Your query returns exactly the right rows, so the logic is sound. Two things to tighten:
> - You used a subquery where a join does the same job. On the sample data your version runs about 3x slower than the join version, because [the subquery is evaluated separately from the main query]. When you're combining rows from two tables, try a join first.
> - `SELECT *` pulls every column. List only the columns the exercise asks for.
>
> Next step: rewrite it with a join and named columns, then compare the run times yourself.

**2. Wrong result: missing customers**

> Your query returns every customer who has placed an order, but the exercise asks for every customer, including those with zero orders. Those customers are missing from your result.
>
> Cause: `INNER JOIN` keeps only rows that match on both sides. A customer with no orders has no match, so it's dropped before you count anything.
>
> Fix: keep all customers by making `customers` the preserved side of the join (`LEFT JOIN`). Then count a column from `orders`, such as `COUNT(o.order_id)`, not `COUNT(*)`. `COUNT(*)` would count the empty row as 1 order.
>
> Next step: make the change and check that a customer with no orders shows 0. Then try the next exercise, which also needs unmatched rows.

**3. Correct and clean, but unreadable naming**

> Your result is correct and the query is well structured, including the joins. Nothing to fix there.
>
> One thing to improve is readability. Aliasing the tables as `a` and `b` means a reader has to scroll back to the `FROM` clause to see what `b.col` refers to. The output column names are also confusing. Use short aliases that hint at the table (`c` for `customers`, `o` for `orders`), and give output columns clear names with `AS` (for example `order_count`).
>
> Next step: rename the aliases and output columns, then ask a classmate to read the query cold and say what it does.

## Notes

- **Template for TAs:** each comment should say what the query did, why, and one next step. If TAs say they don't have time for that, the fix is a short template or a bank of common-error comments (like #2), not more effort per comment.
- **Scores:** if you keep a score like 6/10, publish the criteria behind it. Otherwise drop it for these exercises. The comments above carry the information without it.
