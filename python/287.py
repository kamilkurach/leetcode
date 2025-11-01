class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tab = set()
        for e in nums:
            if e not in tab:
                tab.add(e)
            else:
                return e
