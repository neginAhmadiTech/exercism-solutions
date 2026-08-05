- **Top-down DP** → usually recursion + memoization
- **Bottom-up DP** → usually loops + a DP table

Both solve the same recurrence. The only difference is the order in which subproblems are solved.

---

## Which one should you choose?

That depends on the problem.

### Choose Top-down when...

✅ The recurrence is easy to write recursively.

#### Example:

- Longest Increasing Subsequence
- DFS on trees
- Game DP
- Backtracking + memoization

#### You simply describe:

"The answer for this state depends on these smaller states."

The code often mirrors the mathematical definition and can be easier to write.

### Choose Bottom-up when...

✅ There are many states.

✅ The dependency order is obvious.

#### Example:

- Coin Change
- Fibonacci
- Edit Distance
- Knapsack
- Grid DP

A loop is often simpler and avoids recursion limits.

---

### A mental model that many experienced programmers use

#### Think of DP in two layers:

##### The algorithm:

define the state and the recurrence. This is the heart of the solution.

##### The implementation:

decide whether to evaluate that recurrence top-down (recursion + memoization) or bottom-up (iteration).

Once you can derive the recurrence, switching between top-down and bottom-up often becomes a matter of changing how you compute the same formula rather than inventing a new algorithm. This is a powerful way to think about DP problems because it separates the mathematical idea from the coding technique.
