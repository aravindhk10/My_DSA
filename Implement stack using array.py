
class MyStack:
    
    def __init__(self):
        self.arr=[]
        self.Top = -1
    
    #Function to push an integer into the stack.
    def push(self,data):
        #add code here
        self.arr.append(data)
        self.Top+=1
    
    #Function to remove an item from top of the stack.
    def pop(self):
        #add code here
        if self.Top == -1:
            return self.Top
        else:
            self.temp = self.arr[self.Top]
            self.arr.pop(self.Top)
            self.Top-=1
            return self.temp
