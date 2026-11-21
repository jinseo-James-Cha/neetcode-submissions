class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }


        def backtrack(curr, idx):
            if idx == len(digits):
                res.append("".join(curr))
                return
            
            for ch in phone[digits[idx]]:
                curr.append(ch)
                backtrack(curr, idx + 1)
                curr.pop()

        res = []
        backtrack([], 0)
        return res
