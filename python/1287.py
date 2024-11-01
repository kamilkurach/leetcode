# 1287. Element Appearing More Than 25% In Sorted Array
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        p = int(len(arr)*0.25)
        for e in arr:
            if arr.count(e) > p:
                return e
