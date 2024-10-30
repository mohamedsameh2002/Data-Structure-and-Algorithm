class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class DLinkedList:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
        self.length=0


    def append(self,value):
        new_node=Node(value)
        if not self.head:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1

    def prepend (self,value):
        new_node=Node(value)
        if not self.head:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node 
        self.length+=1


    def search(self,target):
        current=self.head
        index=0
        while current:
            if current.value == target:
                return index
            current=current.next
            index+=1
        return None
    

    def get (self,index:int):
            current_node=None
            if index == -1:
                return self.tail
            if index < -1 or index >= self.length :
                return None
            if index < self.length // 2:
                current_node=self.head
                for _ in range(index):
                    current_node=current_node.next
            else:
                current_node=self.tail
                for _ in range(self.length-1,index,-1):
                    current_node=current_node.prev
            return current_node
    

    def insert (self,index,value):
        new_node=Node(value)
        if index < -1 or index > self.length :
            return False
        if index == 0:
            return self.prepend(value)
        if index == -1 or index == self.length :
            return self.append(value)
        temp_node=self.get(index-1)
        new_node.next=temp_node.next
        new_node.prev=temp_node
        temp_node.next.prev=new_node
        temp_node.next=new_node
        self.length+=1

    def set_value(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    def pop_first(self):
        if not self.head:
            return None
        popped_node=self.head
        if self.length == 1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None
            popped_node.next=None
        self.length-=1
        return popped_node
    
    def pop (self):
        if not self.tail:
            return None
        popped_node=self.tail
        if self.length == 1:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
            popped_node.prev=None
            
        self.length-=1
        return popped_node
    
    def remove(self,index):
        if index >= self.length  or index < -1:
            return None
        if index == -1 or index == self.length  -1:
            return self.pop()
        if index == 0:
            return self.pop_first()
        popped_node=self.get(index)
        popped_node.prev.next=popped_node.next
        popped_node.next.prev=popped_node.prev
        popped_node.next=None
        popped_node.prev=None
        return popped_node


    
    def __str__(self) -> str:
        temp_node=self.head
        result=""
        while temp_node:
            result+=str(temp_node.value)
            if temp_node.next:
                result+=" <-> "
            temp_node=temp_node.next
        return result




ds_linkedList=DLinkedList()
ds_linkedList.append(10)
ds_linkedList.append(20)
ds_linkedList.append(30)
ds_linkedList.append(40)
ds_linkedList.append(40)
ds_linkedList.append(90)
ds_linkedList.append(40)
# ds_linkedList.insert(4,50)
print(ds_linkedList.get(5).value)