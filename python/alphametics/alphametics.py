def solve(puzzle):

    letters = []
    for letter in puzzle:
        if letter.isalpha():
            if letter not in letters:
                letters.append(letter)

    splitted_puzzle = puzzle.split("==")
    equation_result = splitted_puzzle[1].strip()
    equation_operands = [operand.strip() for operand in splitted_puzzle[0].split("+")]
    operands_max_size = max(len(operand) for operand in equation_operands)
    equation_operands = [
        " " * ((max(operands_max_size, len(equation_result))) - len(operand)) + operand
        for operand in equation_operands
    ]

    leading_letters = set(
        [operand[0] for operand in equation_operands] + [equation_result[0]]
    )

    def is_equation_correct(assignments):
        equation_result_after_assign = int(
            "".join([str(assignments[letter]) for letter in equation_result])
        )

        operands_sum = 0
        for operand in equation_operands:

            equation_operand_after_assign = int(
                "".join([str(assignments[letter]) for letter in operand.strip()])
            )

            operands_sum += equation_operand_after_assign

        return equation_result_after_assign == operands_sum

    def continue_this_branch(assignments):
        carry = 0
        for column in range(len(equation_result) - 1, -1, -1):

            if equation_result[column] not in assignments:
                return True

            result_digit = assignments[equation_result[column]]

            operands_digit = 0
            for operand in equation_operands:
                if operand[column] != " " and operand[column] not in assignments:
                    return True

                if operand[column] != " ":
                    operands_digit += assignments[operand[column]]

            total = operands_digit + carry
            if total % 10 != result_digit:
                return False

            carry = total // 10

        return True

    def find_solution(assignments, used_digits):

        # base case
        if len(assignments) == len(letters):
            if is_equation_correct(assignments):
                return assignments

            return None

        for letter in [
            letter for letter in letters if letter not in assignments.keys()
        ]:

            for digit in sorted(set(list(range(10))) - used_digits):
                if (letter in leading_letters and digit == 0) or letter in assignments:
                    continue

                assignments[letter] = digit
                used_digits.add(digit)

                # pruning
                if continue_this_branch(assignments):
                    result = find_solution(assignments, used_digits)
                else:
                    result = None

                if result:
                    return result

                del assignments[letter]
                used_digits.remove(digit)

        return None

    result = find_solution({}, set())

    return result
