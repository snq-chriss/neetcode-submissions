class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        s_pairs = {}
        t_pairs = {}
        for i in s_list:
            if i in s_pairs:
                s_pairs[i] += 1
            else:
                s_pairs[i] = 1
        for i in t_list:
            if i in t_pairs:
                t_pairs[i] += 1
            else:
                t_pairs[i] = 1       
        return s_pairs == t_pairs