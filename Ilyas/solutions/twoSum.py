class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, value in enumerate(nums):
            pair = target - value
            
            try:
                j = nums.index(pair, index+1)
                return [index, j]
            except:
                continue
