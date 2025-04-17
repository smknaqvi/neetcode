from collections import defaultdict

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

if __name__ == "__main__":
    # Local tests
    def run_tests():
        # Create a simple test harness
        solution = type('Solution', (), {'isAnagram': isAnagram})()
        
        test_cases = [
            (("anagram", "nagaram"), True),
            (("rat", "car"), False),
            (("", ""), True),
            (("aacc", "ccac"), False)
        ]
        
        for (s, t), expected in test_cases:
            result = solution.isAnagram(s, t)
            print(f"Input: s = '{s}', t = '{t}'")
            print(f"Expected: {expected}, Got: {result}")
            print(f"{'✓ PASS' if result == expected else '✗ FAIL'}\n")
    
    run_tests()