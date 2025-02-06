class MyQueue:    
    #Function to push an element x in a queue.
    def __init__(self):
        self.arr = []
        self.Top = 0
    def push(self, x):
         #add code here
        self.arr.append(x)
     
    #Function to pop an element from queue and return that element.
    def pop(self):
        # add code here
        if len(self.arr)==0:
            return -1
        temp = self.arr[self.Top]
        self.arr.pop(self.Top)
        return temp
