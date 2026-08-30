from collections import Counter, defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        split the string into as many substrings as possible


        xyxxyzbzbbisl

        x: 3
        y: 2
        z: 2
        b: 3
        i: 1
        s: 1
        l: 1
        xyxxyzbzbbisl
        11232
        """

        count = Counter(s)
        res = []
        curr = defaultdict(int)
        curr_len = 0
        for ch in s:
            curr_len += 1

            curr[ch] += 1
            if curr[ch] == count[ch]:
                del curr[ch]
            
            if len(curr) == 0:
                res.append(curr_len)
                curr_len = 0
        
        if curr_len != 0:
            res.append(curr_len)
        return res