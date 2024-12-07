import sys
sys.path.append(r"C:\Users\sista\Downloads\PY")
from QueueMine.linkedlistQueue import Queue 

class AVLNode:
    def __init__(self,data) -> None:
        self.data=data
        self.left_child=None
        self.right_child=None
        self.height=1
    def __str__(self) -> str:
        return str(self.data)



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

def get_height(root_node):
    return 0 if not root_node else root_node.height

def right_rotate(disbalanced_node):
    new_node=disbalanced_node.left_child
    disbalanced_node.left_child=disbalanced_node.left_child.right_child
    new_node.right_child=disbalanced_node
    disbalanced_node.height= 1 + max(get_height(disbalanced_node.left_child),get_height(disbalanced_node.right_child))
    new_node.height= 1 + max(get_height(new_node.left_child),get_height(new_node.right_child))
    return new_node

def left_rotate(disbalanced_node):
    new_node=disbalanced_node.right_child
    disbalanced_node.right_child=disbalanced_node.right_child.left_child
    new_node.left_child=disbalanced_node
    disbalanced_node.height= 1 + max(get_height(disbalanced_node.left_child),get_height(disbalanced_node.right_child))
    new_node.height= 1 + max(get_height(new_node.left_child),get_height(new_node.right_child))
    return new_node


def get_balance(root_node):
    if not root_node :
        return 0
    return get_height(root_node.left_child) - get_height(root_node.right_child)


def insert_node(root_node,node_value):
    if not root_node:
        return AVLNode(node_value)
    elif node_value < root_node.data:
        root_node.left_child = insert_node(root_node.left_child,node_value)
    else:
        root_node.right_child = insert_node(root_node.right_child,node_value)

    root_node.height= 1 + max(get_height(root_node.left_child),get_height(root_node.right_child))
    balance=get_balance(root_node) 

    #LL
    if balance > 1 and node_value < root_node.left_child.data:
        return right_rotate(root_node)
    
    #LR
    if balance > 1 and node_value > root_node.left_child.data:
        root_node.left_child=left_rotate(root_node.left_child)
        return right_rotate(root_node)
    
    #RR
    if balance < -1 and node_value > root_node.right_child.data:
        return left_rotate(root_node)
    
    #RL
    if balance < -1 and node_value < root_node.right_child.data:
        root_node.right_child=right_rotate(root_node.right_child)
        return left_rotate(root_node)
    
    return root_node


def min_value_node(root_node):
    if root_node is None or root_node.left_child is None:
        return root_node
    return min_value_node(root_node.left_child)





def delete_node(root_node,value):
    if not root_node:
        return root_node
    elif value < root_node.data:
        root_node.left_child=delete_node(root_node.left_child,value)
    elif value > root_node.data:
        root_node.right_child=delete_node(root_node.right_child,value)
    else:
        if root_node.left_child is None:
            temp=root_node.right_child
            root_node=None
            return temp
        elif root_node.right_child is None:
            temp=root_node.left_child
            root_node=None
            return temp
        temp = min_value_node(root_node.right_child)
        root_node.data=temp.data
        root_node.right_child=delete_node(root_node.right_child,temp.data)

    root_node.height= 1 + max(get_height(root_node.left_child),get_height(root_node.right_child))
    balance=get_balance(root_node) 

    #LL
    if balance > 1 and  get_balance(root_node.left_child) >= 0:
        return right_rotate(root_node)
    
    #LR
    if balance > 1 and  get_balance(root_node.left_child) < 0:
        root_node.left_child=left_rotate(root_node.left_child)
        return right_rotate(root_node)
    
    #RR
    if balance < -1 and  get_balance(root_node.right_child) <= 0:
        return left_rotate(root_node)
    
    #RL
    if balance < -1 and  get_balance(root_node.right_child) > 0:
        root_node.right_child=left_rotate(root_node.right_child)
        return left_rotate(root_node)
    
    return root_node



def deleteAVL(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return "The AVL has been successfully deleted"


avl_tree=AVLNode(90)
avl_tree=insert_node(avl_tree,85)
avl_tree=insert_node(avl_tree,150)

avl_tree=insert_node(avl_tree,80)
avl_tree=insert_node(avl_tree,86)
avl_tree=insert_node(avl_tree,140)
avl_tree=insert_node(avl_tree,160)
avl_tree=insert_node(avl_tree,170)

avl_tree=insert_node(avl_tree,75)
avl_tree=insert_node(avl_tree,82)
avl_tree=insert_node(avl_tree,138)
avl_tree=insert_node(avl_tree,158)
avl_tree=insert_node(avl_tree,168)
avl_tree=insert_node(avl_tree,180)
avl_tree=insert_node(avl_tree,165)



level_order_traversal(avl_tree)


