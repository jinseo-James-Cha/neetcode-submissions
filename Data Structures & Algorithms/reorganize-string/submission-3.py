class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = []
        for ch, cnt in count.items():
            heapq.heappush(max_heap, (-cnt, ch))
        
        res = ""
        prev = None
        while max_heap or prev:
            if prev and not max_heap:
                return ""

            curr_cnt, curr_ch = heapq.heappop(max_heap)
            res += curr_ch
            curr_cnt += 1

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None

            if curr_cnt:
                prev = (curr_cnt, curr_ch)

        return res

