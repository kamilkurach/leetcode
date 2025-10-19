class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        tab = []
        for e in word:
            if e != e.upper() and e.upper() in word and e not in tab:
                count+=1
                tab.append(e)
        return count
