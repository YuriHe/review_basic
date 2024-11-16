class Solution:
    """
    Question: graph find nearest exit from entrance
    1.exit is cell at border i=0 or len(grid) or j = 0 or len(grid[0]) and not wall
    bfs
    """
    def check(self, grid, i, j):
        return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        if not maze or not maze[0]: return -1
        step = 0
        dir = [[1,0], [-1, 0], [0, 1], [0, -1]]
        q = deque([(entrance[0], entrance[1])])
        # mark entrance  visited
        maze[entrance[0]][entrance[1]] = "+"

        while len(q) > 0:
            size = len(q)
            step += 1

            for _ in range(size):
                first = q.popleft()
                for x, y in dir:
                    nx = x + first[0]
                    ny = y + first[1]
                    if self.check(maze, nx, ny) and maze[nx][ny] == ".":
                        if nx == 0 or ny == 0 or nx == len(maze)-1 or ny == len(maze[0]) - 1:
                            return step

                        q.append((nx, ny))
                        maze[nx][ny] = "+"
                        
        return -1