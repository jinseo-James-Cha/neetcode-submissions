class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count = {}
        for ch_s in s:
            s_count[ch_s] = s_count.get(ch_s, 0) + 1
        
        for ch_t in t:
            if ch_t not in s_count:
                return False
            
            s_count[ch_t] -= 1
            if s_count[ch_t] == 0:
                del s_count[ch_t]
        
        
        return True if not s_count else False
