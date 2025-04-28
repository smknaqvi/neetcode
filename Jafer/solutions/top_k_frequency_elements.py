def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # Determine frequency of each number (O(n))
    numFrequency = defaultdict(int)
    for num in nums:
        numFrequency[num] += 1

    # Turn frequency map into a list of tuples (O(n))
    frequencyTuples = [(value, key) for key, value in numFrequency.items()]
    
    # Heapify the frequencies (O(log(n)))
    heapq.heapify(frequencyTuples)

    # Return just the values 
    # (O(nlog(k))) because effectively creating a heap of size k with each pop
    return [frequencyTuple[1] for frequencyTuple in heapq.nlargest(k, frequencyTuples)]
