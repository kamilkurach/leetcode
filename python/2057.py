class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        result = []
        for i, e in enumerate(nums):
            if i % 10 == e:
                result.append(i)

        if len(result) != 0:
            return min(result)
        else:
            return -1
