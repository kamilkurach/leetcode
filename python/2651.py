#2651. Calculate Delayed Arrival Time
class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        delayed_time = arrivalTime + delayedTime
        if delayed_time == 24:
            return 0
        elif delayed_time > 24:
            return delayed_time - 24
        else:
            return delayed_time
