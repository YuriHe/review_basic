"""
    Question: Can place flower avoid neighbor [i-1] and [i+1],
    try to place flowers as much we can
    Topic: Greedy
    Issue: Boundary
    """
def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    for i in range(len(flowerbed)):
        # check boundary
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
            # update flowerbed list
            flowerbed[i] = 1
            n -= 1
        if n <= 0:
            return True
    return False