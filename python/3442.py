class Solution:
    def maxDifference(self, s: str) -> int:
        odd = [s.count(e) for e in list(set(s)) if s.count(e)%2 != 0]
        even = [s.count(e) for e in list(set(s)) if s.count(e)%2 == 0]
        return max(odd) - min(even)
