# Insertion Sort
"""
Insertion Sort is a simple sorting algorithm that move one element at a time, from left to right.
It works by repeatedly taking an element from the unsorted portion and inserting it into its correct position in the sorted portion of the list.

x <= pivot | pivot | unsort

Example 1:

Input:
pairs = [(5, "apple"), (2, "banana"), (9, "cherry")]

Output:
[[(5, "apple"), (2, "banana"), (9, "cherry")], 
 [(2, "banana"), (5, "apple"), (9, "cherry")], 
 [(2, "banana"), (5, "apple"), (9, "cherry")]]
Notice that the output shows the state of the array after each insertion. The last state is the final sorted array. There should be pairs.length states in total.
"""
# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    """
    Use two pointer, compare cur value to sorted array, if less then swap, continue 
    find smaller in sorted list(from right to left)
    T: O(n^2) for average&worst, O(n) for best
    """
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        res = []
        
        for i in range(n):
            j = i - 1

            while j >= 0 and pairs[j+1].key < pairs[j].key:
                # swap with cur and continue find smaller in sorted list
                pairs[j+1], pairs[j] = pairs[j], pairs[j+1]
                j -= 1

            res.append(pairs[:])

        return res
        




