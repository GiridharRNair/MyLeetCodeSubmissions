from queue import PriorityQueue

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        pq = PriorityQueue()

        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        sorted_queries = sorted([query, idx] for idx, query in enumerate(queries))
        result = [0] * len(queries)

        pq.put((grid[0][0], 0, 0))
        visited[0][0] = True
        points = 0

        for query, idx in sorted_queries:
            while not pq.empty() and pq.queue[0][0] < query:
                value, row, col = pq.get()
                points += 1

                for direction in directions:
                    new_row = direction[0] + row
                    new_col = direction[1] + col

                    if (
                        0 <= new_row < len(grid) and
                        0 <= new_col < len(grid[0]) and
                        not visited[new_row][new_col]
                    ):
                        pq.put((grid[new_row][new_col], new_row, new_col))
                        visited[new_row][new_col] = True

            result[idx] = points

        return result