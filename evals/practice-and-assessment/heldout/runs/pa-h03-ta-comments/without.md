# What's wrong with the three comments

**1. "Good job!"** is praise with no content. The student can't tell what was good, so they can't repeat it. It also misses real problems: `SELECT *`, and a subquery that runs about 3x slower than a join. The student will assume the pattern is fine and keep using it.

**2. "Your query is wrong. See the solution."** gives a verdict and hands off the work. It doesn't say what is wrong or where. The cause is specific and teachable: `INNER JOIN` drops customers with no orders. Pointing at the solution skips the lesson, and the student may just copy it.

**3. "Great effort. Needs improvement on joins. 6/10"** is wrong on the facts, because the joins were fine. The real issue is readability: the `a`/`b` aliases and the confusing output column names. The vague "needs improvement" will make the student doubt something they got right. The score has no rubric behind it, and "great effort" reads as a consolation prize.

The common thread is that none of them names something specific in the student's code, and none gives a next step. Each is also disconnected from what the student actually submitted.

# Rewrites

**1. Correct rows, but `SELECT *` and a subquery where a join would do**

> Your query returns the right rows, and the logic is correct. Two things to tighten up:
>
> - **Subquery vs. join:** You used a subquery to pull in the related table. A `JOIN` expresses the same thing more directly, and on the sample data it ran about 3x faster than your version. Try rewriting it as a join and compare the timings with `EXPLAIN` or your client's timer.
> - **`SELECT *`:** List only the columns you need. It makes the intent clear and avoids pulling data you don't use, which matters as tables grow.
>
> When would you still choose a subquery over a join? Have a think and bring it to office hours if you want to talk it through.

**2. `INNER JOIN` drops customers with zero orders**

> The task asks for *every* customer, including those who have never ordered. Your result is missing those customers.
>
> The cause is `INNER JOIN customers` to `orders`. An inner join keeps only rows with a match on both sides, so a customer with no orders disappears before you count anything.
>
> Try this: run your query and compare its row count to `SELECT COUNT(*) FROM customers`. The gap is the customers you're losing. Then think about which join type keeps every row from one side even when there's no match. Also check what `COUNT(...)` does with NULLs, since that affects what a zero-order customer shows up as.
>
> Rework it and resubmit. If you're still stuck, tell me what you tried and I'll help from there.

**3. Correct and clean, but `a`/`b` aliases and confusing output columns**

> Your result is correct and the query is well structured. The joins are done properly.
>
> The one thing to improve is readability:
>
> - **Aliases:** `a` and `b` don't say which table is which, so anyone reading the query (including you in two weeks) has to scroll back to the `FROM`. Short but meaningful aliases like `c` for `customers` and `o` for `orders` fix that.
> - **Output columns:** Rename the columns in the result with `AS`, for example `order_count` instead of a bare `count`, so the output is understandable without reading the query.
>
> Readable SQL matters a lot at work, where other people will maintain your queries. Make those two changes and you'll have a solid answer.

# Template for your TAs

Each comment should:

1. **Name what worked**, specifically.
2. **Name the main issue**, tied to the student's code.
3. **Explain why it matters.**
4. **Give a concrete next step**, ideally something the student can check themselves.

Keep the praise and the problem in the same comment. "Good job!" on a slow, sloppy query teaches the wrong thing just as much as a bare "wrong" does.

If you use numeric scores, publish the rubric. Without one, a "6/10" can't be acted on.
