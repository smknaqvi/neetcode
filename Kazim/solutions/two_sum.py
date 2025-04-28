from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    prevNums = {}
    for idx, num in enumerate(nums):
        diff = target - num
        if diff in prevNums:
            return [prevNums[diff], idx]
        prevNums[num] = idx