from queue import LifoQueue
class MyQueue:

    def __init__(self):
        self.s1 = LifoQueue()
        self.s2 = LifoQueue()

    def push(self, x: int) -> None:
        self.s1.put(x)
    def pop(self) -> int:
        if self.s2.empty() == False:
            return self.s2.get()
        else:
            while (self.s1.empty()==False):
                self.s2.put(self.s1.get())
            return self.s2.get()
    def peek(self) -> int:
        if self.s2.empty() == False:
            return self.s2.queue[-1]
        else:
            while (self.s1.empty()==False):
                self.s2.put(self.s1.get())
            return self.s2.queue[-1]

    def empty(self) -> bool:
      return self.s1.empty() and self.s2.empty()
