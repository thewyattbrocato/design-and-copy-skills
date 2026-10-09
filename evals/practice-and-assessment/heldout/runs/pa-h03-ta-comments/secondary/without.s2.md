**What's wrong with each comment**

1. **"Good job!"** is praise with no content. The student can't tell what worked, and the real issues (`SELECT *`, the subquery, the 3x slowdown) go unmentioned. A student who hears "good job" on a slow query has no reason to change it.
2. **"Your query is wrong. See the solution."** doesn't say what's wrong. It also gives the answer away and treats the student as someone to correct rather than someone learning. The actual bug, that INNER JOIN drops customers with no orders, is a concept the student should reason through.
3. **"Great effort. Needs improvement on joins. 6/10"** has three problems. The join logic was correct, so "needs improvement on joins" misdiagnoses the issue, which is readability. "Great effort" and a score with no rationale give the student nothing to act on. And 6/10 is hard to square with a correct result unless the rubric weights style, which the student can't see.

**Rewrites**

1. "Your query returns the right rows, which is the hard part. Two things to level up:
   - `SELECT *` returns every column, including ones you don't use. Naming the columns you need makes the query's intent clear and keeps it stable if the table changes.
   - The subquery works, but a JOIN does the same job here and runs about three times faster on the sample data. Rewrite it as a join and compare the two. Which would you expect to hold up better as the tables grow, and why?"

2. "Look at the requirement again: every customer should appear, including those with no orders. Run your query and compare the row count to the number of customers. What's the difference? Think about what INNER JOIN does with a customer who has no matching row in `orders`. Is there a join type that keeps the left-side rows even without a match?"

3. "The result is correct and the query is clean. The points come from readability:
   - The aliases `a` and `b` make every join condition harder to follow. Use names that say what the table holds, like `c` for customers and `o` for orders.
   - The output column `[name]` doesn't say what it contains. Use `AS` to give it a name a reader would understand, such as `order_count`.
   
   The score should map to a rubric criterion. Tell the student which one lost points so they know what to fix. [Note: I don't have your rubric, so fill in which criterion the 6/10 reflects.]"

**General pattern**

A useful TA comment does four things: names one specific thing that worked, names one specific thing to change, explains why it matters (often the consequence, like missing rows or slower runtime), and ends with a question or hint that leads the student to the fix. If the comment includes a grade, it should also say which criterion it reflects.

If you share the rubric and the actual column names from comment 3, I can tighten those rewrites further.
