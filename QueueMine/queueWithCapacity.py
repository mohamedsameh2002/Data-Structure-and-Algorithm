class Queue:
    def __init__(self,max_size):
        self.items= max_size * [None]
        self.max_size=max_size
        self.start=-1
        self.top=-1

    def __str__(self) -> str:
        values=[str(x) for x in self.items]
        return ' '.join(values)
    
    def is_full (self):
        if self.top +1 == self.start:
            return True
        elif self.start == 0 and self.top+1 == self.max_size:
            return True
        else:
            return False

    def is_empty (self):
        return self.top == -1
    
    def enqueue (self,value):
        if self.is_full():
            return None
        else:
            if self.top+1 == self.max_size:
                self.top = 0
            else:
                self.top +=1
                if self.start == -1:
                    self.start=0
            self.items[self.top]=value
            return True
        
    def dequeue (self):
        if self.is_empty():
            return None
        else:
            first_elemnt=self.items[self.start]
            start=self.start
            if self.start == self.top:
                self.start=-1
                self.top=-1
            elif self.start+1 == self.max_size:
                self.start=0
            else:
                self.start+=1
            self.items[start]=None
            return first_elemnt
        

    def peek (self):
        return False if self.is_empty() else self.items[self.start]
    
    def delete(self):
        self.top=-1
        self.start=-1
        self.items=self.items * [None]

    



queue=Queue(4)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.dequeue()
queue.dequeue()
queue.enqueue(5)

print(queue)