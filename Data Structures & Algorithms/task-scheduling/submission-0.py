class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
         
        mh = [- cnt for cnt in count.values()]
        heapq.heapify(mh)

        time = 0
        q = deque()

        while mh or q:
            time += 1

            if mh:
                largest =  1 +  heapq.heappop(mh) 
                
                if largest < 0:
                    q.append((largest, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(mh, q.popleft()[0])
        
        return time