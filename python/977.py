class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([e**2 for e in nums])
        