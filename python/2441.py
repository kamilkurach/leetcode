class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        while len(nums) != 0:
            m = max(nums)
            if -m in nums:
                return m
            else:
                nums.pop(nums.index(m))
        return -1
            
