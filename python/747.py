class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        snums = sorted(nums)
        if snums[-1] >= snums[-2] * 2:
            return nums.index(snums[-1])
        else:
            return -1
