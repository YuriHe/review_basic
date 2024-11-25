import math
from collections import *
"""
Trash volume fixed + Use at least bins to fill out all trash, trash cannot break into pieces
volume >= each trash in list
"""
def min_bins(volume, trash):
    if not trash:
        return 0

    # sort trash from most to less nlogn
    trash = sorted(trash, reverse=True)

    bin = 0
    left = 0

    for i in range(0, len(trash)):
        if left + trash[i] > volume:
            # move this cur to next bin
            bin += 1
            left = trash[i]
        else:
            left += trash[i] # add this trash to cur bin
    if left > 0:
        bin += 1
    return bin

trash = [6,3,5,4,2,1,9]
v = 10
print(min_bins(v, trash))


def findJudge(n, trust):
    adj = defaultdict(list)
    for a,b in trust:
        adj[a].append(b)
    
    for i in range(1, n+1):
        if i not in adj:
            return i
    return -1

print(findJudge(3, [[1,2],[2,3]]))