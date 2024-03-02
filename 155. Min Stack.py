class MinStack:

    def __init__(self):
        self.ls = []
        # store mini, top is mini, second top is second mini, can be duplicate
        self.minstack = [] 

    def push(self, val: int) -> None:
        self.ls.append(val)
        if len(self.minstack) == 0:
            # first val and also min
            self.minstack.append(val)
        elif val <= self.minstack[-1]:
            self.minstack.append(val)

    def pop(self) -> None:
        if self.ls.pop() == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.ls[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()