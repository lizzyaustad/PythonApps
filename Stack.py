class Stack (object):
    
    def __init__(self):
        self.theStack = []
        
    def push(self,a):
        self.theStack.append(a)
        
    def pop(self):
        return self.theStack.pop()
    
    def isEmpty(self):
        return len(self.theStack) == 0
    
    def peek(self):
        return self.theStack[len(self.theStack)-1]
    
    