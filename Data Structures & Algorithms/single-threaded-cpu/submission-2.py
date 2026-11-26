class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """
        label 0 - n-1

        tasks[i] = [enqueueTimei, processingTimei]

        cpu idle choose shortest processing time -> minheap?
        if processing time same, choose smallest index? -> minheap processing time, index, enqueueTime

        # priority
        enqueue time > processing time > index


        2 - 1 -> 3
        3 - 3 -> 6 => 62 64 61
        6 - 1 -> 7 => 72 74



        """
        available = []
        pending = []
        for i, [enqueueTime, processingTime] in enumerate(tasks):
            heapq.heappush(pending, (enqueueTime, processingTime, i))

        res = []
        curr_time = 0
        while pending or available:
            while pending and pending[0][0] <= curr_time:
                enq, proc, i = heapq.heappop(pending)
                heapq.heappush(available, (proc, i))
            
            if not available:
                curr_time = pending[0][0]
                continue

            pro_time, idx = heapq.heappop(available)
            curr_time += pro_time
            res.append(idx)
        
        return res







