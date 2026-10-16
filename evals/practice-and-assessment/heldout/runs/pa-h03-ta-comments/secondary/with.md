**What's wrong with each comment**

1. **"Good job!"** The student gets no information. It also hides the real issues: `SELECT *`, and a subquery that runs about three times slower than the join. A student reading "Good job!" would reasonably conclude the query is fine.
2. **"Your query is wrong. See the solution."** It says the query is wrong but not why. The student can't tell whether the problem is the join, the grouping, or the count. Pointing to the solution ends the learning step, and the student can copy it without understanding the outer-join idea they need.
3. **"Great effort. Needs improvement on joins. 6/10"** It points at the wrong problem. The joins are correct, and the actual issue is naming. The score has no breakdown, so the student can't tell what cost points.

**Rewrites**

1. "The result is correct, so the logic is sound. Two things to improve:
   - `SELECT *` returns every column. List only the columns you need. It's easier to read and doesn't break when the table changes.
   - The subquery can be a join. On the sample data your version runs about 3x slower. Rewrite it as a join and time both versions. Which would you choose on a table with a million rows, and why?"

2. "The task asks for every customer, including those with no orders. An INNER JOIN drops any customer without a matching row in `orders`, so those customers disappear from the result. Ask yourself which table's rows must be kept no matter what, and which join type keeps unmatched rows from that side. After you change the join, check what a customer with zero orders shows in the count. Hint: `COUNT(*)` counts the padded row as 1, but `COUNT(column)` ignores NULLs. Come to office hours if you get stuck on this."

3. "Your joins are correct, and the result is right. The 6/10 comes from readability, not from the join logic. The aliases `a` and `b` don't tell a reader which table is which. Use short names that mean something, like `c` for customers and `o` for orders. Also give the output columns clear names with `AS` (for example `order_count` instead of an unnamed `COUNT(*)`). Once the names are clear, the query should make sense to someone reading it for the first time. [If the rubric has a line item for this, name it here, e.g. 'Naming and clarity: 4/6.']"

**Pattern across the three:** each rewrite names something specific from the student's code, says why it matters, and gives a next step or a question that makes the student do the thinking. The grade explanation ties to the rubric.

I don't have your rubric or schema, so I made up table and column names in the comments. Check the score line in #3 against your rubric. If the 6 comes from a specific criterion, put that criterion in the comment.
