class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[0:] = sorted(set(nums))
        return len(nums)
