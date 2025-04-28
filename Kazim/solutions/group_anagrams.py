from collections import defaultdict
from typing import List

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    out = defaultdict(list)
    for word in strs:
        charCountKey = [0]*26
        for char in word:
            charCountKey[ord(char)-97] += 1
        out[tuple(charCountKey)].append(word)
    return out.values()