class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        s base and p can be s?

        . -> any single character
        * -> zero  or more of the preceding element
        """

        # a a b
        # c * a *b
        memo = {}

        def dp(s_idx, p_idx):
            if p_idx == len(p):
                return s_idx == len(s)

            if (s_idx, p_idx) in memo:
                return memo[(s_idx, p_idx)]

            first_match = (
                s_idx < len(s)
                and (s[s_idx] == p[p_idx] or p[p_idx] == ".")
            )

            if p_idx + 1 < len(p) and p[p_idx + 1] == "*":
                # 0 times OR 1+ times
                res = (
                    dp(s_idx, p_idx + 2) # 0 times
                    or
                    (first_match and dp(s_idx + 1, p_idx)) # 1+ times
                )
            else:
                res = (
                    first_match
                    and dp(s_idx + 1, p_idx + 1)
                )

            memo[(s_idx, p_idx)] = res
            return res
        memo = {}
        return dp(0, 0)