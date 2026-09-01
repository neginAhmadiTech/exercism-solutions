class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

        self.total_minutes = ((self.hour * 60) + self.minute) % 1440

    def __repr__(self):
        return f"Clock({"0" if self.hour==24 else f"{self.hour}"}, {self.minute})"

    def __str__(self):
        return f"{self.total_minutes//60:02d}:{self.total_minutes%60:02d}"

    def __eq__(self, other):

        return self.total_minutes == other.total_minutes

    def __add__(self, minutes):

        self.total_minutes += minutes

        return Clock(self.total_minutes // 60, self.total_minutes % 60)

    def __sub__(self, minutes):
        self.total_minutes -= minutes

        return Clock(self.total_minutes // 60, self.total_minutes % 60)
