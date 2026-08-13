from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        directed nodes
        label: 1 ~ n
        times = u -> v with t

        starting node = k
        """

        # dijkstra algorithm
        graph = defaultdict(list)
        for u,v,t in times:
            graph[u].append((t, v))

        network_time = [float('inf')] * (n+1)
        network_time[0] = 0
        network_time[k] = 0
        min_heap = [(0, k)]
        while min_heap:
            curr_time, curr_node = heapq.heappop(min_heap)
            if curr_time > network_time[curr_node]:
                continue

            for next_time, next_node in graph[curr_node]:
                new_time = curr_time + next_time
                if network_time[next_node] > new_time:
                    network_time[next_node] = new_time
                    heapq.heappush(min_heap, (new_time, next_node))
        
        if max(network_time) == float('inf'):
            return -1
        
        return max(network_time)

