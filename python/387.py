# 387. First Unique Character in a String
class Solution:
    def firstUniqChar(self, s: str) -> int:
        visited = []
        for l in s:
            if l not in visited:
                if s.count(l) == 1:
                    return s.index(l)
                else:
                    visited.append(l)
        return -1
