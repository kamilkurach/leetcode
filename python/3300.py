class Solution:
    def minElement(self, nums: List[int]) -> int:
        result = 0
        for e in nums:
            s = sum(map(int, str(e)))
            if result == 0:
                result = s
            elif result > s:
                result = s
        return result
