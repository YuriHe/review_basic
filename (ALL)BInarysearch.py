# search first element >= target from sorted array
def search(self, ls, target):
    # find first element >= target, return length of rest list which >= target
    i, j = 0, len(ls)-1
    while i <= j:
        mid = (i+j) // 2
        if ls[mid] >= target:
            j = mid - 1
        else:
            i = mid + 1
    return len(ls) - i # only see left pointer


"""
875. Koko Eating Bananas
guess
"""
def minEatingSpeed(self, piles: List[int], h: int) -> int:
    # find max pile because maximum speed no matter h
    left, right = 1, max(piles) 

    while left <= right:
        mid = (left+right) // 2 # mid is speed
        hour = 0
        for p in piles:
            hour += math.ceil(p / mid)
        if hour > h: # mean overtime need increase speed 
            left = mid + 1
        else:
            # <= hour, meet requirement, find minimum speed
            right = mid - 1

    return left

def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def totalH(speed):
            # hours needed for eating all bananas
            hour = 0
            for p in piles:
                hour += math.ceil(p / speed)
            return hour
             
        left, right = 1, max(piles)
        while left <= right: # about determining speed
            mid = (left+right) // 2
            if totalH(mid) > h:
                # hour exceed, less hour, increase speed
                left = mid + 1
            else:
                right = mid - 1
        return left
            

