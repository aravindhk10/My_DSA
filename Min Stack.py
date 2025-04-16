class MinStack:

    def __init__(self):
        self.ans = []
        self.mini = []

    def push(self, val: int) -> None:
        self.ans.append(val)
        if not self.mini or val<=self.mini[-1]:
            self.mini.append(val) 

    def pop(self) -> None:
        if self.mini and self.ans[-1] == self.mini[-1]:
            self.mini.pop()
        self.ans.pop()

    def top(self) -> int:
        return self.ans[-1]

    def getMin(self) -> int:
        return self.mini[-1]

      
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
