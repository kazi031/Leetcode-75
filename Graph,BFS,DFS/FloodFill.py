class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        def fill(x, y, c):
            if image[x][y] == c:
                image[x][y] = color
                if x > 0: fill(x-1, y, c)
                if x + 1 < len(image): fill(x+1, y, c)
                if y > 0: fill(x, y-1, c)
                if y + 1 < len(image[0]): fill(x, y+1, c)
            

        fill(sr, sc, image[sr][sc])

        return image
