class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        farr = [e for e in arr if arr.count(e) == 1]
        if len(farr) < k:
            return ""
        else:
            return farr[k - 1]
