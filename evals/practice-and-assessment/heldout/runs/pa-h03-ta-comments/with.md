## What's wrong with the three comments

**The shared problem:** each comment is a verdict (good, wrong, 6/10) with no evidence about the student's query. The student can't tell what they did, why it mattered, or what to try next. Two further problems:

- **#1 praises a query with real problems.** The student learns that `SELECT *` and an unneeded subquery are fine.
- **#3 criticizes the wrong thing.** The joins were correct, and the actual issue (aliases and output names) is never mentioned. A vague "needs improvement on joins" sends the student to study something they already did well.

**Rewrites:**

**1. Correct but slow (SELECT * plus subquery)**

> Your query returns the right rows, so the logic is sound. Two things to look at:
>
> - The subquery does the same work a join can do. On the sample data, the join version runs about 3x faster. Try rewriting it with a join, then compare the two with `EXPLAIN`.
> - `SELECT *` pulls every column, including ones you don't use. List only the columns you need. That makes the output easier to read, and the query won't break if the table changes later.
>
> Once you've rewritten it, check that your row count still matches.

**2. INNER JOIN drops customers with no orders**

> Your query counts orders correctly for customers who have them. But the exercise asks for *every* customer, and customers with zero orders are missing from your result.
>
> The cause is `INNER JOIN`: it keeps only customers who have a matching row in `orders`. A customer with no orders has no match, so the row is removed.
>
> To fix it, change the join so all customers are kept even without a match. Then check what `COUNT(...)` returns for those customers. Counting a column from `orders` gives 0 for them, but `COUNT(*)` gives 1. Try both and see why.
>
> To check your fix, compare the number of rows in your result with `SELECT COUNT(*) FROM customers`. They should be equal.

**3. Correct and clean, but aliases `a`/`b` and confusing output names**

> Your join logic and result are correct, and the query is cleanly structured. The one thing to fix is naming.
>
> - **Aliases:** `a` and `b` force the reader to scroll back and work out which table is which. Use short names that say what the table is, such as `c` for `customers` and `o` for `orders`, or just `cust` and `ord`.
> - **Output columns:** the result headers are hard to read. Add `AS` names that describe the value, for example `customer_name` and `order_count`.
>
> Imagine a teammate reading this in six months. Could they tell what each column holds without opening the query?

**What these have in common:** each one says what was right, names the specific issue and why it matters, and gives a concrete next step. In #2 the student can also check their own fix. A TA can write one of these in a couple of minutes once they've read the query closely.

**Rubric for TAs:** before sending a comment, check that it (1) names something specific in the student's query, (2) explains the consequence, and (3) gives one next action. Scores like "6/10" can stay if your program requires them, but only alongside those three things.

**Note:** I assumed the bootcamp's goal is that students can fix and self-check their own queries. If you also want a standard for what counts as full marks, such as whether `SELECT *` loses points, fill in [grading criteria]. I didn't invent one.
