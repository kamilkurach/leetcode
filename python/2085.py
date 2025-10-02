class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        w1 = set([e for e in words1 if words1.count(e) == 1])
        w2 = set([e for e in words2 if words2.count(e) == 1])
        return len(list(w1.intersection(w2)))
        
