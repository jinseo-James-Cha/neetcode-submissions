from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        rearrange the cards into groups which size groupSize

        card values are increasing by 1

        card 1 2 4 2 3 5 3 4 => 8 cards so make 2 groups n // groupSize
        
        1: 1
        2: 2
        3: 2
        4: 2
        5: 1

        1 2 3 4 
        5 4 3 2
        """
        # Greedy
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        for num in hand:
            start = num
            while count[start - 1]:
                start -= 1
            while start <= num:
                while count[start]:
                    for i in range(start, start + groupSize):
                        if not count[i]:
                            return False
                        count[i] -= 1
                start += 1
        return True


        
        # sorting
        if len(hand) % groupSize:
            return False
        
        count = Counter(hand)
        hand.sort()
        for h in hand:
            if count[h]:
                for i in range(h, h + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True

        # brute force
        n = len(hand)
        if n % groupSize:
            return False

        max_num = max(hand)
        bucket = [0] * (max_num + 1)
        for h in hand:
            bucket[h] += 1
        
        for i in range(n // groupSize):
            curr_group = []
            for i, h in enumerate(bucket):
                if bucket[i] > 0:
                    if not curr_group or curr_group[-1] + 1 == i:
                        curr_group.append(i)
                        bucket[i] -= 1
                        n -= 1
                    else:
                        return False
                
                if len(curr_group) == groupSize:
                    break
        return n == 0





