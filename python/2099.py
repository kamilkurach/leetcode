class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        while len(nums) != k:
            idx = nums.index(min(nums))
            nums.pop(idx)
        return nums
