from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        m = defaultdict(int)
        out = 0
        img1_cord = []
        img2_cord = []

        n = len(img1)

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    img1_cord.append((i, j))
                if img2[i][j] == 1:
                    img2_cord.append((i, j))

        overlap = 0
        for c in img1_cord:
            for j in img2_cord:
                diff = (c[0] - j[0], c[1] - j[1])
                m[diff] += 1
                out = max(out, m[diff])
        # print(m)
        return out