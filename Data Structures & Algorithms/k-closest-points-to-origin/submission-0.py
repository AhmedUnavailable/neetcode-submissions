class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:        
        def dist(x, y):
            return (x**2 + y**2)**1/2

        point_dist = [(dist(x,y), [x , y]) for x, y in points]

        heapq.heapify(point_dist)
        res = []
        for _ in range(k):
            dist, point = heapq.heappop(point_dist)
            res.append(point)
        print(res)
        return res