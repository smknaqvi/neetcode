from typing import List

def hasDuplicate(self, nums: List[int]) -> bool:
    seenNums = set()
    for num in nums:
        if num in seenNums:
            return True
        seenNums.add(num)
    return False

if __name__ == "__main__":
    # Local tests
    def run_tests():
        # Create a simple test harness
        solution = type('Solution', (), {'hasDuplicate': hasDuplicate})()
        
        test_cases = [
            ([1, 2, 3, 1], True),
            ([1, 2, 3, 4], False),
            ([], False),
            ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)
        ]
        
        for nums, expected in test_cases:
            result = solution.hasDuplicate(nums)
            print(f"Input: {nums}")
            print(f"Expected: {expected}, Got: {result}")
            print(f"{'✓ PASS' if result == expected else '✗ FAIL'}\n")
    
    run_tests()