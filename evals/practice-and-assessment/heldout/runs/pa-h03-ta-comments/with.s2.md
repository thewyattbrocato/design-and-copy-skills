**What's wrong with all three**

- **They don't describe the work.** None of them mentions what the query does, so the student can't tell which part to repeat or fix.
- **The verdict doesn't match the work.** #1 praises a query with real problems. #2 and #3 give a judgment with no reason.
- **They don't say what to do next.** "See the solution" sends the student off to compare on their own. "Needs improvement on joins" names a topic that the student's join may not even be the problem with.

**Comment by comment**

1. **"Good job!"** is praise with no content. The student learns nothing about what was good. They also don't learn about the `SELECT *`, the subquery, or the 3x slowdown, so they'll repeat the habits. Praise that is only partly earned also teaches students to distrust the praise that is fully earned.
2. **"Your query is wrong. See the solution."** doesn't say what is wrong. It also hides that the student's logic was sound for a different question. The real cause is a specific misunderstanding about `INNER JOIN` dropping unmatched rows, and the student may not find it by diffing against the solution.
3. **"Great effort. Needs improvement on joins. 6/10"** points at the wrong thing. The join was correct and the query was clean. The actual issue is readability (aliases and output column names), and the comment never says so. The "6/10" has no criteria behind it, and "great effort" praises the student rather than the work.

**Rewrites**

1. > Your query returns the right rows, so the logic is sound. Two things to change:
   > - `SELECT *` pulls every column, including ones you don't use. List only the columns the question asks for.
   > - The subquery runs separately for each row. A join does the same job in one pass. On the sample data your version ran about 3x slower than the join version.
   >
   > Rewrite it as a join with an explicit column list and compare the run times. Then tell me what you see.

2. > The question asks for every customer, including those with no orders. `INNER JOIN` keeps only customers that have a matching row in `orders`, so customers with zero orders drop out of your result.
   >
   > Your join condition and your `COUNT` are set up correctly. The problem is the join type. Try `LEFT JOIN` from `customers` to `orders`, then check that the customers with zero orders now appear with a count of 0.
   >
   > One thing to watch for: `COUNT(*)` would count the NULL row as 1, while `COUNT(orders.order_id)` gives 0. Check which one you used.

3. > Your result is correct, and the query is clean and well structured.
   >
   > The one thing to fix is naming. `a` and `b` are easy to mix up once a query has more than two tables, and a reader has to scroll back to see what they mean. Use short names that say what the table is, like `c` for `customers` and `o` for `orders`, or `cust` and `ord`.
   >
   > The output column names are also unclear. Use `AS` to give them names that tell the reader what they hold, like `order_count`. Try it, and read the output as if you'd never seen the query.

**A pattern TAs can follow**

1. Say what the query does correctly.
2. Name the specific problem and what it caused, using the student's own result.
3. Give one concrete next step.

Drop numeric scores unless the criteria are written down and shared with students. Also drop "good effort" and "needs work on X" when X is too broad to act on. A TA who runs out of time can still do well by writing only step 2 and step 3 on every submission.

I haven't invented any rubric or timing figures beyond what you gave me. The 3x figure comes from your description of comment 1. Comment 2's `COUNT` note assumes the student may have used `COUNT(*)`, so remove it if their code already uses `COUNT(orders.order_id)`.
