class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # check for distinct pairs
        arr = []
        for i in range(len(s)):
            if (s[i], t[i]) not in arr:
                arr.append((s[i], t[i]))
        
        if len(set(s)) == len(set(t)) == len(arr):
            return True
        else:
            return False