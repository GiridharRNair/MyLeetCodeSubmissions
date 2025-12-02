class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        n = len(grid)
        m = len(grid[0])
        
        res = 0

        for i in range(n):
            for j in range(m):
                node = grid[i][j]

                if node == 1:
                    for dx, dy in DIRECTIONS:
                        new_i = i + dx
                        new_j = j + dy

                        if (
                            new_i < 0 or
                            new_j < 0 or
                            new_i >= n or
                            new_j >= m
                        ):
                            res += 1
                            continue

                        neighbor_node = grid[new_i][new_j]
                        

                        if neighbor_node == 0:
                            # print(new_i, new_j, grid[new_i][new_j])
                            res += 1
        
        return res






