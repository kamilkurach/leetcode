#2586. Count the Number of Vowel Strings in Range
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowel = ['a','e','i','o','u']
        count = 0
        for word in words[left:right+1]:
            if word[0] in vowel and word[-1] in vowel:
                count+=1
        return count
