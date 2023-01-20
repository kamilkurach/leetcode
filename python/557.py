class Solution:
    def reverseWords(self, s: str) -> str:
        arr = [e[::-1] for e in s.split(" ")]
        return " ".join(arr)
