class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        lowercase alphabets nad all distict

        cat, sag , ["bat","bag","sag","dag","dot"]

        cat -> bat -> bag -> dag -> sag
                          -> sag

    

        """
        
        if len(beginWord) != len(endWord):
            return 0
        
        if endWord not in wordList:
            return 0
        
        if beginWord == endWord:
            return 0

       
        wordSet = set(wordList)
        res = 0
        
        queue = deque([beginWord])
        while queue:
            res += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == endWord:
                    return res
                
                for i in range(len(node)):
                    for j in range(26):
                        if chr(j + ord('a')) == node[i]:
                            continue
                        new_node = node[:i] + chr(j + ord('a')) + node[i+1:]
                        if new_node in wordSet:
                            queue.append(new_node)
                            wordSet.remove(new_node)
        return 0



