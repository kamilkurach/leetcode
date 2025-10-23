class Solution:
    def maxFreqSum(self, s: str) -> int:
        arr =  ['a','e','i','o','u']
        c = max([s.count(e) for e in s if e not in arr], default=0)
        v = max([s.count(e) for e in s if e in arr], default=0)
        return c + v
