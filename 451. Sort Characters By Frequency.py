"""
    Question: return sorted s in decreasing order based on frequency of chars
"""
def frequencySort(self, s: str) -> str:
    # Solution1: Brute force T:nlogn. S:O(n)
    dic = {}
    for c in s:
        dic[c] = dic.get(c, 0) + 1
    # sort key based on val in decreasing order 
    ls = sorted(dic, key=dic.get, reverse=True)
    # display all chars based on frequencey 
    res = ""
    for char in ls:
        freq = dic[char]
        res += char*freq
    return res

    # Solution2: heap T: O(nlogn), S: O(n)
    counter = Counter(s)
    # create heap list
    pq = [(-freq, char) for char, freq in counter.items()]
    # heapify/sort pq O(nlogn)
    heapq.heapify(pq)
    res = ""
    while pq:
        freq, char = heapq.heappop(pq)
        res += char*(-freq)
    return res
