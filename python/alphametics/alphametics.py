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
    print(max(operands_max_size, len(equation_result)), equation_result)
    equation_operands = [
        " " * ((max(operands_max_size, len(equation_result))) - len(operand)) + operand
        for operand in equation_operands
    ]

    # print(equation_operands, max(equation_operands))

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

            # if operands_sum > equation_operand_after_assign:
            #     return False
        # print(equation_result_after_assign, operands_sum)
        return equation_result_after_assign == operands_sum

    # is_equation_correct(
    #     {"S": 9, "E": 5, "N": 6, "D": 7, "M": 1, "O": 0, "R": 8, "Y": 2}
    # )
    # 3,4

    def continue_this_branch(assignments):
        # print(assignments)
        carry = 0
        for column in range(len(equation_result) - 1, -1, -1):

            if equation_result[column] not in assignments:
                return True
            # print("res: ", column, equation_result[column])

            result_digit = assignments[equation_result[column]]

            operands_digit = 0
            for operand in equation_operands:
                if operand[column] != " " and operand[column] not in assignments:
                    # print(operand[column])
                    return True

                # print(operand[column])

                if operand[column] != " ":
                    operands_digit += assignments[operand[column]]

            total = operands_digit + carry
            if total % 10 != result_digit:
                return False

            # print(
            #     "COLUMN " + str(column),
            #     "result: " + str(result_digit),
            #     # "operands: " + str(equation_operands),
            #     "incoming carry: " + str(carry),
            #     "total: " + str(operands_digit + carry),
            #     "expected digit: " + str((total) % 10),
            #     "outgoing carry: " + str((total) // 10),
            # )

            # assert total == ((total) % 10) + 10 * ((total) // 10)

            carry = total // 10

        return True

    # assignments = {}
    # assignments = {"A": 9}
    # assignments = {"A": 9, "B": 1, "C": 0}

    # print(continue_this_branch(assignments))
    nodes_visited = 0

    def find_solution(assignments, used_digits):
        print("DEPTH:", len(assignments), assignments)
        # if nodes_visited % 100_000 == 0:
        # print("nodes:", nodes_visited)
        # nodes_visited += 1

        # base case
        if len(assignments) == len(letters):
            if is_equation_correct(assignments):
                return assignments

            return None

        # print(letters - assignments.keys())

        for letter in [
            letter for letter in letters if letter not in assignments.keys()
        ]:
            # available_digits = [
            #     digit for digit in range(10) if digit not in used_digits
            # ]
            for digit in sorted(set(list(range(10))) - used_digits):
                # print(
                #     "BEFORE:",
                #     "letter =",
                #     letter,
                #     "digit =",
                #     digit,
                #     "assignments =",
                #     assignments,
                #     "used =",
                #     used_digits,
                # )
                # print(digit)
                if (letter in leading_letters and digit == 0) or letter in assignments:
                    continue

                    # if digit not in used_digits:
                assignments[letter] = digit
                used_digits.add(digit)
                # print(assignments, used_digits)

                # print("AFTER:", "assignments =", assignments, "used =", used_digits)

                # print("➡️ CHOOSE", letter, digit, assignments, used_digits)

                # pruning
                if continue_this_branch(assignments):
                    result = find_solution(assignments, used_digits)
                else:
                    # print(
                    #     "❌ Couldn't continue this branch",
                    #     letter,
                    #     digit,
                    #     assignments,
                    #     used_digits,
                    # )
                    result = None

                if result:
                    return result

                # print("⬅️ BACKTRACK", letter, digit, assignments, used_digits)

                del assignments[letter]
                used_digits.remove(digit)

                # print("🔄 AFTER UNDO", assignments, used_digits)

        return None
        # print(result)

    # print(leading_letters, equation_result, letters, equation_operands)

    # unused_digits = list(range(0, 10))
    result = find_solution({}, set())
    # result = 0
    # print(result)

    return result


# solve("A + A + A + A + A + A + A + A + A + A + A + B == BCC")
# {"A": 9, "B": 1, "C": 0},
solve("SEND + MORE == MONEY")
# solve("NO + NO + TOO == LATE")
# solve("AS + A == MOM")
# is_equation_correct(
#     {"S": 9, "E": 5, "N": 6, "D": 7, "M": 1, "O": 0, "R": 8, "Y": 2}
# )
# 3,4
