class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        word = ""
        for e in words:
            word = word + e[0]
        if word == s:
            return True
        else:
            return False
