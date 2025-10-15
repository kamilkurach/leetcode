class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(e for e in nums if nums.count(e) == 1)
