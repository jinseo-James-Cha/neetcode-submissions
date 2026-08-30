class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        triplets : a, b, c
        target : x, y, z

        triplets becomes target? possible?

        triplet[i] -> triplet[j] => current = [max(i[])

            [[2,5,3],[1,8,4],[1,7,5]] target [2,7,5]
              M - -   - N -   - M M
              0                 1 2 => True
        """
        # Greedy
        found = set()
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            
            for i, v in enumerate([a, b, c]):
                if v == target[i]:
                    found.add(i)
        return len(found) == 3
        
    
            
