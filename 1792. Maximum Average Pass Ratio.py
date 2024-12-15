class Solution:
    """
    Question: increase pass ratio for each class
    1.increase ratio: a+1 / b+1 - a/b if add 1 student to this current class
    2.use heap to store (incre_retio, newpass, newtotal)
    3.pop out one classes and re-calculate if add one student until assign all students
    3.sum up the heap
    """
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # this formulate is to acculate potential profit, no actual student added
        def incre_ratio(a, b):
            return (a+1) / (b+1) - a/b
        
        # create maxheap, most incre_ratio is on the top  will add extra for it 
        maxheap = []
        # first heapify whole original classes
        for a, b in classes:
            tp = (-incre_ratio(a,b), a, b)
            maxheap.append(tp)
        # heapify O(n)
        heapq.heapify(maxheap)

        # add extra student
        for _ in range(extraStudents):
            # based on pop result, and push again 
            _, a, b = heapq.heappop(maxheap)
            tp = (-incre_ratio(a+1, b+1), a+1, b+1)
            heapq.heappush(maxheap, tp)
        
        return sum(a/b for _, a, b in maxheap) / len(classes)

        
