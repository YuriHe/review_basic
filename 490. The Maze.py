from typing import (
    List,
)
import collections
class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    """
    Question: from start point to destination which can stop
    Use bfs 
    start from start index, explore 4 direction, each direction will rolling in this specific direction
    until hitting wall, stop at in-bound pos
    check the pos before go rolling, if not valid, stop at previoud valid point
    """
    def has_path(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # bfs visit
        # corner case
        if maze[start[0]][start[1]] == 1 or maze[destination[0]][destination[1]] == 1:
            return False

        dir = [[1,0], [-1,0], [0,1], [0,-1]]
        def check(i, j):
            return 0 <= i < len(maze) and 0 <= j < len(maze[0])
        
        q = collections.deque([])
        q.append((start[0], start[1]))
        visit = set()
        visit.add((start[0], start[1]))
        while q:
            x,y = q.popleft()
            # exit early 
            if [x,y] == destination:
                return True
            for r, c in dir:
                """
                The ball must roll in a given direction until it hits a wall, 
                but if use 'if' moves the ball by one step (nx = r + x, ny = c + y) and then immediately considers it as a stopping point. 
                This behavior does not align with the problem statement where the ball keeps moving until it cannot proceed.
                """
                nx, ny = x, y
                while check(nx+r, ny+c) and maze[nx+r][ny+c] == 0:
                    nx += r
                    ny += c
                # After rolling, check if the stopping point is visited
                if (nx, ny) not in visit:
                    visit.add((nx, ny))
                    # push into queue
                    q.append((nx, ny))
        return False
