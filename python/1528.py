class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        sorted_s = sorted(zip(s, indices), key=lambda x: x[1])
        return "".join([e[0] for e in sorted_s])
