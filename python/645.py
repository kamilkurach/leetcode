class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l = list(range(1, len(nums)+1))
        missing = set(l)-set(nums)
        for e in nums:
            if nums.count(e) > 1:
                return [e, *missing]
