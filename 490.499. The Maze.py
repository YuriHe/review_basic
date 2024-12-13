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


from typing import (
    List,
)
import heapq
class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """
    def shortest_distance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        """
        Step means track distance traveled by ball which won't stop rolling until
        hit the wall and find shortest path, steps mean walk each cell
        Use Dijkstra algorithm use heap, not queue
        """
        if maze[start[0]][start[1]] == 1 or maze[destination[0]][destination[1]] == 1:
            return False

        dir = [[1,0], [-1,0], [0,1], [0,-1]]
        def check(i, j):
            return 0 <= i < len(maze) and 0 <= j < len(maze[0]) and maze[nx+r][ny+c] == 0
        
        heap = []
        heapq.heappush(heap, (0, start[0], start[1]))
        
        # store shortest distance to that point
        dist_map = {(start[0], start[1]): 0}

        while heap:
            dist, x, y = heapq.heappop(heap)
            # exit early 
            if [x,y] == destination:
                return dist
            for r, c in dir:
                nx, ny, step = x, y, 0
                while check(nx+r, ny+c):
                    nx += r
                    ny += c
                    step += 1
                # new pos offers shorter path, update and push into push
                new_dist = dist + step
                if (nx, ny) not in dist_map or new_dist < dist_map[(nx, ny)]:
                    # update dist_map
                    dist_map[(nx, ny)] = new_dist
                    # smaller can push to heap
                    heapq.heappush(heap, (new_dist, nx, ny))
        return -1
