class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word1 = [e for e in s1.split() if s1.split().count(e) == 1 and e not in s2.split()]
        word2 = [e for e in s2.split() if s2.split().count(e) == 1 and e not in s1.split()]
        return word1 + word2
