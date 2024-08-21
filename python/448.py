class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = set(list(range(1, len(nums)+1))) - set(nums)
        return list(result)
