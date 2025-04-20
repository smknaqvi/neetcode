from collections import defaultdict

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
      
    dictS = dict()
    dictT = dict()
    for i in s:
        dictS[i] = dictS.get(i, 0) + 1
  
    for j in t:
        dictT[j] = dictT.get(j, 0) + 1
  
    return dictT == dictS
