class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for e in set(nums):
            if nums.count(e) > len(nums)/2:
                return e
