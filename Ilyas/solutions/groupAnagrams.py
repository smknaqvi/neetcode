#25 Mins -- Had too google how defaultdicts work
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict1 = defaultdict(list)
        for index, value in enumerate(strs):
            valsort = ''.join(sorted(value))
                
            dict1[valsort].append(value)
        return list(dict1.values())
