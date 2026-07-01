class Solution:
    """
    encode
    4#neet4#code4#love3#you

    decode
    4#neet4#code4#love3#you
    4 == length
    # == dividor
    neet == actual word == encode[#index + 1: #index+1+length]
    """
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res