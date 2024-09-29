class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for e in nums1:
            if e in nums2:
                result.append(e)
                idx = nums2.index(e)
                nums2.pop(idx)
        return result
