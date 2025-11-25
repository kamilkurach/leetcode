class Solution:
    def clearDigits(self, s: str) -> str:
        while any(e.isdigit() for e in s) is True:
            s = re.sub(r'[a-z][0-9]', '', s)
        return s
