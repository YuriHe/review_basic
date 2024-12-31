class Solution:
    """
Question:reach value 0 keep jump at i+arr[i] or i-arr[i] in loop until find result
Topic:DFS Recursion+visit, try all paths to find result(T/F)
    """
    def canReach(self, arr: List[int], start: int) -> bool:
        # base case
        if start < 0 or start >=len(arr) or arr[start]<0:
            return False
        if arr[start] == 0:
            return True
        # set visited avoid infinite loop
        arr[start] *= -1
        # recursion 
        return self.canReach(arr, start+arr[start]) or self.canReach(arr, start-arr[start])
