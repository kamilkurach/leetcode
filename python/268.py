# 268. Missing Number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       return set(list(range(len(nums) + 1))).difference(set(nums)).pop()
       
