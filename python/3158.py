class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        t = list(set([e for e in nums if nums.count(e) == 2]))
        result = 0
        for e in t:
            result = result ^ e
        return result
