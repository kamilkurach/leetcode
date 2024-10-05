class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        prev = []
        for e in set(arr):
            c = arr.count(e)
            if c not in prev:
                prev.append(c)
            else:
                return False
        return True
