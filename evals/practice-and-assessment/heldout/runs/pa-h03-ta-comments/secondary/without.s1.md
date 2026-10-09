## What's wrong with the three comments

1. **"Good job!"** gives praise without information. The student can't tell what worked or what to change, and the real issues (`SELECT *`, the subquery, the 3x slowdown) go unmentioned.
2. **"Your query is wrong. See the solution."** doesn't say what is wrong, and handing over the answer removes the learning. The actual error is conceptual: `INNER JOIN` drops customers with no orders, which the requirement explicitly asks to keep.
3. **"Great effort. Needs improvement on joins. 6/10"** contradicts itself. A correct, clean query doesn't need joins improved, and the real issue is naming. A score with no stated reason also gives the student nothing to act on.

## Rewritten comments

**1.**
> Your rows are correct, and the query runs cleanly. Two things would make it stronger:
>
> - `SELECT *` pulls every column, including ones you don't need. List the columns you want so the output is explicit and the query doesn't change if the table does.
> - The subquery returns the same rows as a join here, but it runs about 3x slower on the sample data. Rewrite it as a join and compare the timing, or run `EXPLAIN` on both, to see why. When you need columns from two tables, a join is usually the better default.
>
> Next step: rewrite the subquery as a join, confirm it returns the same output, and compare the run times.

**2.**
> Your query doesn't return every customer yet. Reread the requirement: customers who have never ordered should still appear, with a count of 0. What does `INNER JOIN` do with a customer that has no matching rows in `orders`? Which join type keeps every row from the left table? Once you've changed it, check your count: if you count all rows, an unmatched customer still shows 1. Which column should you count instead?
>
> Try it and tell me what you get. Happy to look at it with you.

**3.**
> Your join is correct, and the result matches what was asked. The gap is readability:
>
> - Aliases `a` and `b` don't tell a reader which table is which. Use short names that match the tables, like `c` for customers and `o` for orders.
> - The output column names don't describe their contents. Alias them to clear names, such as `customer_name` or `order_count`.
>
> Readable names make a query faster to review and easier to debug.
>
> Score: [X/10, per rubric]. Correctness: full credit. Readability and naming: partial credit, for the reasons above.

For the third comment, I don't know your rubric, so the score is a placeholder. The point is that the score should be stated with the criteria it reflects, and the criteria should match the comment.

## Principles for all of them

- **Say what's specific.** Name the line, the column, or the requirement.
- **Tie feedback to the requirement.** Students can check their work against the spec, not against the TA's opinion.
- **Give one clear next step.** Two or three priorities are enough.
- **Guide, don't solve.** Use questions and hints, and share a solution only after the student has tried.
- **Keep praise and critique separate and accurate.** Say what works, then what to change, and make sure the score reflects the same points.
