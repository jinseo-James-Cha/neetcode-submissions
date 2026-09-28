class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(strs[0])
        for s in strs:
            min_len = min(min_len, len(s))

        res = ""
        for i in range(min_len):
            curr_ch = strs[0][i]
            flag = True
            for s in strs:
                if curr_ch != s[i]:
                    flag = False
                    break
            
            if not flag:
                break
            res += curr_ch

        return res