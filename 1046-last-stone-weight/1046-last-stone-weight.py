import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)


        while len(max_heap) > 1:
            stone_one = heapq.heappop(max_heap)
            stone_two = heapq.heappop(max_heap)
            
            if stone_one != stone_two:
                heapq.heappush(max_heap,stone_one - stone_two)
            else:
                continue

        if len(max_heap) == 0:
            return 0
        else:
            return heapq.heappop(max_heap) * -1
        
       





        