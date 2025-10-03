class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewels = [e for e in jewels]
        for stone in jewels:
            count = count + stones.count(stone)
        return count
