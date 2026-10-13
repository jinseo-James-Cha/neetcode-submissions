class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        OUZODYXAZV
        0010011    -> res right - left + 1
           L   01  -> res right - left + 1       
               
        X1 Y1 Z1
        """
        if s == t:
            return t

        if len(s) < len(t):
            return ""
        
        count_t = {}
        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1
        
        have = 0
        need = len(count_t)
        window = {}
        res = [-1, -1]
        min_window_len = float('inf')

        left = 0
        for right in range(len(s)):
            curr = s[right]
            window[curr] = window.get(curr, 0) + 1

            if curr in count_t and window[curr] == count_t[curr]:
                have += 1
            
            while have == need:
                if right - left + 1 < min_window_len:
                    res = [left, right]
                    min_window_len = right - left + 1
                
                window[s[left]] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1
        left = res[0]
        right = res[1]
        return s[left: right + 1] if min_window_len != float('inf') else ""






