class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = sum(int(e) for e in str(x))
        if x % s == 0:
            return s
        else:
            return -1
