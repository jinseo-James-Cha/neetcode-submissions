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

        network_nodes = [float('inf')] * (n+1)
        network_nodes[0] = 0
        network_nodes[k] = 0
        queue = [(0, k)]
        while queue:
            curr_time, curr_node = heapq.heappop(queue)

            for next_time, next_node in graph[curr_node]:
                new_time = curr_time + next_time
                if network_nodes[next_node] > new_time:
                    network_nodes[next_node] = new_time
                    heapq.heappush(queue, (new_time, next_node))
        
        if max(network_nodes) == float('inf'):
            return -1
        
        return max(network_nodes)

