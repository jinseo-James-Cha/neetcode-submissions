class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.head = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.head
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_word = True        

    def searchInMiddle(self, word, idx, node): 
        if idx >= len(word):
            return node.is_word
        
        curr = node
        for i in range(idx, len(word)):
            ch = word[i]
            if ch == ".":
                for k in curr.children:
                    if self.searchInMiddle(word, i+1, curr.children[k]):
                        return True
                return False
            elif ch not in curr.children:
                return False
            curr = curr.children[ch]
        
        return curr.is_word

    def search(self, word: str) -> bool:
        return self.searchInMiddle(word, 0, self.head)
        
