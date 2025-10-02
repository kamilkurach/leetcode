class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        diff = -1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j and j < len(nums) and nums[i] < nums[j]:
                    if nums[j] - nums[i] > diff:
                        diff = nums[j] - nums[i] 
        return diff
