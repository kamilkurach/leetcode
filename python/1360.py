from datetime import date

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = date.fromisoformat(date1)
        d2 = date.fromisoformat(date2)
        diff = d2 - d1
        return abs(diff.days)
