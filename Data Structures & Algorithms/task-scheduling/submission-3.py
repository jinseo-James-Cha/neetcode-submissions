from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = {}
        for t in tasks:
            hashmap[t] = hashmap.get(t, 0) + 1
        
        maxHeap = [-cnt for cnt in hashmap.values()]
        
        heapq.heapify(maxHeap) # current todo
        q = deque() # after cooltime
        
        time = 0 # current time
        while maxHeap or q:
            time += 1

            if not maxHeap: # if there is no todo, move to the first task from cooltime list
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap) # finish one task from todo
                if cnt: # if it is not 0
                    q.append([cnt, time + n]) # move to next cycle in cooltime

            if q and q[0][1] == time: # this time take from cool time to todolist
                heapq.heappush(maxHeap, q.popleft()[0])
        return time