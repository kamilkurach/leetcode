class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        result = []
        for e in nums:
            if nums.count(e) > 1 and e not in result:
                result.append(e)
        return result
