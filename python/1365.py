class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for x in nums:
            count = sum(1 for e in nums if e < x)
            result.append(count)
        return result
        
