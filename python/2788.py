class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        for e in words:
            for w in e.split(separator):
                if len(w) != 0:
                    result.append(w)
        return result
