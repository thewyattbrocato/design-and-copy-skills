## What's wrong with them

1. **"Good job!"** is praise with no information. It doesn't say what worked, and it hides the one real improvement the student could make. The SELECT * and the 3x slowdown are the useful part of the feedback, and they're missing.

2. **"Your query is wrong. See the solution."** says there's a problem but not what it is. The student can't tell whether the issue is the join, the filter, or the output. "See the solution" ends the learning: the student copies the answer and doesn't learn why INNER JOIN drops customers with no orders.

3. **"Great effort. Needs improvement on joins. 6/10"** has three problems. "Great effort" is vague praise. "Needs improvement on joins" is wrong about this submission, since the joins return the correct result. The score has no stated basis, so the student can't tell what cost points. The actual issue, unreadable aliases and column names, is never named.

Across all three, the comments describe the grade or the verdict but not the specific thing in the query, and they don't tell the student what to do next.

## Rewrites

**1.**
> Your query returns the right rows, so the logic is sound. Two things to tighten:
>
> - `SELECT *` pulls every column. List only the ones you need so the next reader knows what the query produces.
> - The subquery works, but a JOIN does the same job here and runs about 3x faster on the sample data. Rewrite it as a join against the same tables and compare the timings. Knowing why one approach is faster is worth building.

**2.**
> This doesn't meet the requirement. The exercise asks for every customer, including those with no orders. An INNER JOIN keeps only rows that match on both sides, so customers with zero orders drop out of the result.
>
> Look at what a LEFT JOIN does with unmatched rows, and at how `COUNT(*)` differs from `COUNT(o.order_id)` when the joined side is NULL. Then check your output: is the zero-order customer there, and what does their count show? If the join direction is still unclear after that, come to office hours and we'll work through it together.

**3.**
> Your query returns the correct result and the structure is clean. The main thing to fix is readability:
>
> - Aliases `a` and `b` make it hard to tell which table each column comes from. Use short names that mean something, like `c` for customers and `o` for orders.
> - Give output columns names that describe them. A column called `count` or left unaliased tells the reader nothing; `order_count` does.
>
> I deducted points for readability, so that's where to focus on the next pass. [If there's a rubric line for this, cite it here. If there isn't, don't include a score.]

The third one shows the pattern to keep. Only give a score if you can point to the criterion behind it. A number without a stated basis reads as arbitrary, and students will assume it is.

## The pattern

Each good TA comment does four things: it says what the student did right, names the specific line or behavior that needs changing, explains why it matters (correctness, speed, or readability), and gives a next step that doesn't hand over the answer. If you want, I can draft a short checklist of these for the TAs or review a few more comments from this week.
