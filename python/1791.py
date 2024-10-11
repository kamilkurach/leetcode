class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        result = set()
        for n in edges[1:]:
            i = set(edges[0]).intersection(set(n)).pop()
            result.add(i)
        return result.pop()
