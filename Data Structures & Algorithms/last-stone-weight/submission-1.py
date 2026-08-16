class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for i in stones:
            heapq.heappush(max_heap, -i)
        
        while len(max_heap)  > 1:
            x = - heapq.heappop(max_heap)
            y = - heapq.heappop(max_heap)
            
            

            res = max(x, y) - min(x, y)
            if res != 0:
                heapq.heappush(max_heap, -res)
            
        return -max_heap[0] if max_heap else 0