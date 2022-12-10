class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        freq_val = 0
        for e in nums:
            if e == val:
                freq_val+=1

        for _ in range(freq_val):
            idx = nums.index(val)
            nums.pop(idx)

        return len(nums)
