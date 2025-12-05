class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        for _ in range(int(len(nums)/2)):
            min_value = nums.pop(nums.index(min(nums)))
            max_value = nums.pop(nums.index(max(nums)))
            averages.append(((min_value + max_value) / 2))
        return min(averages)
