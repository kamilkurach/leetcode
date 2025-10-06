class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([e for e in nums if len(str(e)) % 2 == 0])
