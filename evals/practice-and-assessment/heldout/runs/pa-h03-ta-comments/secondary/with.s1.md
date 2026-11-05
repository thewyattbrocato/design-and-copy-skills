## What's wrong with the three comments

**1. "Good job!"** tells the student nothing they can act on. The query is correct, so the praise is accurate, but it hides the two things that matter most: `SELECT *` pulls columns nobody asked for, and the subquery is slower than a join on the same data. A student reading this has no reason to revisit the query.

**2. "Your query is wrong. See the solution."** says the query is wrong but not why. The real problem is conceptual: an INNER JOIN drops customers with no orders, and the exercise asked for them. The comment also points the student to the answer, so they copy it without learning the join behavior. That is the most likely reason they'd call it useless.

**3. "Great effort. Needs improvement on joins. 6/10"** has three problems. "Great effort" is filler. "Needs improvement on joins" is wrong for this submission, since the joins were correct and the weak points were the aliases and output column names. The 6/10 has no explanation, so the student can't tell what earned or lost points.

## Rewrites

**1.**
> Your query returns the right rows, and the logic is clear. Two things to tighten:
>
> - **`SELECT *`**: List the columns you need. It makes the output explicit and keeps the query working if the table changes.
> - **Subquery vs. join**: Your version runs about three times slower than a join on the sample data. Try rewriting the subquery as a JOIN and compare the timings. Which one does the database have to do more work for, and why?
>
> Once you've tried it, tell me what you found.

**2.**
> The exercise asks for every customer, including those with zero orders. Check what your JOIN does to a customer who has no rows in `orders`. Which join type keeps rows from the left table even when there's no match on the right? Look that up in the course notes and try it.

The comment names the requirement, points to the exact place the error happens, and gives the join type to look up without writing the query.

**3.**
> Your joins are correct, and the result is right. The main improvements are in readability:
>
> - **Aliases**: `a` and `b` make it hard to tell which table each column comes from. Use short names that mean something, like `c` for customers and `o` for orders.
> - **Output column names**: The result headers are hard to read. Use `AS` to label them, e.g., `AS order_count`.
>
> This is a good foundation. Clear names will matter more as your queries get longer.

*Score:* If you grade with a rubric, state what the points were for, e.g., "Correct results (4/4), readability (1/2: aliases and column names), efficiency (not scored this week)." A bare number without a breakdown is what made this comment feel arbitrary. If you don't have a rubric, consider dropping the number and using the feedback alone.

## Principles behind the rewrites

- **Lead with what's specific.** Name the exact line, column, or behavior, not the overall quality.
- **Explain why, not just what.** "Use a LEFT JOIN" teaches less than "an INNER JOIN drops rows with no match."
- **Ask, don't answer.** A question or a hint keeps the student doing the thinking. Withhold the solution until they've tried.
- **End with one next step.** Students need to know what to do next, not just what went wrong.
- **Match the feedback to the work.** A correct query with style issues should get style feedback, not a critique of joins.
