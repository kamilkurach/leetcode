class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = []
        for i, e in enumerate(nums):
            arr.append(sum(nums[:i+1]))
        return arr