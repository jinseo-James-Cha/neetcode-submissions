class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_word = True

    def search(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        
        return curr.is_word

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        for word in wordDict:
            trie.add(word)
        
        def backtrack(start, curr):
            if start == len(s):
                res.append(" ".join(curr))
                return
            
            for i in range(start, len(s)):
                curr_word = s[start: i + 1]
                if trie.search(curr_word):
                    curr.append(curr_word)
                    backtrack(i+1, curr)
                    curr.pop()
        
        res = []
        backtrack(0, [])
        return res




        