class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        for i in range(1, len(nums)):
            result = result * nums[i]
        if result > 0:
            return 1
        elif result < 0:
            return -1
        elif result == 0:
            return 0
