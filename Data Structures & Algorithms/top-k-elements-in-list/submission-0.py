from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        most frequent elements

        count how many each num in the list
        sorting them based on frequence
        and return by the most frequence
        """

        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        freq_arr = []
        for num, freq in count.items():
            freq_arr.append([freq, num])
        
        freq_arr.sort(reverse=True)
        return [ num for freq, num in freq_arr[:k]]
        
