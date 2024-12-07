import sys
sys.path.append(r"C:\Users\sista\Downloads\PY")
from QueueMine.linkedlistQueue import Queue 

class TreeNode:
    def __init__(self,data) -> None:
        self.data=data
        self.left_child=None
        self.right_child=None



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
    print(root_node.data)#
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



def searchBT(root_node,node_value):
    if not root_node:
        return None
    queue=Queue()
    queue.enqueue(root_node)
    while not (queue.is_empty()):
        root=queue.dequeue()
        if root.value.data == node_value:
            return True
        else:
            if root.value.left_child:
                queue.enqueue(root.value.left_child)
            if root.value.right_child:
                queue.enqueue(root.value.right_child)
    return False
        


def insert_nodeBT(root_node,value):
    new_node=TreeNode(value)
    if not root_node:
        root_node=new_node
    else:
        queue=Queue()
        queue.enqueue(root_node)
        while not (queue.is_empty()):
            root=queue.dequeue()
            
            if root.value.left_child:
                queue.enqueue(root.value.left_child)
            else:
                root.value.left_child=new_node
                return 'Successfully inserted'
            
            if root.value.right_child:
                queue.enqueue(root.value.right_child)
            else:
                root.value.right_child=new_node
                return 'Successfully inserted'
        


#Delete node


def get_deepest_node(root_node):
    if not root_node:return
    else:
        queue=Queue()
        queue.enqueue(root_node)
        while not (queue.is_empty()):
            root=queue.dequeue()
            if root.value.left_child is not None:
                queue.enqueue(root.value.left_child)
            if root.value.right_child is not None:
                queue.enqueue(root.value.right_child)
        deepest_node=root.value
        return deepest_node

def delete_deepest_node(root_node,dNode):
    if not root_node:return
    else:
        queue=Queue()
        queue.enqueue(root_node)
        while not (queue.is_empty()):
            root=queue.dequeue()
            if root.value is dNode:
                root.value=None
                return
            if root.value.right_child:
                if root.value.right_child is dNode:
                    root.value.right_child=None
                    return
                else:
                    queue.enqueue(root.value.right_child)
            if root.value.left_child:
                if root.value.left_child is dNode:
                    root.value.left_child=None
                    return
                else:
                    queue.enqueue(root.value.left_child)
            
def delete_nodeBT(root_node,node):
    if not root_node:return
    else:
        queue=Queue()
        queue.enqueue(root_node)
        while not (queue.is_empty()):
            root=queue.dequeue()
            if root.value.data == node:
                dNode=get_deepest_node(root_node)
                root.value.data=dNode.data
                delete_deepest_node(root_node,dNode)
                return "The node has been successfully deleted"
            if root.value.left_child is not None:
                queue.enqueue(root.value.left_child)
            if root.value.right_child is not None:
                queue.enqueue(root.value.right_child)
        return "Faild to delete"


#Delete node
#------------------------------

def deleteBT(root_node):
    root_node.data=None
    root_node.left_child=None
    root_node.right_child=None

tree=TreeNode(3)
insert_nodeBT(tree,2)
insert_nodeBT(tree,7)
insert_nodeBT(tree,8)
insert_nodeBT(tree,5)
insert_nodeBT(tree,4)
insert_nodeBT(tree,2)
pre_order_traversal(tree)