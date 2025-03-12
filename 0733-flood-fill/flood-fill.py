class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        s_color = image[sr][sc]
        def fill(row, col):
            print(row, col)
            if row >= len(image) or col >= len(image[0]) or row < 0 or col < 0:
                return
            
            if image[row][col] != s_color:
                return
            image[row][col] = color
                
            fill(row + 1, col)
            fill(row, col + 1)
            fill(row - 1, col)
            fill(row, col - 1)
            
        fill(sr, sc)
        return image