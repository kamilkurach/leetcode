class Solution:
    def alternateDigitSum(self, n: int) -> int:
        result = 0
        for i, e in enumerate(list(str(n))):
            if i % 2 == 0:
                result+=int(e)
            else:
                result-=int(e)
        return result
