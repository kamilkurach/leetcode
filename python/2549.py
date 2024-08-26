#2549. Count Distinct Numbers on Board
class Solution:
    def distinctIntegers(self, n: int) -> int:
        s = []
        s.append(n)
        for e in s:
            for i in range(1, e):
                if e%i == 1 and i not in s:
                    s.append(i)
        return len(s)
