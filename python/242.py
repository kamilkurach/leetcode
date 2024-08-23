#242. Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

#class Solution:
#    def isAnagram(self, s: str, t: str) -> bool:
#        return set(s) == set(t)
