class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        result = []
        for e in nums: 
            result.append(int(str(e)[::-1]))
        return len(list(set(result + nums)))
