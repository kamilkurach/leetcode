class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min([sum(e) for e in tasks])
