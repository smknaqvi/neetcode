from collections import defaultdict

def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        # Go through first str and count the occurrence of each letter
        occurrenceMap = {}
        for letter in s:
            if letter in occurrenceMap:
                occurrenceMap[letter] += 1
            else:
                occurrenceMap[letter] = 1
        
        # Go through second str and subtract occurrence of each letter
        for letter in t:
            if letter not in occurrenceMap:
                return False
            else:
                occurrenceMap[letter] -= 1
            if occurrenceMap[letter] == 0:
                del occurrenceMap[letter]
        
        return len(occurrenceMap) == 0
