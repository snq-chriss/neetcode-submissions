class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pairs = {}
        result = []
        for n in nums:
            if n in pairs:
                pairs[n] += 1
            else:
                pairs[n] = 1
        while len(result) < k:
            highest = 0
            mostFrequent = None
            for n in pairs:
                if pairs[n] > highest:
                    highest = pairs[n]
                    mostFrequent = n
            pairs.pop(mostFrequent)
            result.append(mostFrequent)
        return result 