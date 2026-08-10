```
days = [("number", "gift"),...]
first_sentence = "On the {number} day of Christmas my true love gave to me: "

gifts = []
for start_verse to 1:
    if start_verse == 1:
        gifts.append("and " + days[start_verse-1][1])

    gifts.append(days[start_verse-1][1])

for start_verse + 1  to end_verse:
    gifts.append(days[start_verse][1])
```
