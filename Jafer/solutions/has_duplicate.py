from typing import List

def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueNums = set(nums)
        return len(uniqueNums) != len(nums)
