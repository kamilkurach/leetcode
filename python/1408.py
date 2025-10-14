class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        tab = []
        for word in words:
            for word2 in words:
                if word in word2 and word != word2 and word not in tab:
                    tab.append(word)
        return tab
