class Solution:
    """
    QUESTION: modify array, 
    1step:change startpoint to target, then when dfs neighbors, change to target if they have same value as original pixel
    """
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]
        if start == color:
            return image
        dire = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(r,c):
            if r < 0 or c < 0 or r>=len(image) or c >= len(image[0]):
                return
            if image[r][c] != start:
                return
            #visited and modified
            image[r][c] = color

            for d in dire:
                newr, newc = r+d[0], c+d[1]
                dfs(newr, newc)

        dfs(sr,sc)
        return image