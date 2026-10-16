## What's wrong with the three comments

1. **"Good job!"** praises without saying what was good, and it misses the two real issues: `SELECT *` and the subquery that runs three times slower than a join. A student reading it learns nothing and may think the query is fine.
2. **"Your query is wrong. See the solution."** says that something is wrong but not what. The student can't tell whether the problem is the join, the count, or the output. Pointing to the solution skips the learning, and the student still has to work out why their rows are missing.
3. **"Great effort... 6/10"** gives a score with no reason. "Needs improvement on joins" is wrong about this submission, since the joins were correct. The real problem was the aliases and column names, which the comment never mentions. A bare 6/10 can't be checked or acted on.

All three share the same gap: they describe the grade or the feeling about the work, not the specific thing in the query.

## Rewrites

**1.**
> Your query returns the right rows, so the logic is sound. Two things to work on:
>
> - `SELECT *` pulls every column. List the columns you need. This also makes the output clearer to the next person who reads it.
> - The subquery could be a join. On the sample data, the join version runs about 3× faster than yours. Rewrite the subquery as a join and compare the timings. Then think about when a subquery is still the better choice.

**2.**
> Your query is missing customers who have never ordered. The requirement asks for every customer, but `INNER JOIN` only keeps customers with at least one matching order, so the customers with zero orders are dropped.
>
> Look at which join type keeps every row from the customers table even when there's no match. Then check what `COUNT` should count so that a customer with no orders shows 0, not 1. Once you've changed the query, check it: does your result have as many rows as the customers table?

**3.**
> Your joins and results are correct, and the query is easy to follow. The main thing to fix is the aliases. `a` and `b` don't tell a reader which table is which, and you'll have to look them up when you return to this query. Use short names that mean something, like `c` for customers and `o` for orders. Also name your output columns the way the requirement does (for example, `order_count` rather than `count`).
>
> Score: [X]/10. Correctness [full], readability [X/Y] (aliases and column names). The score should map to the rubric so you can see which part lost points.

Note: I don't know your rubric, so the score line in #3 is a placeholder. The breakdown is the important part. If the 6/10 really came from the aliasing alone, the breakdown should show that.

## The pattern to use every time

- **Name the specific thing** in the submission ("the `INNER JOIN` on line 4," not "joins").
- **Say why it matters**: correctness, speed, or readability.
- **Give a next step** the student can do, such as a hint, a question, or a test to run. Save the full solution for after the exercise is submitted and graded.
- **Praise specifically** when you give it ("the `WHERE` clause is clear and correct"), so the student knows what to keep doing.
- **Tie any score to a rubric item** so the student knows what to fix to improve it.

If it helps, I can turn this into a short TA guide with a few before-and-after examples for other common SQL mistakes like `GROUP BY` errors or `NULL` handling.
