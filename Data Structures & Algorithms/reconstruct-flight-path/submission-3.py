from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        tickets - from, to => directed edges

        start from JFK
        use all edges and lexicographically smallest order 
        -> alphabetical ascending order

        JFK -> SEA, HOU and remove SEA
        """
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        res = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)

        dfs('JFK')
        return res[::-1]


        # DFS - TLE
        tickets.sort()
        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)
        
        def dfs(src):
            if len(res) - 1 == len(tickets):
                return True
            
            if src not in adj:
                return False
            
            temp = adj[src][:]
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                adj[src].insert(i, v)
                res.pop()
            return False
        res = ["JFK"]
        dfs("JFK")
        return res

                




