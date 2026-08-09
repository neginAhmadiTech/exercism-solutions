```
target
exclude
result = []
solve(size, candidate, start, current_sum) {

    <!-- base case -->
    if size == 0:
        if current_sum == target:
            result.append(candidate)
        return

    for number=start number<=9 number++:
        if number in exclude:
            continue

        candidate.append(number)
        new_sum = current_sum + number

        if new_sum > target:
            candidate.pop()
            continue

        solve(size - 1, candidate, number+1, new_sum)
        candidate.pop()

}
```
