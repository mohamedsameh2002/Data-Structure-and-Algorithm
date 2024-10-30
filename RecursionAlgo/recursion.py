# Basis
def firstMethod():
    secondMethod()
    print("I am the first Method")

def secondMethod():
    thirdMethod()
    print("I am the second Method")

def thirdMethod():
    fourthMethod()
    print("I am the third Method")

def fourthMethod():
    print("I am the fourth Method")

# Basis

#Factorial: !4=4*3*2*1 , !0=1

def factorial(n):
    assert n > 0 and isinstance(n, int),'The number must be positive interger only!'
    if n in [0,1]:
        return 1
    else:
        return n *factorial(n-1)
    

#Factorial

#Fibonacci : 0,1,1,2,3,5,8,13... -> 0 + 1 = 1 , 1 + 1 = 2 , 2 + 3 = 5 , 3 + 5 = 8 , 5 + 8 = 13.....


def fibonacci(n):
    assert n >= 0 and isinstance(n, int), 'The number must be a non-negative integer!'
    if n in [1,0]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(5))
# Fibonacci


#Find max num

def find_max_num(arr,n):
    if n == 1:
        return arr[0]
    else:
        return max(arr[n-1],find_max_num(arr,n-1))
    
#Find max num


