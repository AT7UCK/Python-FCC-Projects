def arithmetic_arranger(problems, solve=False):

    # 1. Error: Too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    results = []

    for problem in problems:
        parts = problem.split()

        if len(parts) != 3:
            return "Error: Invalid problem format."

        first, operator, second = parts

        # 2. Error: Operator check
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # 3. Error: Digits only
        if not first.isdigit() or not second.isdigit():
            return "Error: Numbers must only contain digits."

        # 4. Error: Max 4 digits
        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate width
        width = max(len(first), len(second)) + 2

        # Prepare each line
        first_line.append(first.rjust(width))
        second_line.append(operator + second.rjust(width - 1))
        dashes.append("-" * width)

        # If solve is True, calculate result
        if solve:
            if operator == "+":
                answer = str(int(first) + int(second))
            else:
                answer = str(int(first) - int(second))
            results.append(answer.rjust(width))

    # Join with 4 spaces
    arranged = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(dashes)

    if solve:
        arranged += "\n" + "    ".join(results)

    return arranged