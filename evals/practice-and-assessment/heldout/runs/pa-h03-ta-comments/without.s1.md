# What's wrong with them

| # | Comment | Problem |
|---|---------|---------|
| 1 | "Good job!" | It's praise with no content, and it's misleading. The student will conclude the query is ideal, but it has a real performance problem. It also misses the chance to say what they did right (correct rows). |
| 2 | "Your query is wrong. See the solution." | It names no error and doesn't say where to look. "See the solution" replaces the TA's explanation. The student has to diff their query against the answer and work out the lesson alone. The tone also reads as a verdict, not teaching. |
| 3 | "Great effort. Needs improvement on joins. 6/10" | It gives the wrong feedback about the wrong thing. The joins were fine, and the real issues are the `a`/`b` aliases and confusing output column names. "Great effort" is filler, and the 6/10 has no rubric behind it. |

The common failure is that none of them point to a specific line, say why it matters, or tell the student what to do next. Two of them also misdiagnose the submission (#1 says nothing is wrong, #3 blames the wrong skill).

A useful comment has four parts: what worked, the specific issue and where it is, why it matters, and a concrete next step.

# Rewrites

**1. Correct rows, but `SELECT *` and a subquery**

> Your query returns the right rows, so the logic is solid.
>
> Two things to tighten up:
> - **Subquery vs. join:** you're using a subquery to pull in the customer data. A plain `JOIN` expresses the same thing, and on the sample data it ran about 3x faster than your version. Try rewriting it and compare the timings yourself (`EXPLAIN` or your client's timer).
> - **`SELECT *`:** list only the columns the exercise asks for. It makes the query's intent clear, and it avoids fetching columns you don't need.
>
> Rewrite it with a join and explicit columns, and tell me what difference you see.

**2. `INNER JOIN` drops customers with no orders**

> Your query runs and the order counts are right for customers who have orders. The problem is that the exercise asks for *every* customer, including those with zero orders, and those customers are missing from your result.
>
> The cause is `INNER JOIN`. It only keeps customers that have a matching row in `orders`, so a customer with no orders disappears before you ever count.
>
> To fix it:
> 1. Change the join so all customers are kept even when there's no match (think about which table should be the "preserved" side).
> 2. Check that `COUNT(...)` counts a column from `orders`, not `COUNT(*)`. With an outer join, `COUNT(*)` would count the unmatched row as 1.
>
> Once you've made the change, compare the row count to `SELECT COUNT(*) FROM customers`. They should match. Come find me if it still looks off.

**3. Correct and clean, but `a`/`b` aliases and confusing output names**

> Your result is correct and the query is well structured, and your join logic is right.
>
> The thing to work on is readability:
> - **Table aliases:** `a` and `b` force the reader to scroll back to the `FROM` clause to remember which is which. Use short but meaningful aliases, like `c` for `customers` and `o` for `orders`.
> - **Output column names:** the result columns are confusing. Use `AS` to give them clear names, such as `customer_name` and `order_count`, so whoever reads the output (or a downstream query) knows what each one means.
>
> This won't change your results, but readable SQL is easier to debug and review, and you'll be writing a lot of it. Try renaming both and re-running.

# One more suggestion for the TA team

Drop the numeric score from the comment unless there's a shared rubric (correctness, efficiency, readability). A bare "6/10" gives the student a judgment but nothing to act on. If you want scores, tie each one to named criteria so students can see where the points went.
