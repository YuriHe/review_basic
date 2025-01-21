import heapq

def find_MaxBalance(s, kit, efficiency_rating):
    # Create two max heaps to store open close
    openHeap, closeHeap = [], []
    
    for i, char in enumerate(kit):
        if char == "(":
            heapq.heappush(openHeap, (-efficiency_rating[i]))
        if char == ")":
            heapq.heappush(closeHeap, (-efficiency_rating[i]))

    # Use stack to check s string and keep imbalanced and pop pair
    stack = []
    for c in s:
        if c =="(":
            stack.append(c)
        elif c == ")" and stack:
            # found match pop
            stack.pop()
        elif c == ")" and not stack:
            stack.append(c)
            
    # Calculate imbalanced parentheses
    max_score = 0
    while stack:
        cur = stack.pop()
        if cur == "(": # extra open, now find largest close from closeHeap
            if closeHeap:
                max_score += (-heapq.heappop(closeHeap))
        elif cur == ")":
            if openHeap:
                max_score += (-heapq.heappop(openHeap))

    # Use kit's remaining pair to maximum rate
    while openHeap and closeHeap:
        openCur = -heapq.heappop(openHeap)
        closeCur = -heapq.heappop(closeHeap)
        max_score = max(max_score, openCur+closeCur+max_score)
    return max_score


# Example Usage
s1 = "()"
kit1 = "(())"
efficiency_ratings1 = [4, 2, -3, -3]
print(find_MaxBalance(s1, kit1, efficiency_ratings1))  # Output: 1

s2 = ")(("
kit2 = ")(()))"
efficiency_ratings2 = [3, 4, 2, -4, -1, -3]
print(find_MaxBalance(s2, kit2, efficiency_ratings2))  # Output: 6

s3 = "()"
kit3 = "()()()"
efficiency_ratings3 = [5, 5, 5, 5, 5, 5]
print(find_MaxBalance(s3, kit3, efficiency_ratings3))  # Output: 30
