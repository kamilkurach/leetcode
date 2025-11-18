class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        letters = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
        if (letters[coordinate1[0]] + int(coordinate1[1])) % 2 == 0 and (letters[coordinate2[0]] + int(coordinate2[1])) % 2 == 0:
            return True
        elif (letters[coordinate1[0]] + int(coordinate1[1])) % 2 != 0 and (letters[coordinate2[0]] + int(coordinate2[1])) % 2 != 0:
            return True
