class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        top = 0
        bottom = len(matrix) - 1
        while top < bottom:
            for i in range(len(matrix)):
                temp = matrix[top][i]
                matrix[top][i] = matrix[bottom][i]
                matrix[bottom][i] = temp
            top += 1
            bottom -= 1

        for idx in range(len(matrix)):
            for jdx in range(idx + 1, len(matrix[0])):
                temp = matrix[idx][jdx]
                matrix[idx][jdx] = matrix[jdx][idx]
                matrix[jdx][idx] = temp
        

        