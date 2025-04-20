from typing import List

def hasDuplicate(self, nums: list[int]) -> bool:
      x = len(nums)
      y = len(set(nums))
      return x != y
