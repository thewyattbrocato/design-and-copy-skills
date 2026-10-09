**What's wrong with all three**

- **They don't point to anything in the work.** A student can't tell which line or decision the comment is about.
- **They don't say what to do next.** "See the solution" and "needs improvement" leave the student to guess.
- **Their tone doesn't match the content.** Comment 1 praises a query with real problems. Comment 3 gives a score that rates the query below its actual quality.

Each comment fails in its own way:

1. **"Good job!"** is praise with nothing behind it. The query returns the right rows but has two avoidable problems (`SELECT *` and a subquery where a join works, about 3x slower on the sample data). The student learns nothing and will repeat both habits. The praise is also misleading, because it signals nothing needs fixing.
2. **"Your query is wrong. See the solution."** The comment is accurate but gives no diagnosis. The student has no way to learn that INNER JOIN drops customers with zero orders, which is the exact concept the exercise tests. Pointing at the solution makes them compare two queries and guess at the difference. The flat tone also reads as a verdict instead of help.
3. **"Great effort. Needs improvement on joins. 6/10"** is wrong about the content. The joins are fine, since the result is correct and the query is clean. The real issue is readability: the aliases `a` and `b`, and confusing output column names. The comment sends the student to study the wrong topic, and "6/10" has no stated criteria. "Great effort" is also praise for trying, not for the work.

**Rewrites**

1. > Your query returns the right rows, and that's the hard part. Two changes would make it better:
   > - Replace `SELECT *` with only the columns you need. It's faster and won't break if someone adds a column later.
   > - Your subquery can be a plain `JOIN`. On the sample data the join version runs about 3x faster. Try rewriting it and compare the two with `EXPLAIN`.
   >
   > Once you've done that, you'll have a pattern you can reuse: if a subquery just fetches matching rows from another table, a join usually does the same job.

2. > You're close. The structure is right, but the `INNER JOIN` between `customers` and `orders` is dropping customers with zero orders. An inner join keeps only rows that match on both sides, so anyone who has never ordered disappears. The exercise asks for every customer.
   >
   > Try this: change the join so all customers are kept, then run the query and check that the customers with no orders now appear with a count of 0. Think about which table has to be on the "keep everything" side, and what `COUNT(o.order_id)` does with NULLs compared to `COUNT(*)`.
   >
   > If you're stuck after trying that, bring the query to office hours and we'll go through it together.

3. > Your result is correct and your query is clean. Your join logic is solid, so nothing to fix there.
   >
   > One thing to work on is readability. Aliasing the tables as `a` and `b` makes the query hard to follow, because nobody can tell which table is which without scrolling up. Use short names that mean something, like `c` for `customers` and `o` for `orders`.
   >
   > Also, give the output columns clear names with `AS`, for example `customer_name` and `order_count`. A teammate should be able to read your results without seeing the query.

**What the rewrites do**

- Each names the specific thing in the student's query.
- Each says why it matters.
- Each gives a concrete next step.
- Each says what was right, so the student knows what to keep.
- The score is gone from comment 3. If you want to keep scores, publish the criteria so the number means something.

**Suggestion for the TAs:** have them check each comment against three questions: *what did the student do, why does it matter, and what should they do next?* A comment that can't answer all three isn't ready to send.
