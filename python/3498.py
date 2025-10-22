class Solution:
    def reverseDegree(self, s: str) -> int:
        alphabet = sorted([chr(e) for e in range(97, 123)], reverse=True)
        result = 0
        for i, e in enumerate(s):
            result = result + ((i + 1) * (alphabet.index(e) + 1))
        return result
