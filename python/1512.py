class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i, _ in enumerate(nums):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    count += 1
        return count
