import re


def make_headings(line):

    if re.match("###### (.*)", line):

        line = "<h6>" + line[7:] + "</h6>"

    elif re.match("##### (.*)", line):

        line = "<h5>" + line[6:] + "</h5>"

    elif re.match("#### (.*)", line):

        line = "<h4>" + line[5:] + "</h4>"

    elif re.match("### (.*)", line):

        line = "<h3>" + line[4:] + "</h3>"

    elif re.match("## (.*)", line):

        line = "<h2>" + line[3:] + "</h2>"

    elif re.match("# (.*)", line):

        line = "<h1>" + line[2:] + "</h1>"

    return line


def make_bold(match):
    return match.group(1) + "<strong>" + match.group(2) + "</strong>" + match.group(3)


def make_italic(match):
    return match.group(1) + "<em>" + match.group(2) + "</em>" + match.group(3)


def find_bold_match(item):
    return re.match("(.*)__(.*)__(.*)", item)


def find_italic_match(item):
    return re.match("(.*)_(.*)_(.*)", item)


def make_list_item(item):
    return "<li>" + item + "</li>"


def parse(markdown):
    lines = markdown.split("\n")
    result = ""
    item_in_list = False
    item_added_to_list = False
    for line in lines:

        line = make_headings(line)

        unordered_list = re.match(r"\* (.*)", line)

        if unordered_list:
            current_item = unordered_list.group(1)

            # make html bold sign
            bold_match = find_bold_match(current_item)

            if bold_match:
                current_item = make_bold(bold_match)

            # make html italic sign
            italic_match = find_italic_match(current_item)
            if italic_match:
                current_item = make_italic(italic_match)

            # makes the first list item
            if not item_in_list:
                item_in_list = True
                line = "<ul>" + make_list_item(current_item)

            else:  # makes other list items
                line = make_list_item(current_item)
        else:
            if item_in_list:
                item_added_to_list = True
                item_in_list = False

        another_tag_open = re.match("<h|<ul|<p|<li", line)

        if another_tag_open is None:
            line = "<p>" + line + "</p>"

        bold_match = find_bold_match(line)
        if bold_match:
            line = make_bold(bold_match)

        italic_match = find_italic_match(line)
        if italic_match:
            line = make_italic(italic_match)

        if item_added_to_list:
            # ends the list
            line = "</ul>" + line
            item_added_to_list = False
        result += line

    if item_in_list:
        result += "</ul>"

    return result
