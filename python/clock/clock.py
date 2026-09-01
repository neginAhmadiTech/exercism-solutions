class Clock:
    MINUTES_PER_DAY = 24 * 60

    def __init__(self, hour, minute):
        self.total_minutes = ((hour * 60) + minute) % self.MINUTES_PER_DAY

    @property
    def hour(self):
        return self.total_minutes // 60

    @property
    def minute(self):
        return self.total_minutes % 60

    def __repr__(self):
        return f"Clock({self.hour%24}, {self.minute})"

    def __str__(self):
        return f"{self.hour:02d}:{self.minute%60:02d}"

    def __eq__(self, other):

        return self.total_minutes == other.total_minutes

    def __add__(self, minutes):

        total_minutes_updated = self.total_minutes + minutes

        return Clock(total_minutes_updated // 60, total_minutes_updated % 60)

    def __sub__(self, minutes):
        total_minutes_updated = self.total_minutes - minutes

        return Clock(total_minutes_updated // 60, total_minutes_updated % 60)
