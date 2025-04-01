class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flatten = []
        for row in mat:
            for ele in row:
                flatten.append(ele)

        if r * c != len(flatten):
            return mat

        new_mat = [[0] * c for _ in range(r)]
        for idx, ele in enumerate(flatten):
            new_mat[idx // c][idx % c] = ele
        return new_mat