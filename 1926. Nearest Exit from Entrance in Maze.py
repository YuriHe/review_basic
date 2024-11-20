class Solution:
    """
    Question: graph find nearest exit from entrance
    1.exit is cell at border i=0 or len(grid) or j = 0 or len(grid[0]) and not wall
    bfs
    """
    def check(self, grid, i, j):
        return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        if not maze or maze[entrance[0]][entrance[1]] == "+":
            return 0

        q = deque()
        q.append((entrance[0], entrance[1])) # start from entrance
        maze[entrance[0]][entrance[1]] = "+"
        res = 0 # layer
        dir = [[0,1], [0, -1], [1, 0], [-1, 0]]

        while q:
            size = len(q)
            res += 1
            for _ in range(size):
                i, j = q.popleft()

                for x, y in dir:
                    nx = x + i
                    ny = y + j
                    if self.check(maze, nx, ny) and maze[nx][ny] == ".":
                        if nx == 0 or ny == 0 or nx == len(maze) - 1 or ny == len(maze[0]) - 1:
                            return res
                        else:
                            q.append((nx, ny))
                            maze[nx][ny] = "+"
            
        return -1
