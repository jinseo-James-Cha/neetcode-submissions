class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        - from src to dst within k stops(not including src and dst)
        - directed weight graph
        """
        # dijkstra
        adj = defaultdict(list)
        for u,v,w in flights:
            adj[u].append((w, v))

        dist = [[float('inf')] * (k + 2) for _ in range(n)]
        min_heap = [(0, src, 0)]
        
        while min_heap:
            price, curr, edges = heapq.heappop(min_heap)
            if curr == dst:
                return price

            if edges == k + 1:
                continue

            if price > dist[curr][edges]:
                continue

            for next_price, neighbor in adj[curr]:
                new_price = price + next_price
                new_edges = edges + 1

                if new_price < dist[neighbor][new_edges]:
                    dist[neighbor][new_edges] = new_price

                    heapq.heappush(
                        min_heap,
                        (new_price, neighbor, new_edges)
                    )

        return -1