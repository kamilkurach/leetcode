class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for e in nums:
            if e%2 == 0:
                even.append(e)
            else:
                odd.append(e)
        return even + odd
