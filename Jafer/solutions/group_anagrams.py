def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # Outline:
    # For each string, create a tuple of length 26
    # For each ocurrence of a letter, increment tuple[i]
    # In a map, use the tuple as the key, and let each corresponding anagram be the value
    anagramSets = defaultdict(list)
    for string in strs:
        alphabetList = [0 for i in range(26)]
        
        for character in string:
            positionInAlphabet = ord(character) - ord('a')
            alphabetList[positionInAlphabet] += 1

        alphabetTuple = tuple(alphabetList)
        anagramSets[alphabetTuple].append(string)

    return anagramSets.values()
