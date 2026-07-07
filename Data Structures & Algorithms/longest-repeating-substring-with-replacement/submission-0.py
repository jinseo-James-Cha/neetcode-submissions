class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        uppercase alphabets
        can ingore difference as much as k

        X Y Y X  k = 2 -> 1 -> 0
        L
            R 
        
        X Y Y X
        1 2 2 2
            L R
        """

        # Sliding window
        longest_repeating = 0
        s_set = set(s)
        
        for c in s_set:
            count = 0
            left = 0
            for right in range(len(s)):
                if s[right] == c:
                    count += 1
                
                while right - left + 1 - count > k:
                    if s[left] == c:
                        count -= 1
                    left += 1
                
                longest_repeating = max(longest_repeating, right - left + 1)
        return longest_repeating


