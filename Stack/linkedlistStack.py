class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    def __str__(self) -> str:
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Stack():
    def __init__(self) -> None:
        self.linkedlist=LinkedList()
    
    def is_empty(self):
        if self.linkedlist.head is None:
            return True
        return False
    def push(self,value):
        new_node=Node(value)
        new_node.next=self.linkedlist.head
        self.linkedlist.head=new_node

    def pop(self):
        if self.is_empty() :
            return None
        else:
            popped_node=self.linkedlist.head
            self.linkedlist.head=self.linkedlist.head.next
            popped_node.next=None
            return popped_node
    def peek (self):
        if self.is_empty() :
            return None
        else:
            return self.linkedlist.head
    def delete(sefl):
        sefl.linkedlist.head=None

    
    def __str__(self) -> str:
        values=[str(x) for x in self.linkedlist ]
        return "\n".join(values)

stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)


for i in stack.linkedlist:
    print(i)