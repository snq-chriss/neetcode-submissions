class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        result = []
        for n in nums:
            if n in frequency:
                frequency[n] += 1
            else:
                frequency[n] = 1
        while len(result) < k:
            mostFrequent = None
            highest = 0
            for n in frequency:
                if frequency[n] > highest:
                    highest = frequency[n]
                    mostFrequent = n
            result.append(mostFrequent)
            frequency.pop(mostFrequent)
        return result
        