#3168. Minimum Number of Chairs in a Waiting Room
class Solution:
    def minimumChairs(self, s: str) -> int:
        tmp_state = 0
        peak_state = 0
        for action in s:
            if action == "E":
                tmp_state += 1
            elif action == "L":
                tmp_state -= 1
            if tmp_state > peak_state:
                peak_state = tmp_state
        return peak_state
