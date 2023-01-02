class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = ""
        result = []
        for e in num:
            n = n + str(e)
        a = int(n) + k
        for e in str(a):
            result.append(int(e))
        return result