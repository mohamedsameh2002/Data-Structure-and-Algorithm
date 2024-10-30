from random import randint


class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    def __str__(self) -> str:
        return str(self.value)



class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length =0


    def prepend (self,value):
        new_node=Node(value) 
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length +=1


    def append (self,value):
        new_node=Node(value) 
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length +=1
    
    def insert (self,index,value):
        new_node=Node(value)
        if index < -1 or index > self.length :
            return False
        elif self.length  == 0:
            self.head=new_node
            self.tail=new_node
        elif index == 0:
            new_node.next=self.head
            self.head = new_node
        elif index == -1:
            new_node.next=self.tail.next
            self.tail.next=new_node
            self.tail=new_node
        else:
            temp_node=self.head
            for _ in (range(index-1)):
                temp_node=temp_node.next
            new_node.next=temp_node.next
            temp_node.next=new_node
            if new_node.next == None:
                self.tail = new_node

        self.length +=1
        return True

    def search(self,target):
        current=self.head
        index=0
        while current:
            if current.value == target:
                return index
            current=current.next
            index+=1
        return 'Not found'
    def get (self,index):
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length :
            return None
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
            self.tail=temp
            temp.next=None
        self.length -=1
        return popped_node
    def remove(self,index):
        if index >= self.length  or index < -1:
            return None
        if index == -1 or index == self.length  -1:
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

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head 


    def remove_duplicates(self):
        if self.head is None:
            return
        node_values = set()  # set to store unique node values
        current_node = self.head
        node_values.add(current_node.value)
        while current_node.next:
            if current_node.next.value in node_values:  # duplicate found
                current_node.next = current_node.next.next
                self.length -= 1
            else:
                node_values.add(current_node.next.value)
                current_node = current_node.next
        self.tail = current_node


    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    def generate(self,n,min_value,max_value):
        self.head=None
        self.tail=None
        for _ in range(n):
            self.append(randint(min_value,max_value))
        return self
    
    def __len__(self):
        length=0
        node=self.head
        while node:
            length+=1
            node=node.next
        return length
    def __str__(self) -> str:
        values=[str( x.value) for x in self]
        return ' -> '.join(values)


