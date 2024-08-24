#2309. Greatest English Letter in Upper and Lower Case
class Solution:
    def greatestLetter(self, s: str) -> str:
        tab = [""]
        for letter in s:
            if letter.isupper() == True:
                for lower_letter in s:
                    if lower_letter.islower() == True and lower_letter == letter.lower():
                        if tab[0] < letter:
                            tab.pop(0)
                            tab.append(letter)
        if len(tab) > 0:
            return tab[0]
        else:
            return ""
