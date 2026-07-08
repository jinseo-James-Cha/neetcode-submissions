class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        OUZODYXAZV
             -- -
             YX Z => window size 4 and YXAZ
            
        return substring of s if any
        """
        
        if s == t:
            return s
        
        if len(s) < len(t):
            return ""

        count_t = {}
        for ch_t in t:
            count_t[ch_t] = count_t.get(ch_t, 0) + 1
        
        have = 0
        need = len(count_t)
        res = [-1, -1]
        resLen = float('inf')
        
        window = {}
        left = 0
        for right in range(len(s)):
            curr = s[right]
            window[curr] = window.get(curr, 0) + 1

            if curr in count_t and window[curr] == count_t[curr]:
                have += 1
            
            while have == need:
                if right - left + 1 < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                window[s[left]] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1
        
        return s[res[0] : res[1] + 1] if resLen != float('inf') else ""








        