## What's wrong with the three comments

**1. "Good job!"** This is praise with no information. The student can't tell what was good, so they can't repeat it. It also hides a real problem: `SELECT *` and a subquery that runs about 3x slower than a join. The student will keep doing both because they were told it was fine.

**2. "Your query is wrong. See the solution."** It says the query is wrong but not how, where, or why. Pointing to the solution makes the student compare two queries and guess at the difference. This is the most costly of the three, because the student had a clear, fixable misunderstanding: `INNER JOIN` drops customers with no orders. It's also discouraging, with no acknowledgment of what they got right.

**3. "Great effort. Needs improvement on joins. 6/10"** It has three problems:
- It praises effort rather than the work.
- "Needs improvement on joins" is wrong. The result was correct and the joins were fine.
- The 6/10 punishes a correct, clean query with no stated criteria. The real issues (aliases `a` and `b`, confusing output column names) are about readability, and the comment never mentions them.

The common thread is that none of them says what the student did, what happened as a result, or what to do next. Two of them also misdescribe the submission.

## Rewrites

**1. Correct rows, but `SELECT *` and a subquery**

> Your query returns the right rows, so the logic is sound. Two things to change:
>
> - **Subquery → join.** On the sample data your version runs about 3x slower than the equivalent join, because the subquery is evaluated separately from the main query instead of being combined with it. Try rewriting it as a join and compare the run times yourself.
> - **`SELECT *` → named columns.** Listing only the columns you need makes the output predictable and avoids pulling data you don't use.
>
> Next time you reach for a subquery, ask: "could this be a join?"

**2. INNER JOIN drops customers with zero orders**

> Your query is close, and the counting logic is right. The issue is the join type. The task asked for *every* customer, including those who have never ordered. `INNER JOIN` keeps only customers who have a matching row in `orders`, so customers with zero orders vanish from the result.
>
> Try `LEFT JOIN` from `customers` to `orders`. That keeps all customers, and the unmatched ones get NULLs on the orders side. Then check your count: `COUNT(*)` would count that NULL row as 1, so count a column from `orders` instead, e.g. `COUNT(o.order_id)`.
>
> Rerun it and check that the never-ordered customers now appear with a count of 0.

**3. Correct and clean, but aliases `a`/`b` and confusing output names**

> Your result is correct and the query is well structured. The joins are fine.
>
> One thing to improve is readability. With the aliases `a` and `b`, a reader has to scroll back to the `FROM` clause to learn which table each one is. Short, meaningful aliases (`c` for `customers`, `o` for `orders`) make the query readable at a glance. The output column names are also confusing. Add `AS` to give them clear names, such as `customer_name` and `order_count`.
>
> Whoever reads your query next, including you in a month, will thank you.

## Notes for your TAs

- **Order:** say what happened (the rows were right, or customers went missing), give the one-sentence reason, then the next step.
- **Scores:** if you keep them, tie each one to stated criteria (correctness, performance, readability). A bare 6/10 gives the student nothing to act on.
- **Time:** these rewrites are longer, but a TA who knows the common mistakes can keep a short bank of snippets (INNER vs LEFT JOIN, `SELECT *`, aliasing) and tailor them in under a minute.
