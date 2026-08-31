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


def make_bold(unordered_list):
    return (
        unordered_list.group(1)
        + "<strong>"
        + unordered_list.group(2)
        + "</strong>"
        + unordered_list.group(3)
    )


def make_italic(unordered_list):
    return (
        unordered_list.group(1)
        + "<em>"
        + unordered_list.group(2)
        + "</em>"
        + unordered_list.group(3)
    )


def is_bold(item):
    return re.match("(.*)__(.*)__(.*)", item)


def is_italic(item):
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
            if is_bold(current_item):
                current_item = make_bold(is_bold(current_item))

            # make html italic sign
            if is_italic(current_item):
                current_item = make_italic(is_italic(current_item))

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

        if is_bold(line):
            line = make_bold(is_bold(line))

        if is_italic(line):
            line = make_italic(is_italic(line))

        if item_added_to_list:
            # ends the list
            line = "</ul>" + line
            item_added_to_list = False
        result += line

    if item_in_list:
        result += "</ul>"

    return result


# parse("* __Bold Item__\n* _Italic Item_")
# parse("# Header!\n* __Bold Item__\n* _Italic Item_\n* __Bold Item__")
# parse("# Start a list\n* Item 1\n* Item 2\nEnd a list")
parse("# Start a list\n* Item 1\n* Item 2\nEnd a list")
# "<h1>Start a list</h1><ul><li>Item 1</li><li>Item 2</li></ul><p>End a list</p>"
