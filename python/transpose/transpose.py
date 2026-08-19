def transpose(text):
    if not text:
        return ""

    rows = text.splitlines()
    max_length = max(map(len, rows))

    result = []

    for col in range(max_length):
        transposed_row = ""

        for row_index, row in enumerate(rows):

            # does this row have a character at this column?
            if col < len(row):
                transposed_row += row[col]
            elif any(col < len(r) for r in rows[row_index + 1 :]):
                transposed_row += " "

        result.append(transposed_row)

    return "\n".join(result)
