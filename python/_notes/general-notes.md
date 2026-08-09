# How do you know which algorithm to use?

## Pattern 1: Need to find all possibilities?

### Examples:

- Generate permutations
- Generate subsets
- Maze paths

### Think: Backtracking

### Question:

"Try choices and undo."

---

## Pattern 2: Need the best/minimum/maximum/count?

### Examples:

- Fewest coins
- Maximum profit
- Shortest path

### Think: Optimization problem

### Then ask:

"Are there overlapping subproblems?"

If yes:

### Dynamic Programming

---

## Pattern 3: Can I always make the best local choice?

### Example:

Coins:
[1,5,10,25]

Take biggest first.

Works.

### Think: Greedy

But prove it first.

---

## Pattern 4: Need to find something in sorted data?

### Think: Binary Search

---

## Pattern 5: Need relationships between items?

### Examples:

- graphs
- networks
- dependencies

### Think: Graph algorithms

---

# How professionals train this skill

- Not by solving 500 random problems.

- By doing problem decomposition exercises.

#### For every problem, before coding, write:

1. What is the input?

2. What is the output?

3. What exactly am I trying to optimize/find?

4. What is the smallest example?

5. If I knew a smaller answer, could I solve the bigger one?

6. What changes between states?

7. What algorithm pattern does this resemble?
