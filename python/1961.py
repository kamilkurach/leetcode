class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        concat = ""
        for e in words:
            concat = concat + e
            if concat == s:
                return True
        return False
