def twoSum(self, nums: List[int], target: int) -> List[int]:
    # Create a map of number to index
    # For each number, check if the corresponding number exists
    numsMap = {}
    for i, num in enumerate(nums):
        if target - num in numsMap:
            return [min(i, numsMap[target-num]), max(i, numsMap[target-num])]
        numsMap[num] = i
    return -1, -1
