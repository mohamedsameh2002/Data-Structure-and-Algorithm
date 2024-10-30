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
    def __iter__(self):
        cur_node=self.head
        while cur_node:
            yield cur_node
            cur_node=cur_node.next

class Queue:
    def __init__(self) -> None:
        self.linkedlist=LinkedList()

    def __str__(self) -> str:
        values=[str(x) for x in self.linkedlist]
        return ' '.join(values)
    
    def enqueue (self,value):
        new_node=Node(value)
        if not self.linkedlist.head:
            self.linkedlist.head=new_node
            self.linkedlist.tail=new_node
        else:
            self.linkedlist.tail.next =new_node
            self.linkedlist.tail =new_node
        
    def dequeue (self):
        if not self.linkedlist.head :return None
            
        first_node=self.linkedlist.head
        if self.linkedlist.head == self.linkedlist.tail:
            self.linkedlist.head=None
            self.linkedlist.tail=None
        else:
            self.linkedlist.head=self.linkedlist.head.next 
        first_node.next = None
        return first_node
    
    def peek (self):
        return None if not self.linkedlist.head else self.linkedlist.head
    
    def is_empty (self):
        return self.linkedlist.head == None
    
    def delete(self):
        self.linkedlist.head=None
        self.linkedlist.tail=None
        