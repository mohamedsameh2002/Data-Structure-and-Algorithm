class Stack:
    def __init__(self) -> None:
        self.list=[]
    def is_empty(self):
        if self.list == []:
            return True
        return False
    def push (self,value):
        self.list.append(value)
        return True
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.list.pop()
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.list[-1]
    def delete (self):
        self.list = []
        
    def __str__(self) -> str:
        values=[str(x) for x in reversed(self.list) ]
        return "\n".join(values)
    


stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())