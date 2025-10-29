class Solution:
    def smallestNumber(self, n: int) -> int:
        c = n
        while c >= n:
            if "0" not in bin(c)[2:]:
                return c
            else:
                c += 1
