class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        out = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                out[j][i] = matrix[i][j]
        return out