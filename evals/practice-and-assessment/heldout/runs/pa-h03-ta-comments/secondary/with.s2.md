## What's wrong with each comment

**1. "Good job!"** gives the student no information. It doesn't say what was good, and it leaves out the two things they should change: `SELECT *` and the subquery that runs three times slower than the join. The student can't tell whether to fix anything, and the performance point, which is the most instructive part of the submission, is lost.

**2. "Your query is wrong. See the solution."** doesn't say what is wrong. It sends the student to the answer, which skips the lesson, and the lesson is the point of this exercise: INNER JOIN drops customers with no matching orders. A useful comment names that mechanism and gives a hint that leads the student to the fix.

**3. "Great effort. Needs improvement on joins. 6/10"** names the wrong problem. The join is correct. The real issues are the `a`/`b` aliases and the unclear output column names. "Great effort" is filler, and the score has no stated basis, so the student can't tell why they got a 6 for work that was correct. If the rubric does deduct for readability, the comment should say so.

## Rewrites

**1.**
> Your query returns the right rows, and the logic is sound. Two things to work on:
>
> - `SELECT *` pulls every column, including ones you don't use. Name the columns you need. It makes the query easier to read and keeps it from breaking if the table changes.
> - The subquery works, but on the sample data the join version ran about three times faster. Rewrite it as a join and time both. Then think about why the join might be faster here: a correlated subquery can end up doing work once per row.

**2.**
> Your query runs, but the result is missing customers who have never placed an order. Check your output for a customer you know has no orders. They won't appear. Think about why: INNER JOIN keeps only rows that match on both sides. Which join type keeps every row from the left table even when there's no match? Once you've changed that, look at what `COUNT` is counting for those customers. Ask me if you want to talk it through.

**3.**
> Your query returns the correct rows, and the join conditions are right. The thing to improve is readability:
>
> - Aliases like `a` and `b` make it hard to tell which table is which. Use short names that mean something, like `c` for customers and `o` for orders.
> - Give your output columns clear names with `AS`, such as `order_count` instead of `cnt`, so the result makes sense without the query next to it.
>
> Score: 6/10. The result is correct, so the deduction is for readability (aliases and column names). If the rubric doesn't include readability, the score should be revisited.

## Principles these follow

- **Say what's right, what's wrong, and what to do next.** Praise should name the specific thing that was done well.
- **Diagnose the actual issue.** A comment should point at the problem that matters most in the submission, not a general area.
- **Give a hint, not the answer.** Name the concept (here, join types and how `COUNT` treats NULLs) and ask a question that leads to the fix.
- **Tie scores to criteria.** A number with no stated reason is not useful feedback.

One caveat: I don't have your rubric, so the 6/10 in #3 may reflect criteria I can't see. If it doesn't, the score and the comment should be reconciled.
