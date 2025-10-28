class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for e in sorted(nums):
            if nums.count(e) > 2:
                nums.pop(nums.index(e))
