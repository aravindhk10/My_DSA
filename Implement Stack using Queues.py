from queue import Queue
class MyStack:

    def __init__(self):
        self.q = Queue()

    def push(self, x: int) -> None:
        s = self.q.qsize()
        self.q.put(x)
        for i in range(s):
            self.q.put(self.q.get())

    def pop(self) -> int:
        return self.q.get()
        
    def top(self) -> int:
        return self.q.queue[0]
        
    def empty(self) -> bool:
        return self.q.empty()
