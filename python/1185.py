class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
         arr = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
         tm_wday = datetime.date(year, month, day).timetuple().tm_wday
         return arr[tm_wday]
         