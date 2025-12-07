class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        return [e for e in order if e in friends]
