"""
    Question: Search in sorted list of chars, compare chars, find smallests char which greater than target
    Topic:char<->ASCII
    Issue:duplicate chars change boundary
    Pattern: mid+-1 avoid loop
"""
def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    low, high = 0, len(letters)-1
    while low <= high:
        mid = (low + high) // 2
        if ord(letters[mid]) <= ord(target): # track upper bound
            low = mid + 1
        else:
            high = mid - 1
    if low == len(letters): return letters[0] # no one greater than targer
    else: return letters[low]
