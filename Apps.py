from Stack import Stack

class Operator (object):

    def __init__(self):
        self.operator=""
        self.precedence=0
  

#returns True if a is a String representing a number, False otherwise
def num(a):
    try:
        int(a)
        return True
    except ValueError:
        return False
    
def tenToTwo(toConvert):
    stack = Stack()
    while toConvert > 0:
        stack.push(toConvert % 2)
        toConvert = toConvert // 2    # integer division
    answer = ""
    while not stack.isEmpty():
        answer = answer + str(stack.pop())
    return answer

def reverse(a):
    stack = Stack()
    for x in a:
        stack.push(x)
    answer = ""
    while not stack.isEmpty():
        answer = answer + stack.pop()
    return answer

def balanced(a):
    stack = Stack()
    b=0
    for x in a:
        if (x=='['): 
            stack.push(1)  
        if (x=='('):
            stack.push(2)
        if (x=='{'):
            stack.push(3)

        if (x==']'):
            if (stack.isEmpty()):
                return False
            b=stack.pop()
            if (b!=1):
                return False
        if (x==')'):
            if (stack.isEmpty()):
                return False
            b=stack.pop()
            if (b!=2):
                return False
        if (x=='}'):
            if (stack.isEmpty()):
                return False
            b=stack.pop()
            if (b!=3):
                return False

    if (stack.isEmpty()):    
        return True
    else:
        return False

def value(x):
    stack = Stack()
    list=x.split()
    answer=0
    for a in list:
        stack.push(a)
        if (a=='+'):
            stack.pop()
            answer=int(stack.pop())+int(stack.pop())
            stack.push(answer)
        if (a=='-'):
            stack.pop()
            b=stack.pop()
            c=stack.pop()
            answer=int(c)-int(b)
            stack.push(answer)
        if (a=='*'):
            stack.pop()
            answer=int(stack.pop())*int(stack.pop())
            stack.push(answer)
        if (a=='/'):
            stack.pop()
            b=stack.pop()
            c=stack.pop()
            answer=int(c)/int(b)
            stack.push(answer)
        if (a=='='):
            return answer

    return 0


def convert(a):
    stack=Stack()
    stack.push(0)
    op=Operator()
    list=a.split()
    answer=""
    b=""
    m=1
    n=2
    for x in list:
      
        if (num(x)==True):
            answer = answer + x + " "
        if (x=='='):
            while not stack.isEmpty():
                popped=stack.pop()
                if (num(popped)==True):
                    answer = answer + " " + str(stack.pop())
                if (num(popped)!=True):
                    answer = answer + " " + popped
            answer = answer + " ="
        if (x=='+' or x=='-'):
            popped=stack.pop()
            if (popped>=m):
                answer = answer + stack.pop() + " "
                stack.push(x)
                stack.push(m)
            if (popped<m):
                stack.push(x)
                stack.push(m)
           
        if (x=='*' or x=='/'):
            popped=stack.pop()
            if (popped>=n):
                answer = answer + stack.pop() + " "
                stack.push(x)
                stack.push(n)
                
            if (popped<n):
                stack.push(x)
                stack.push(n)

        if (x=='('):
            m=m+4
            n=n+4
        if (x==')'):
            m=m-4
            n=n-4
    
    return answer

print("Convert to binary:")                
print("15: "+tenToTwo(15))
print("1027: "+tenToTwo(1027))

print()
print("Reverse:")
toreverse = "god yzal eht revo spmuj xof nworb kciuq eht"
print(toreverse)
print(reverse(toreverse))

print()
print("Check balance:")
tobalance = "((){})[]]"
truebalance = "[]({})"
print(tobalance+": "+str(balanced(tobalance)))
print(truebalance+": "+str(balanced(truebalance)))

print()
print("infix to postfix:")
toconvert = "4 + ( 10 - 5 ) * 6 ="
print("infix: "+ str(toconvert))
converted = convert(toconvert)
print("postfix: "+str(convert(toconvert)))

print()
print("Evaluate postfix:")
tosum = "1 2 + 3 * 14 - ="
print(converted+" "+str(value(converted)))
print(tosum+" "+str(value(tosum)))



