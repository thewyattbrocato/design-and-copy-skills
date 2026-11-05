## What's wrong with the originals

| # | Problem |
|---|---|
| 1 | The praise is vague, so the student won't know what they did right. It also hides the real issue. They'll keep writing `SELECT *` and subqueries because nothing told them it cost anything. |
| 2 | It gives a verdict ("wrong") and sends them to the solution. It doesn't say what is wrong, where, or why. The student has to reverse-engineer the error from the answer key, and many won't. |
| 3 | The praise ("great effort") is about effort, not the work. "Needs improvement on joins" is wrong, because the join was correct. The real issues were readability issues (aliases and output names), and the 6/10 has no stated criteria. A student could take away that they don't understand joins when they do. |

All three have the same flaw. They judge the student instead of describing what the query did. Good feedback says what happened, gives the one principle behind it, and names the next move. It also says what was right, specifically.

## Rewrites

**1.**
> Your query returns the correct rows, and the logic is sound. Two things made it slower than it needed to be. On the sample data it ran about 3x slower than the equivalent join. The subquery makes the database do a separate lookup, where a join lets it match the tables in one pass. `SELECT *` also pulls every column when you only need [the columns the exercise asks for]. Try rewriting it as a join and list only the columns you need, then compare the run times. Tell me what you see.

**2.**
> Your query runs, and the join condition is correct. But customers who have never ordered are missing from the result, and the exercise asks for every customer. `INNER JOIN` keeps only rows that match in both tables, so a customer with no orders is dropped before you count anything. Switch to a `LEFT JOIN` from `customers` to `orders`. That keeps all customers. Then use `COUNT(orders.order_id)` rather than `COUNT(*)`. `COUNT(*)` would report 1 for a customer with no orders, but counting the order column gives 0. After the change, check that a customer with no orders appears with a count of 0.

**3.**
> Your result is correct and the query is clean. The join logic is right, so nothing to fix there. The one thing to change is readability. With the aliases `a` and `b` throughout, anyone reading it (including you in a month) has to keep looking back to see which table is which. The output column names are also hard to interpret. Use short aliases that hint at the table (`c` for customers, `o` for orders) and name the output columns with `AS`, for example `AS order_count`. Try that on this query. Naming things for the reader is the habit to build.

I left out the 6/10. If you want scores, publish a short rubric (for example correctness, performance, readability) and score each part. A single number tells the student nothing about what to change.

Two notes:
- The bracketed text in #1 needs the actual columns from the exercise, which I didn't have.
- If TAs find these too long, a good minimum is three parts: what the query did, why, and one next step.
