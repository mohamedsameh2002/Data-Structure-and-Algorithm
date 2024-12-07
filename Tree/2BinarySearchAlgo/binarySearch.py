import sys
sys.path.append(r"C:\Users\sista\Downloads\PY")
from QueueMine.linkedlistQueue import Queue 

class BSTNode:
    def __init__(self,data) -> None:
        self.data=data
        self.left_child=None
        self.right_child=None
    def __str__(self) -> str:
        return str(self.data)


def insert_node(root_node,node_value):
    if root_node.data == None:
        root_node.data = node_value
    elif root_node.data > node_value :
        if root_node.left_child is None:
            root_node.left_child = BSTNode(node_value)
        else:
            insert_node(root_node.left_child,node_value)
    else:
        if root_node.right_child is None:
            root_node.right_child = BSTNode(node_value)
        else:
            insert_node(root_node.right_child,node_value)
    return True



#Depth first search
def pre_order_traversal(root_node):
    if not root_node:
        return
    print(root_node.data)
    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.right_child)


def in_order_traversal(root_node):
    if not root_node:
        return
    in_order_traversal(root_node.left_child)
    print(root_node.data)
    in_order_traversal(root_node.right_child)


def post_order_traversal(root_node):
    if not root_node:
        return
    post_order_traversal(root_node.left_child)
    post_order_traversal(root_node.right_child)
    print(root_node.data)
#Depth first search
#-----------------------------


#Breadth first search
def level_order_traversal(root_node):
    if not root_node:
        return
    queue=Queue()
    queue.enqueue(root_node)
    while not (queue.is_empty()):
        root=queue.dequeue()
        print(root.value.data)
        if root.value.left_child is not None:
            queue.enqueue(root.value.left_child)
        if root.value.right_child is not None:
            queue.enqueue(root.value.right_child)
#Breadth first search
#-----------------------------

def search_node(root_node, value):
    if root_node is None:
        return False
    
    if root_node.data == value:
        return True
    
    if root_node.data > value:
        return search_node(root_node.left_child, value)
    else:
        return search_node(root_node.right_child, value)

def min_value_node(root_node):
    current=root_node
    while current.left_child is not None:
        current=current.left_child
    return current

def delete_node(root_node,value):
    if root_node is None:return root_node
    if value < root_node.data:
        root_node.left_child=delete_node(root_node.left_child,value)
    elif value > root_node.data:
        root_node.right_child=delete_node(root_node.right_child,value)
    else:
        if root_node.left_child is None:
            temp=root_node.right_child
            root_node=None
            return temp
        if root_node.right_child is None:
            temp=root_node.left_child
            root_node=None
            return temp
        temp = min_value_node(root_node.right_child)
        root_node.data=temp.data
        root_node.right_child=delete_node(root_node.right_child,temp.data)
    return root_node


def deleteBST(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return "The BST has been successfully deleted"


tree=BSTNode(None)



