class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # [0, 0]
        # [0, 1]
        # [1, 0]
        # [2, 0]
        # [2, 2]
        # [0, 2]

        rows = len(mat)
        cols = len(mat[0])
        out = []
        for d in range(rows + cols + 1):
            temp = []
            r, c = 0, 0
            if d < cols:
                r = 0
                c = d
            else:
                r = d - cols + 1
                c = cols - 1

            while r < rows and c > -1:
                temp.append(mat[r][c])
                r += 1
                c -= 1

            if d % 2 == 0:
                temp = temp[::-1]
            
            out.extend(temp)
        return out
            
