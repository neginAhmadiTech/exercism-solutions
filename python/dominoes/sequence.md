BACKTRACKING — DOMINOES

1. STATE
   used_dominoes
   unused_dominoes

2. CHOICES
   choose an unused domino
   choose its orientation

3. CONSTRAINT
   - first domino → no previous connection needed 
   - for the second domino-> need to consider both orientations of the first one too
   - every other domino → must connect to previous domino
   - after all dominoes are used → last must connect to first

4. BASE CASE
   unused_dominoes is empty
       AND
   last connects to first
       → solution

5. BACKTRACK
   choose valid domino
   add it
   recurse
   if path fails:
       undo the choice
       try another choice