#961. N-Repeated Element in Size 2N Array
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)/2
        for element in nums:
            if nums.count(element) == n:
                return element
