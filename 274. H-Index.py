"""
    Question: H index
    Definition: at least h papers have each been cited at least h times， remaining N-H paper no more than h citation
    citations  =[3,0,6,1,5]
    count_array=[1,1,0,1,0,2]
"""
def hIndex(citations):
    n = len(citations)
    if n == 0: return 0

    # Step 1: Create a count array store how many paper have each citation from 0 to n
    count = [0] * (n + 1)
    
    # Count each citation frequency
    for citation in citations:
        if citation >= n:
            count[n] += 1  # Count papers with citations >= n
        else:
            count[citation] += 1
    print(count)
    # Step 2: Calculate the h-index
    # iterate froom n down to 0, keep a running total of how many papers have at least h citations(what is reason why no need to explictly check remaining N-h paper)
    total_papers = 0
    for h in range(n, -1, -1):
        print(f"check total paper {total_papers} for h {h} and count: {count[h]}")
        total_papers += count[h]
        if total_papers >= h:
            return h

    return 0
        
print(hIndex([3,0,6,1,5]))