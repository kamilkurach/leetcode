#2114. Maximum Number of Words Found in Sentences
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        result = 0
        for sentence in sentences:
            if len(sentence.split(" ")) > result:
                result = len(sentence.split(" "))
        return result
