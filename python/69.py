class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(2147483647):
            if i*i == x:
                return i
            elif i*i > x:
                return i-1
