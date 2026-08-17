class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # topological sort
        adj = defaultdict(set)
        indegree = defaultdict(int)
        for word in words:
            for c in word:
                indegree[c] = 0
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        
        queue = deque()
        for c in indegree:
            if indegree[c] == 0:
                queue.append(c)
        
        res = []
        while queue:
            ch = queue.popleft()
            res.append(ch)
            
            for neighbor in adj[ch]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(res) != len(indegree):
            return ""
        
        return "".join(res)





