"""Module to set the deadline of a delivery date
    based on the given description
"""
from datetime import datetime, timedelta

def delivery_date(start, description):
    """Set the deadline of a delivery date
    based on the given description

    Args:
        start (str): start date
        description (str): the given description code

    Returns:
        str: delivery date
    """

    deadline = datetime.strptime(start, "%Y-%m-%dT%H:%M:%S")
    hour = deadline.strftime('%H')
    today = deadline.strftime('%A')
    weekday = deadline.weekday()
    month = deadline.strftime('%m')
    # print(month)

    if description == "NOW":
        deadline += timedelta(hours=2)

    elif description == "ASAP":
        if int(hour) < 13:
            deadline = deadline.replace(hour=17, minute=00, second=00)

        else:
            deadline += timedelta(days=1)
            deadline = deadline.replace(hour=13, minute=00, second=00)

    elif description == "EOW":

        if today in ("Monday", "Tuesday", "Wednesday"):
            deadline += timedelta(days = 4 - weekday)
            deadline = deadline.replace(hour=17, minute=00, second=00)

        elif today in ("Thursday", "Friday"):
            deadline += timedelta(days = 6 - weekday)
            deadline = deadline.replace(hour=20, minute=00, second=00)

    elif description.endswith("M"):
        deadline_month = int(description[:len(description)-1])

        if deadline_month <= int(month):
            deadline = deadline.replace(year=deadline.year + 1)

        deadline = deadline.replace(month=deadline_month, day=1, hour=8, minute=00, second=00)
        new_weekday = deadline.weekday()

        if new_weekday == 5:
            deadline += timedelta(days=2)
        elif new_weekday == 6:
            deadline += timedelta(days=1)

    elif description.startswith("Q"):
        quarter = int(description[1:])
        last_month = quarter * 3
        current_quarter = (int(month) - 1) // 3 + 1

        if current_quarter > quarter:
            deadline = deadline.replace(year=deadline.year + 1)

        if last_month == 12:
            last_month = 0
            deadline = deadline.replace(year=deadline.year + 1)            

        deadline = deadline.replace(month=int(last_month) + 1,day=1, hour=8, minute=00, second=00)
        deadline += timedelta(days=-1)

        new_weekday = deadline.weekday()

        if new_weekday == 5:
            deadline += timedelta(days=-1)
        elif new_weekday == 6:
            deadline += timedelta(days=-2)


    deadline_formatted = datetime.strftime(deadline, "%Y-%m-%dT%H:%M:%S")

    return deadline_formatted
