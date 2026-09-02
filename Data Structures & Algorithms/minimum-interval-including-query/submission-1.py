class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        both side inclusive => close intervals
        queries length = answer length


        intervals = [[1,3],[2,3],[3,7],[6,6]], 
           queries = [2,3,1,7,6,8]

        Query 2
        interval [2,3] is the smallest one containing 2
        """
        # Sweep line
        events = []
        for idx, (start, end) in enumerate(intervals):
            events.append((start, 0, end - start + 1, idx))
            events.append((end, 2, end - start + 1, idx))
        
        for i, q in enumerate(queries):
            events.append((q, 1 , i))
        
        events.sort(key=lambda x: [x[0], x[1]])

        sizes = []
        ans = [-1] * len(queries)
        inactive = [False] * len(intervals)
        
        for time, type, *rest in events:
            if type == 0: # interval start
                interval_size, idx = rest
                heapq.heappush(sizes, (interval_size, idx))
            
            elif type == 2: # interval end
                idx = rest[1]
                inactive[idx] = True
            
            else: # Query
                query_idx = rest[0]
                while sizes and inactive[sizes[0][1]]:
                    heapq.heappop(sizes)
                if sizes:
                    ans[query_idx] = sizes[0][0]
        return ans






        # Brute force -> TLE
        shortest_len = {}
        for left, right in intervals:
            curr_len = right - left + 1
            for i in range(left, right + 1):
                if i not in shortest_len:
                    shortest_len[i] = curr_len
                else:
                    shortest_len[i] = min(shortest_len[i], curr_len)

        res = []
        for q in queries:
            if q not in shortest_len:
                res.append(-1)
            else:
                res.append(shortest_len[q])
        return res

