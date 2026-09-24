## 1. state
letter → digit assignments
+
which digits are already used

## 2. choices
choose an unused number

Choose an unassigned letter
        ↓
Try an unused digit

## 3. constraint
- first letter can not be zero
- numbers given to the letters must be different


## 4. base case
- all letters have a valid number
- the equation is correct

if every letter has been assigned:
    return whether the complete equation is correct

## 5. backtrack
choose a number
if number is_valid:
recurse
else:
undo and try another number

```
choose digit
    ↓
is it allowed?
    ↓
  yes
    ↓
assign it
    ↓
recurse
    ↓
did it find solution?
   / \
 yes  no
 ↓     ↓
done  undo assignment
       ↓
   try next digit
```

```Python
for each possible unused digit:

    if digit violates a constraint:
        continue

    assign digit to letter

    recurse

    if solution found:
        return solution

    undo assignment
```