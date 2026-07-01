from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        anagram: contains the exact same characters

        act => a1 c1 t1
        pots => p1 o1 t1 s1
        cat => c1 a1 t1 => a1 c1 t1 in order

        sort each string and add its index in hashmap
        """

        # sorting & hashmap
        # n = len(strs)
        # m = len(strs[i])
        # time: o(n * log(m) * m)
        # space: o(n * m)
        hashmap = defaultdict(list)
        for i, st in enumerate(strs):
            hashmap["".join(sorted(st))].append(st)
        
        res = []
        for group in hashmap.values():
            res.append(group)
        return res