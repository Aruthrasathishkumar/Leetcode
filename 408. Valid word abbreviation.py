class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        i = 0  # pointer for word
        j = 0  # pointer for abbr

        while i < len(word) and j < len(abbr):

            # Case 1: letter
            if abbr[j].isalpha():
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1

            # Case 2: digit
            else:
                if abbr[j] == '0':   # leading zero not allowed
                    return False

                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1

                i += num

        return i == len(word) and j == len(abbr)