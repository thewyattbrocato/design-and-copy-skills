## What's wrong with them

- **"Good job!"** praises without saying what worked, and it hides the main lesson. The query returns correct rows, but the student also needs to hear about `SELECT *`, the subquery, and the 3x slowdown.
- **"Your query is wrong. See the solution."** gives a verdict but no cause. Pointing to the solution invites copying, so the student never learns why the INNER JOIN drops customers with no orders.
- **"Great effort. Needs improvement on joins. 6/10"** attaches the criticism to the wrong thing. The joins were correct. The problems were the `a`/`b` aliases and unclear output names. The score also has no stated basis, so the student can't tell what cost points.

All three also lack a next step. A useful comment says what works, names the specific issue, explains why it matters, and suggests a concrete thing to try without giving the answer away.

## Rewrites

**1. Correct rows, but the query is heavier than it needs to be.**

> The rows are correct, and the query is easy to follow. Two things to tighten:
>
> - `SELECT *` returns every column from every table. List the columns you need. The query then documents its own output and won't change if a table gains a column.
> - The subquery works, but a `JOIN` does the same job here. On the sample data your version ran about three times slower than the join. Rewrite the subquery as a join and time both versions.
>
> Question to carry forward: can this be one join instead of a nested query?

**2. Missing customers with zero orders.**

> You're using the right tables and columns. The issue is the join type. An INNER JOIN keeps only customers with at least one matching order, but this exercise needs every customer, including those with none.
>
> Ask yourself: which table has to appear in full in the result, and which join keeps the unmatched rows from that side?
>
> Then check your count. If a customer has no orders, a `LEFT JOIN` produces one row with NULLs on the orders side. `COUNT(*)` counts that row as 1. Which column should you count so a customer with no orders shows 0?

**3. Correct result, weak readability (6/10).**

> The result is correct and the joins are right. The points were lost on readability:
>
> - `a` and `b` don't say what they refer to. Use short names that do, such as `customers c` and `orders o`.
> - Output names like the ones here are hard to read. Give each column an `AS` alias that says what it holds, such as `order_count` instead of `count`.
>
> Renaming these is the change that will matter most to the next person who reads your query, including you in a month. If the 6/10 comes from a rubric, list the criteria that lost points here so the student can see where the score came from.

## A short checklist for TAs

- Say what the student did right, specifically.
- Name the issue at the level where it lives (join type, naming, performance), not a general topic like "joins."
- Explain why it matters.
- Give a next step that points toward the fix without writing it out.
- Tie any score to visible criteria.

I used generic names like `customers` and `orders` in the rewrites. Swap in your course's actual schema if it differs.
