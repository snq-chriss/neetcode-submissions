class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pairs = {}
        for s in strs:
            letters = tuple(sorted(s))
            if letters in pairs:
                pairs[letters].append(s)
            else:
                pairs[letters] = [s]
        return list(pairs.values())