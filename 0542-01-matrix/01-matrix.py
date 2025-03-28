class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque()

        for i, row in enumerate(mat):
            for j, ele in enumerate(row):
                if ele == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = float("inf")

        while q:
            row, col = q.popleft()
            for direction in directions:
                n_row = row + direction[0]
                n_col = col + direction[1]

                if (
                    0 <= n_row < len(mat) and
                    0 <= n_col < len(mat[0]) and
                    mat[n_row][n_col] > mat[row][col] + 1
                ):
                    mat[n_row][n_col] = mat[row][col] + 1
                    q.append((n_row, n_col))
        
        return mat



        