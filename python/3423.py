class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        circular = nums[:len(nums)] + nums[-len(nums):-1]
        diff = 0
        for i in range(len(circular) - 1):
            if abs(circular[i] - circular[i + 1]) > diff:
                diff = abs(circular[i] - circular[i + 1])
        return diff
