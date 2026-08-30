import calendar
from datetime import date

DAYS_OF_WEEK = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}

WEEKS = {"first": 0, "second": 1, "third": 2, "fourth": 3, "fifth": 4, "last": -1}

TEENTH = [13, 14, 15, 16, 17, 18, 19]


# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """

    def __init__(self, message):
        super().__init__(message)


def meetup(year, month, week, day_of_week):
    calendar_object = calendar.Calendar()

    days_in_month = []
    for month_week in calendar_object.monthdays2calendar(year, month):
        for month_day, week_day in month_week:
            if month_day > 0 and week_day == DAYS_OF_WEEK[day_of_week]:
                days_in_month.append((month_day, week_day))

    day = None
    if week == "teenth":
        days = [day for day in days_in_month if day[0] in TEENTH]
        day = days[0][0]
    else:
        if len(days_in_month) < 5 and week == "fifth":
            raise MeetupDayException("That day does not exist.")

        day = days_in_month[WEEKS[week]][0]

    return date(year, month, day)
