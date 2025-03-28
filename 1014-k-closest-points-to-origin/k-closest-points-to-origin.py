import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # min_heap = PriorityQueue()
        h = []
        for point in points:
            d = math.sqrt(math.pow(point[0], 2) + math.pow(point[1], 2))
            heapq.heappush(h, (d, [point[0], point[1]]))
        
        out = []
        for i in range(k):
            d, arr = heappop(h)
            out.append(arr)
        return out