class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = 0
        for i, e in enumerate(nums):
            if i == 0:
                right_sum = sum(nums[i+1:])
            else:
                left_sum = left_sum + nums[i-1]
                right_sum = sum(nums[i+1:])
            if left_sum == right_sum:
                return i
        return -1