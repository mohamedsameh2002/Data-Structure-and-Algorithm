class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,value):
        new_node=Node(value)
        if self.length == 0:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
        else:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node
        self.length+=1
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=new_node
        self.length+=1

    def insert (self,index,value):
        new_node=Node(value)
        if index < -1 or index > self.length:
            raise Exception("Index out of the range")
        if self.length == 0:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
        elif index == -1 or index == self.length:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node

        elif index == 0:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=new_node

        else:
            temp_node=self.head
            for _ in range(index-1):
                temp_node=temp_node.next
            new_node.next=temp_node.next
            temp_node.next=new_node
        self.length+=1
    def search(self,target):
        index=0
        current=self.head
        while current:
            if current.value == target:
                return index
            current=current.next
            index+=1
            if current == self.head:
                break
        return None
    

    def get(self,index):
        if index < -1 or index >= self.length:
            return None
        elif index == -1 or index == self.length-1:
            return self.tail
        current=self.head
        for _ in range(index):
            current=current.next
        return current
    def set_value(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    def pop_first(self):
        popped_node=self.head
        if self.length  == 0:
            return None
        if self.length  == 1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.tail.next=self.head
            popped_node.next=None
        self.length -=1
        return popped_node
    

    def pop(self):
        popped_node=self.tail
        if self.length  == 0:
            return None
        if self.length  == 1:
            self.head = self.tail =None
        else:
            temp=self.head
            while temp.next is not self.tail:
                temp=temp.next
            temp.next=self.head
            self.tail=temp
            popped_node.next=None
        self.length -=1
        return popped_node
    

    def remove(self,index):
        if index >= self.length  or index < -1:
            return None
        if index == -1 or index == self.length-1:
            return self.pop()
        if index == 0:
            return self.pop_first()
        prev_noed=self.get(index-1)
        popped_node=prev_noed.next
        prev_noed.next=popped_node.next
        popped_node.next=None
        self.length -=1
        return popped_node
    
    def delete_all(self):
        self.head=None
        self.tail=None
        self.length =0


        
    def __str__(self) :
        temp_node=self.head
        result=''
        while temp_node:
            result+=str(temp_node.value)
            temp_node =temp_node.next
            if temp_node == self.head:
                break
            result +=' -> '
        return result






cs_linkedList=CSLinkedList()


for i in range(6):
    cs_linkedList.append(i)


cs_linkedList.remove(5)

print(cs_linkedList)



