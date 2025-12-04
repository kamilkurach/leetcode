class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if any([True for e in str(n) if int(e) != 0]):
            n = str(n).replace('0', '')
            s = sum([int(e) for e in n])
            return int(n) * s
        else:
            return 0
