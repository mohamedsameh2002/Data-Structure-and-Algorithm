class BinaryTree:
    def __init__(self,size) -> None:
        self.list=size * [None]
        self.last_used_index=0
        self.max_size=size
    
    def insert_node(self,value):
        if self.last_used_index+1 == self.max_size:return False
        self.list[self.last_used_index+1]=value
        self.last_used_index+=1
        return True
    
    def search_node(self,value):
        for i in range(len(self.list)):
            if self.list[i] == value:
                return True
        return False
    

    #Depth first search
    def pre_order_traversal(self,index):
        assert isinstance(index,int),"Number must be int"
        if index > self.last_used_index or 0 >= index:
            return
        print(self.list[index])
        self.pre_order_traversal(index*2)
        self.pre_order_traversal(index*2 + 1)

    def in_order_traversal(self,index):
        assert isinstance(index,int),"Number must be int"
        if index > self.last_used_index or 0 >= index:
            return
        self.in_order_traversal(index*2)
        print(self.list[index])
        self.in_order_traversal(index*2 + 1)

    def post_order_traversal(self,index):
        assert isinstance(index,int),"Number must be int"
        if index > self.last_used_index or 0 >= index:
            return
        self.in_order_traversal(index*2)
        self.in_order_traversal(index*2 + 1)
        print(self.list[index])
    #Depth first search
    #-----------------------------


    #Breadth first search
    def level_order_traversal(self,index):
        assert isinstance(index,int),"Number must be int"
        if index > self.last_used_index or 0 >= index:
            return
        for i in range(index,self.last_used_index+1):
            print(self.list[i])
    #Breadth first search
    #-----------------------------

    
    def delete_node(self,node):
        if self.last_used_index == 0:return False
        for i in range(1,self.last_used_index+1):
            if self.list[i] == node:
                self.list[i]=self.list[self.last_used_index]
                self.list[self.last_used_index]=None
                self.last_used_index-=1
                
    def deleteBT(self):
        self.list=None
        return True


tree=BinaryTree(10)
tree.insert_node('Drinks')
tree.insert_node('Hot')
tree.insert_node('Cold')
tree.insert_node('Tea')
tree.insert_node('Coffee')
tree.insert_node('Soda')
tree.insert_node('Fanta')


