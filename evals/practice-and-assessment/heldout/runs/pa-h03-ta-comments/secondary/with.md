## What's wrong with the originals

1. **"Good job!"** names no specific thing to keep doing and no specific thing to change. The student can't tell whether the SELECT * or the subquery matters, or whether the speed difference is important.
2. **"Your query is wrong. See the solution."** says the work is wrong without saying where. It also hands over the answer, so the student doesn't learn the join logic. The real bug, an INNER JOIN that drops customers with no orders, is never named.
3. **"Great effort. Needs improvement on joins. 6/10"** is vague in three ways. "Needs improvement on joins" doesn't match the feedback, since the joins are correct, and the student can't tell what the 6 reflects. The aliasing and column-name problems are never mentioned.

All three share the same gaps: no link to the actual submission, no reason, and no next step.

## Rewrites

I only have your descriptions of the submissions, not the SQL, so the wording below is generic. Swap in the real table and column names before using them.

**1.**
> Your query returns the correct rows, and the logic is easy to follow. Two things to work on:
>
> - `SELECT *` pulls every column. Name the columns you need. That keeps the output stable if the table changes and makes the query's purpose clear to the next reader.
> - The subquery works, but on the sample data the equivalent JOIN runs about three times faster. Rewrite it as a JOIN and time both. Then think about when the subquery would still be the clearer choice.

**2.**
> The query gets the columns right, but it's missing customers who have never placed an order, and the task asks for every customer. Look at the join type: INNER JOIN keeps only rows that match in both tables. Which join keeps every row from the left table?
>
> Once you change it, check what your count returns for a customer with no orders. `COUNT(*)` counts the row even when it's empty, so think about which column should be counted.

This version points to the bug and asks questions that lead to the fix. It doesn't give the answer away.

**3.**
> Your query returns the correct rows, and the structure is clean. Points were lost on readability:
>
> - Aliases `a` and `b` make it hard to tell which table each column comes from. Use names that mean something, like `c` for customers and `o` for orders, or the full table names.
> - The output headers are hard to interpret. Add `AS` aliases such as `AS order_count` so the result explains itself.
>
> Score: 6/10. Correctness earned full credit; the deduction is for readability.

If the 6 reflects something beyond readability, the comment should name that too. A score with no stated basis is the thing students are complaining about.

## The pattern to follow

Each comment should cover:
- **What's right**, specifically enough that the student knows to keep doing it.
- **What's wrong**, pointing to the part of the submission, not the whole thing.
- **Why it matters**, so the student learns the principle and not just this fix.
- **A next step**, ideally a hint or question rather than the solution.
- **The score basis**, if you give a score.
