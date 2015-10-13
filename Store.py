class Store (object):

    def __init__(self):
        self.theStore = []
    
    def operator(self, string):
        if (string=='+' or string=='-'):
            if (len(self.theStore)!=0):
                if (self.theStore.pop()>=1):
                    stack.push(string)
            self.theStore.append(string)
            self.theStore.append(1)
           
        if (string=='*' or string=='/'):
            while (len(self.theStore)!=0):
                while (self.theStore.pop()>=2):
                    stack.push(string)
            self.theStore.append(string)
            self.theStore.append(2)

       # if (string=='('):
         #  a

        if (string=='='):
            while (len(self.theStore)!=0):
                stack.push(self.theStore.pop())
