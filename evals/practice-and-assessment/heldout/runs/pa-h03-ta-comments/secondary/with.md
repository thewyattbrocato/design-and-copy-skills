## What's wrong with the three comments

1. **"Good job!"** is praise with no content. It doesn't say what was good, and it skips the real issues: `SELECT *` and a subquery where a join is simpler, plus a 3x slowdown the student could have measured. The student learns nothing they can act on.

2. **"Your query is wrong. See the solution."** says the query is wrong but not why, so the student can't tell what concept they missed. It also points to the answer, which ends the learning. The student's query is mostly right: it's a join, it's just the wrong kind for this question.

3. **"Great effort. Needs improvement on joins. 6/10"** gives a grade with no reasoning, and "joins" is the wrong diagnosis. The joins are correct. The problems are the `a`/`b` aliases and the unclear output column names. The score is also unexplained. If the rubric is about correctness, a correct result shouldn't get 6/10 without a stated reason, so the TA should either name what the points are for or raise the score.

## Rewrites

**1.** (Note: I'm working from your description, so swap in the student's actual column names.)

> Your query returns the right rows, and reaching for a subquery shows you're thinking in steps. Two things to tighten:
>
> - **`SELECT *`**: List the columns you need. It makes the query's output explicit, and it keeps working if the table gains columns later.
> - **Subquery → join**: Here a `JOIN` does the same job. On the sample data your version runs about 3x slower. Try rewriting it as a join and compare the timings yourself (`EXPLAIN` will show you why).
>
> Next step: rewrite the query with a join and explicit columns, then check that you get the same rows.

**2.**

> Your join is the right idea, but the join type drops some rows. An `INNER JOIN` keeps only customers who have at least one matching order. The question asks for *every* customer, including ones with zero orders, so you need a `LEFT JOIN` starting from `customers`:
>
> ```sql
> SELECT c.customer_id, c.name, COUNT(o.order_id) AS order_count
> FROM customers c
> LEFT JOIN orders o ON o.customer_id = c.customer_id
> GROUP BY c.customer_id, c.name;
> ```
>
> Notice `COUNT(o.order_id)` rather than `COUNT(*)`. For a customer with no orders, the left join produces one row with NULL in `order_id`, and `COUNT(o.order_id)` correctly counts that as 0.
>
> Hint before you look at the solution: run your query and count the rows. Then count the customers. If the numbers differ, which customers are missing?

**3.**

> Your query returns the correct result, and the join logic is sound. The main issue is readability. Aliases like `a` and `b` make the query hard to follow for whoever reads it next, including you in a month. Use short names that say what the table is, such as `c` for `customers` and `o` for `orders`.
>
> The output columns have the same problem. Name them with `AS` so the result reads without the query beside it, for example `customer_name` rather than `name`.
>
> Score: 6/10. Correctness is full, so the deduction is for readability. [Or: raise the score to X if the rubric doesn't include readability.]
>
> Next step: rename the aliases and output columns, then rerun to confirm nothing changed.

## A pattern to apply to all TA comments

- **Name what's right**, specifically enough that the student knows to keep doing it.
- **Name the one thing that matters most**, with the concept behind it ("INNER JOIN drops unmatched rows") rather than just the symptom.
- **Give a hint or a check before the solution**, so the student does the last step.
- **Give a next action**, something they can do and verify in a few minutes.
- **Tie any score to a reason**, or leave it out.
