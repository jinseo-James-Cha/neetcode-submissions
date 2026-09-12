class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()

        carry = 1
        res = []
        for digit in digits:
            curr = (carry + digit) % 10
            res.append(curr)
            carry = (carry + digit) // 10
        if carry:
            res.append(carry)
        print(res)
        res.reverse()
        return res