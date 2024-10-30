import ctypes

class Stack:
    def __init__(self, max_size) -> None:
        self.max_size = max_size
        self.array_type = ctypes.py_object * max_size 
        self.stack_array = self.array_type()  
        self.top = -1  

    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.max_size - 1
    
    def push(self, value):
        if self.is_full():
            return False
        self.top += 1
        self.stack_array[self.top] = value
        print(ctypes.sizeof(self.stack_array))
        return True
    
    def pop(self):
        if self.is_empty():
            return None
        value = self.stack_array[self.top]
        self.top -= 1
        return value
        
    def peek(self):
        if self.is_empty():
            return None
        return self.stack_array[self.top]
        
    def delete(self):
        self.top = -1  
        
    def __str__(self) -> str:
        values = [self.stack_array[i] for i in range(self.top, -1, -1)]
        return "\n".join(map(str, values))


stack=Stack(3)
stack.push(1)
stack.push(2)
stack.push(2)
stack.push(2)
stack.push(60)






# class Stack:
#     def __init__(self,max_size) -> None:
#         self.max_size=max_size
#         self.list=[]

#     def is_empty(self):
#         if self.list == []:
#             return True
#         return False
    
#     def is_full(self):
#         if len(self.list) == self.max_size:
#             return True
#         return False
    
#     def push (self,value):
#         if self.is_full():
#             return False
#         else:
#             self.list.append(value)
#         return True
    
#     def pop(self):
#         if self.is_empty():
#             return None
#         else:
#             return self.list.pop()
        
#     def peek(self):
#         if self.is_empty():
#             return None
#         else:
#             return self.list[-1]
        
#     def delete (self):
#         self.list = []
        
#     def __str__(self) -> str:
#         values=[str(x) for x in reversed(self.list) ]
#         return "\n".join(values)
