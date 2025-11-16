class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        result = []
        for i, e in enumerate(nums):
            tmp = 0
            for ee in str(e):
                tmp += int(ee)
            if tmp == i:
                result.append(i)
        if len(result) != 0:
            return min(result)
        else:
            return -1
