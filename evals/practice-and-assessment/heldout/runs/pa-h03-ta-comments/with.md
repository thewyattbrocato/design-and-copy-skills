## What's wrong with them

All three comments fail the same way. The student can't tell what they did, why it matters, or what to do next.

1. **"Good job!"** is praise with no information. It hides a real problem (the 3x slowdown, `SELECT *`, an unneeded subquery), so the student will repeat it. It also never says what was right: the correct rows.
2. **"Your query is wrong. See the solution."** gives a verdict and hands the student the answer. The student doesn't learn that the cause is the INNER JOIN dropping customers with no orders. They'll probably copy the solution without understanding it.
3. **"Great effort. Needs improvement on joins. 6/10"** praises effort, not the work. The "joins" criticism is wrong, because the join was fine. The real issues are the `a`/`b` aliases and the confusing output column names, and the comment never mentions them. The 6/10 has no stated basis, so the student can't tell what would earn a 9.

## Rewrites

Each one says what happened, gives the principle in a sentence, and ends with one thing to try. Where a comment would be unclear without it, I've included the query.

**1.**
> Your query returns the right rows, so the logic is sound. Two things to look at next. `SELECT *` pulls every column, including ones you don't use. A subquery here makes the database do extra work a join can do directly. On the sample data, your version ran about 3x slower than a join. Try rewriting it with a JOIN and listing only the columns you need, then compare run times.

**2.**
> Your result is missing customers who have never ordered. The task asked for every customer, including those with an order count of 0. An INNER JOIN keeps only customers with a matching row in `orders`, so those customers disappear. Try a LEFT JOIN from `customers` to `orders`. Then check that a customer with no orders shows up with a count of 0, not missing. Your grouping and counting approach is otherwise on the right track. [Remove this sentence if the student's grouping is actually wrong.]

**3.**
> Your result is correct and the query is well structured, including the join. The weak spot is readability. With tables aliased as `a` and `b`, a reader has to look back at the FROM clause to know which is which. The output column names are also hard to read. Try aliases that hint at the table (`c` for `customers`, `o` for `orders`) and name the output columns (for example `AS order_count`). Then re-read the query as if someone else wrote it.

## Notes

- I dropped the 6/10. If you want scores, publish a short rubric (correctness, efficiency, readability) so a number maps to something the student can act on.
- In #2, I assumed the student's grouping was fine since you only mentioned the join. TAs should only say that when they've checked.
