class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window
        curr_subs = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while curr_subs and s[right] in curr_subs:
                curr_subs.remove(s[left])
                left += 1
            
            curr_subs.add(s[right])
            res = max(res, right - left + 1)            
        return res
