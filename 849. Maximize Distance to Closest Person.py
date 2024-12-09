class Solution:
    """
    Question: maximum distance from any empty seat(0) to the closest occupied seat(1)
    """
    def maxDistToClosest(self, seats: List[int]) -> int:
        occupied = []
        
        # collect indices where seats are occupied
        for i in range(len(seats)):
            if seats[i] == 1:
                occupied.append(i)

        # maximum distance to closet occupied seat, compare first, last
        res = max(occupied[0], len(seats)-1-occupied[-1])
        
        # check distance between consecutive occupied seats
        for i in range(1, len(occupied)):
                res = max(res, (occupied[i] - occupied[i - 1]) // 2) # middle
        
        return res

