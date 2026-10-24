class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        spairs = {}
        for i in s:
            if i in spairs:
                spairs[i] += 1
            else:
                spairs[i] = 1
        tpairs = {}
        for j in t:
            if j in tpairs:
                tpairs[j] += 1
            else:
                tpairs[j] = 1
        return spairs == tpairs
        