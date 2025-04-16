class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.top = self.stack[-1]

    def pop(self) -> int:
        tmp = []
        # pop whole stack, and push into tmp
        while self.stack:
            val = self.stack.pop()
            tmp.append(val)
            
        if tmp:
            top = tmp[-1]
            tmp.pop() # pop first one
            while tmp: # push back to stack
                self.stack.append(tmp.pop())
            return top
        else:
            return -1 # nothing to pop

    def peek(self) -> int:
        tmp = []
        # pop whole stack, and push into tmp
        while self.stack:
            val = self.stack.pop()
            tmp.append(val)
        if tmp:
            top = tmp[-1]
            while tmp: # push back to stack
                self.stack.append(tmp.pop())
            return top
        else:
            return -1 # nothing to pop

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()