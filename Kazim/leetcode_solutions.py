# Kazim's LeetCode Solutions
from collections import defaultdict
from typing import List


def hasDuplicate(self, nums: List[int]) -> bool:
    seenNums = set()
    for num in nums:
        if num in seenNums:
            return True
        seenNums.add(num)
    return False


def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    sCount = defaultdict(int)
    tCount = defaultdict(int)

    for letter in s:
        sCount[letter] += 1
    for letter in t:
        tCount[letter] += 1

    if len(tCount) != len(sCount):
        return False
    for letter, count in sCount.items():
        if tCount[letter] != count:
            return False
    return True

