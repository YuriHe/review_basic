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
    return n <= 0


# show detail
def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    if len(flowerbed) == 1 and flowerbed[0] == 0: return True
    
    for i in range(0, len(flowerbed)):
        # first slot
        if i == 0 and i+1 < len(flowerbed) and flowerbed[i] == 0 and flowerbed[i+1] == 0:
            flowerbed[i] = 1
            n -= 1
        # last slot
        elif i == len(flowerbed)-1  and i - 1 >= 0 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
            flowerbed[i] = 1
            n -= 1
        else:
            if i-1 >= 0 and i+1 < len(flowerbed):
                if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1

    return n <= 0

    # Best 
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # add padding to simplify boundary check
        flowerbed = [0]+ flowerbed+[0]
        for i in range(1, len(flowerbed)-1, 1):
            if flowerbed[i] == 0:
                if flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                    n-= 1
                    flowerbed[i] = 1
            if n <= 0:
                return True


        return True if n <=0 else False