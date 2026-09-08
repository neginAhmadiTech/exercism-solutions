def matches(line, pattern, flags):

    matched_line = False

    if "-i" in flags:
        line = line.lower()
        pattern = pattern.lower()

        if pattern in line:
            matched_line = True

    if "-x" in flags:
        matched_line = pattern == line

    if "-v" in flags:
        if not matched_line and pattern not in line:
            matched_line = True
        elif matched_line:
            matched_line = False

    return matched_line


def print_result(line, flags, line_number, file_address):

    if "-n" in flags:
        line = f"{line_number+1}:{line}"

    if "-l" in flags:
        line = f"{file_address}"

    return line


def search_in_lines(lines, pattern, flags, file_address, files_count):

    result = ""

    match_flags = []
    output_flags = []

    for flag in flags:
        if flag in ("-i", "-x", "-v"):
            match_flags.append(flag)

        if flag in ("-n", "-l"):
            output_flags.append(flag)

    for line_number, line in enumerate(lines):

        keep_line = False
        if match_flags:
            if matches(line, pattern, match_flags):

                keep_line = True
                if output_flags:
                    line = print_result(line, output_flags, line_number, file_address)
        else:
            if pattern in line:

                keep_line = True
                if output_flags:
                    line = print_result(line, output_flags, line_number, file_address)

        if files_count > 1 and "-l" not in output_flags:
            line = f"{file_address}:{line}"

        if keep_line and line not in result.split("\n"):

            result += line + "\n"

    return result


def grep(pattern, flags, files):

    if flags:
        flags = flags.split(" ")

    result = ""

    for file_address in files:
        with open(file_address, "r", encoding="utf-8") as file:
            lines = file.readlines()
            lines = list(filter(lambda line: line != "\n", lines))
            lines = [line.replace("\n", "") for line in lines]

            result += search_in_lines(lines, pattern, flags, file_address, len(files))

    return result
