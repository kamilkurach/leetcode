class Solution:
    def dayOfYear(self, date: str) -> int:
        y = int(date.split("-")[0])
        m = int(date.split("-")[1])
        d = int(date.split("-")[2])
        return datetime.date(y, m, d).timetuple().tm_yday
        