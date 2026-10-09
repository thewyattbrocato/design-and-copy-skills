## What's wrong with them

All three fail the same test: **a student can't act on them.** Each one also has a specific problem.

1. **"Good job!"** It's praise with no content, and it hides a real issue. The student learns nothing about what was good, and they'll keep writing `SELECT *` plus subqueries because they were told it was fine. A comment that says "good" about a query that is 3x slower than it needs to be is misleading.
2. **"Your query is wrong. See the solution."** It doesn't say what is wrong or where, and it sends the student to a solution to reverse-engineer. The error is a classic, specific, learnable one (INNER vs LEFT JOIN), and the comment turns it into a vague failure. It's also discouraging in tone.
3. **"Great effort. Needs improvement on joins. 6/10"** It's wrong on the facts: the joins were correct, and the real issue was readability (aliases and output column names). The "effort" language is vague, and the score is unexplained, so the student can't tell what would make it a 9.

## Rewrites

**1. SELECT \* and subquery (correct but slower)**

> Your query returns exactly the right rows, so the logic is solid. Two things to tighten up:
>
> - **Replace the subquery with a join.** You're using a subquery to pull in data from the second table, but a `JOIN` expresses the same thing more directly. On the sample data, the join version runs about 3x faster, because the subquery is evaluated separately instead of being planned together with the rest of the query. Try rewriting it and compare with `EXPLAIN`.
> - **List the columns you need instead of `SELECT *`.** It makes the query's output explicit, and it won't break if someone adds a column to the table later.
>
> Both are habits worth building now, because they matter a lot more on large tables.

**2. INNER JOIN dropping customers with no orders**

> The task asks for *every* customer, including those who've never ordered. Your result is missing those customers, and the cause is the `INNER JOIN` between `customers` and `orders`. An inner join keeps only rows that match on both sides, so a customer with no orders is discarded before you ever count anything.
>
> Try a `LEFT JOIN` from `customers` to `orders`. That keeps all customers and fills in NULLs where there are no orders. Then check your count: `COUNT(*)` would count the NULL row as 1, so count a column from `orders` (e.g. `COUNT(o.order_id)`) to get 0 for those customers.
>
> To check your fix, compare the number of rows in your result with `SELECT COUNT(*) FROM customers`. They should match.

**3. Correct and clean, but poor aliases and output names**

> Correct result and a clean structure, and your join logic is right. The remaining issue is readability.
>
> - **Aliases:** `a` and `b` throughout means the reader has to look back at the `FROM` clause to know which table is which. Use short but meaningful aliases, like `c` for `customers` and `o` for `orders`.
> - **Output columns:** the result headers are confusing. Rename them with `AS` (e.g. `COUNT(o.order_id) AS order_count`) so that someone reading the output without seeing the query knows what each column means.
>
> Fix those two and this is a query I'd be happy to see in a real codebase.

## A reusable pattern for TAs

Each rewrite follows the same shape, which may be worth turning into a TA guideline:

1. **Say what worked**, specifically. This is the only kind of praise that teaches.
2. **Name the issue and where it is**, in one sentence.
3. **Explain why it matters** (wrong results, slower, harder to read).
4. **Give a concrete next step**, ideally with a way to check the fix.

Also, drop numeric scores unless there's a rubric the student can see. Comment 3's "6/10" had no explanation, and the student's work was in fact correct.
