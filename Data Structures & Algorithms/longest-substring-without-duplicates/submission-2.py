class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window 2
        substring = set()
        left = 0
        longest_len = 0
        for right in range(len(s)):
            while substring and s[right] in substring:
                substring.remove(s[left])
                left += 1
            substring.add(s[right])
            longest_len = max(longest_len, len(substring))
        return longest_len













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
