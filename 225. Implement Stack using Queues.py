from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque([])

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        # q=1,2,3, pop: 1,2,3 tmp:1,2, pop 3, q= tmp
        tmp = deque([])
        first = None
        while self.q:
            first = self.q.popleft()
            if self.q:
                # not last one
                tmp.append(first)
            else:
                break
        # assign tmp to q
        self.q = tmp
        return first

    def top(self) -> int:
        # q=1,2,3, pop: 1,2,3 tmp:1,2, return (no pop) 3, q= tmp
        tmp = deque([])
        first = None
        while self.q:
            first = self.q.popleft()
            tmp.append(first)
        # assign tmp to q
        self.q = tmp
        return first

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()