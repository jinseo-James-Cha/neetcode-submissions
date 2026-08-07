class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_word = True

    def search(self, word: str) -> bool:
        def dfs(idx, node):
            curr = node
            for i in range(idx, len(word)):
                ch = word[i]
                if ch == ".":
                    for child_node in curr.children.values():
                        if dfs(i + 1, child_node):
                            return True
                    return False
                else:
                    if ch not in curr.children:
                        return False
                    curr = curr.children[ch]
            return curr.is_word
        
        return dfs(0, self.root)




        
