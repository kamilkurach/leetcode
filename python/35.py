class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        elif target > nums[len(nums)-1]:
            return len(nums)
        else:
            for i, e in enumerate(nums):
                if target < e:
                    return i
