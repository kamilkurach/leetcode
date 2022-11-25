class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i, e in enumerate(nums):
            num = target - nums[i]
            match_index = [j for j in range(i+1, len(nums)) if nums[j]==num]
            if len(match_index) != 0:
                if nums[i] + num == target:
                    return [i, *match_index]
                    