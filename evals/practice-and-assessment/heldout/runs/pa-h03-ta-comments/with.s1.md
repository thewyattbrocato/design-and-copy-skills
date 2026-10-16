## What's wrong with the three comments

**1. "Good job!"** This is praise with no information. The student gets the right rows, so they will assume the query is fine. They won't learn that `SELECT *` and the subquery are habits to fix, or that the query is about 3x slower than the join. The comment also hides what they did well.

**2. "Your query is wrong. See the solution."** It says the result is wrong but not how. It also sends the student to the solution, so they never find the cause themselves. The student used `INNER JOIN`, which drops customers with zero orders. That is a specific, learnable misunderstanding, and the comment doesn't name it.

**3. "Great effort. Needs improvement on joins. 6/10"** Three problems:
- It praises effort rather than the work.
- It says "joins" need work when the join was fine. The real issues are naming and readability.
- The 6/10 has no stated criteria, so the student can't tell what would make it a 9.

All three comments describe the TA's impression instead of what the query did.

## Rewrites

**1. Correct, but inefficient**

> Your query returns the right rows, and the logic is correct. Two things to change before this is production-style SQL:
>
> - **Subquery vs. join:** On the sample data, this runs about 3x slower than the equivalent join. A join lets the database plan the lookup once instead of repeating it. Try rewriting it as a `JOIN` and compare run times.
> - **`SELECT *`:** List only the columns you need. It makes the output predictable if the table changes, and it avoids reading data you don't use.
>
> Rewrite it with both changes and confirm you still get the same rows.

**2. Missing customers with zero orders**

> Your query runs and the counts are right for customers who have orders. But the exercise asked for *every* customer, including those who have never ordered, and those customers are missing from your result.
>
> The cause is `INNER JOIN`. It keeps only rows that match on both sides, so a customer with no orders is dropped. To keep every customer, you need a join type that preserves all rows from `customers`.
>
> Try this: change the join type, then run `SELECT COUNT(*) FROM customers` and check that your result has that many rows. Also check what `COUNT` does with the `NULL`s that appear for customers with no orders. Which column should you count so those customers get 0?

**3. Correct, but hard to read**

> Your result is correct and the query is cleanly structured, so the join logic is fine.
>
> The readability issue is naming. Aliasing the tables as `a` and `b` means a reader has to look back at the `FROM` clause to learn what `b.id` refers to. The output columns are confusing for the same reason.
>
> Next time:
> - Use short but meaningful aliases, such as `c` for `customers` and `o` for `orders`.
> - Name output columns with `AS`, for example `order_count` instead of `count`.
>
> Rename these in your query and reread it as if you'd never seen the exercise. Is it clear what each column holds?

## Pattern for TAs

Each rewrite follows the same structure:
1. Say what the query did (the result).
2. Name the one thing that matters most and why.
3. Give a concrete next step the student can check themselves.

If you use scores, publish the criteria. A rubric with correctness, efficiency, and readability would make the 6/10 in comment 3 meaningful.

I haven't checked these against your course materials, so adjust the join type and function names to match what you've taught. If you want, I can turn the pattern into a one-page TA template with a short practice set for calibrating comments.
