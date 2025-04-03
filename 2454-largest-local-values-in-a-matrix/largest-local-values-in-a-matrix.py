class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        out = [[0] * (len(grid) - 2) for _ in range(len(grid) - 2)]
        for i in range(0, len(grid) - 2):
            for j in range(0, len(grid) - 2):
                out[i][j] = self.maxLocal(i, j, grid)
        return out

    def maxLocal(self, i, j, grid):
        max_element = 0
        for idx in range(i, i + 3):
            for jdx in range(j, j + 3):
                max_element = max(max_element, grid[idx][jdx])
        return max_element