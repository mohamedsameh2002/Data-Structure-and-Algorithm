class Queue:
    def __init__(self) -> None:
        self.items=[]

    def __str__(self) -> str:
        values=[str(x) for x in self.items]
        return ' '.join(values)
    
    def is_empty(self):
        return self.items == []
    
    def enqueue(self,value):
        return self.items.append(value)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)
    
    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]
    
    def delete(self):
        self.items=None


queue=Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
