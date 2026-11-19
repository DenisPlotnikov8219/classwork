[homework 1.11.py](https://github.com/user-attachments/files/35098431/homework.1.11.py)
class Time:
    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0):

        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

        self._normalize()

    def _normalize(self):

        total_sec = self.hours * 3600 + self.minutes * 60 + self.seconds

        seconds_in_day = 86400

        total_sec = total_sec % seconds_in_day

        self.hours = total_sec // 3600
        self.minutes = (total_sec % 3600) // 60
        self.seconds = total_sec % 60

    def __add__(self, other):

        if not isinstance(other, Time):
            return NotImplemented

        total_sec = (self.hours * 3600 + self.minutes * 60 + self.seconds) + \
                    (other.hours * 3600 + other.minutes * 60 + other.seconds)

        return Time(seconds=total_sec)

    def __str__(self):

        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def __repr__(self):

        return f"Time(hours={self.hours}, minutes={self.minutes}, seconds={self.seconds})"

    def total_seconds(self) -> int:

        return self.hours * 3600 + self.minutes * 60 + self.seconds
