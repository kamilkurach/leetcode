class Solution:
    def sortSentence(self, s: str) -> str: 
        tab = sorted(s.split(" "), key=lambda x: x[-1])
        clean_tab = [e[:-1] for e in tab]
        return " ".join(clean_tab)
