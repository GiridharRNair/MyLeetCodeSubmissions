from queue import PriorityQueue

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = PriorityQueue()
        for point in points:
            d = math.sqrt(math.pow(point[0], 2) + math.pow(point[1], 2))
            min_heap.put((d, [point[0], point[1]]))
        
        out = []
        for i in range(k):
            d, arr = min_heap.get()
            out.append(arr)
        return out