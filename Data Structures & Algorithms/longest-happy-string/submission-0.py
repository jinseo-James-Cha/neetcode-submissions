class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        # max heap
        pending = []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(pending, (count, char))

        res = ""
        while pending:
            cnt, ch = heapq.heappop(pending)
            if len(res) > 1 and res[-1] == res[-2] == ch:
                if not pending:
                    break

                cnt2, ch2 = heapq.heappop(pending)
                res += ch2
                cnt2 += 1
                if cnt2:
                    heapq.heappush(pending, (cnt2, ch2))
                heapq.heappush(pending, (cnt, ch))
            else:
                res += ch
                cnt += 1
                if cnt:
                    heapq.heappush(pending, (cnt, ch))
        return res
