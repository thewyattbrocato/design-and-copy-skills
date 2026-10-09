## What's wrong with each comment

**1. "Good job!"** praises without saying what was good, so the student can't repeat it. It also skips the two things that matter: the query is slow relative to a join, and `SELECT *` pulls unused columns. The student has no next step.

**2. "Your query is wrong. See the solution."** doesn't say what's wrong, so the student can't find the bug. Pointing to the solution ends the learning. The student will copy the answer without learning why `INNER JOIN` drops customers with no orders.

**3. "Great effort. Needs improvement on joins. 6/10"** is filler ("great effort") and points at the wrong problem. The joins were correct. The actual issues are the aliases and the column names. The 6/10 has no explanation, so a clean, correct query looks like a punishment the student can't understand.

## Rewrites

**1.**
> Your query returns the correct rows and is easy to follow. Two things to work on:
> - `SELECT *` returns every column, including ones you don't use. List the columns you need. This matters more as tables grow.
> - A JOIN gives the same rows as your subquery and runs about 3× faster on the sample data. Rewrite it as a join, then compare the two with `EXPLAIN` (or your database's equivalent) to see why.

**2.**
> Your query returns customers who have orders, but the task asks for every customer, including those with zero orders. Think about what `INNER JOIN` does when a customer has no matching rows in `orders`. Which join type keeps every row from the left table whether or not it matches?
>
> Once you've changed the join, check what your `COUNT` counts. A customer with no orders should show 0, not 1.
>
> Test it on a customer you know has no orders. If they appear with 0, you've got it. Then compare your version with the solution and note what changed and why.

**3.**
> Your query returns the correct rows, and the join logic is right. Points came off for readability:
> - The aliases `a` and `b` don't tell the reader what the tables are. Use names that mean something, like `c` for customers and `o` for orders.
> - The output column name `[the name]` is hard to read in a report. Use `AS` to give it a clear name, such as `order_count`.
>
> Code is read far more than it's written. These are quick fixes, and they make the query easier for a reviewer, or for you in three weeks, to follow.

## General rules for TA comments

- **Name the specific thing** in this submission. "Good job" and "needs improvement" could apply to anyone's work.
- **Say why it matters** in one clause, such as "this returns wrong results when a customer has no orders" or "the reader can't tell what `a` refers to."
- **Give a next step** the student can do without the solution, such as a test case, a question, or a rewrite to try.
- **Hint before you give the answer.** Naming the concept (`LEFT JOIN`) is usually enough.
- **Make the grade traceable.** Tie any score to a rubric line. If 6/10 reflects readability, say so and name the rubric item. If the score doesn't match that rubric, fix the score.
