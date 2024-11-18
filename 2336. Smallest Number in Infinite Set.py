class SmallestInfiniteSet:
    """
    How to handle infinite set from [1 ....]
    """
    def __init__(self):
        # smallest in existing infinite set
        self.nextone = 1
        # remove set
        self.moved = set()
        
    def popSmallest(self) -> int: 
        res = self.nextone
        self.moved.add(res)
        while self.nextone in self.moved: # consider addback/pop
            self.nextone += 1

        return res
        
    def addBack(self, num: int) -> None:
        if num in self.moved: # removed
            self.moved.discard(num)
            # update smallest
            self.nextone = min(self.nextone, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)