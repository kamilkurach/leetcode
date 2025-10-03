class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = [e for e in ransomNote]
        for e in ransom:
            if ransomNote.count(e) > magazine.count(e):
                return False 
        return True
