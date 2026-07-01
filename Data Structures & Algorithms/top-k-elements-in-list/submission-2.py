from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        most frequent elements

        count how many each num in the list
        sorting them based on frequence
        and return by the most frequence
        """
        # bucket sort
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        bucket = [[] for i in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)
        
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            res.extend(bucket[i])
            if len(res) >= k:
                break
        return res[:k]

        # max heap
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        freq_arr = []
        for num, freq in count.items():
            heapq.heappush(freq_arr, [-freq, num])
        
        res = []
        while k > 0:
            res.append(heapq.heappop(freq_arr)[1])
            k -= 1
        return res

        

        # sorting
        # time: O(n + n log n + k)
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        freq_arr = []
        for num, freq in count.items():
            freq_arr.append([freq, num])
        
        freq_arr.sort(reverse=True)
        return [ num for freq, num in freq_arr[:k]]
        
