#3131. Find the Integer Added to Array I
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return list(set([a - b for a, b in zip(sorted(nums2), sorted(nums1))])).pop(0)
