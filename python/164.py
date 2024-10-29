class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        result = 0
        s_nums = sorted(nums)
        for i in range(len(s_nums) - 1):
            gap = s_nums[i+1] - s_nums[i]
            if gap > result:
                result = gap
        return result
