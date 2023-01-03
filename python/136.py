class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for e in nums:
            if nums.count(e) == 1:
                return e
