class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i, e in enumerate(sorted(nums)):
            if e == target:
                result.append(i)
        return result
