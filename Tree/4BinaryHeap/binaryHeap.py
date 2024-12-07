class Heap:
    def __init__(self,size):
        self.list=[None] * (size+1)
        self.exist_items_len=0
        self.max_size= size + 1
    
    def peek(self):
        return None if self.exist_items_len == 0 else self.list[1]
    
    def sizeof_heap(self):
        return self.exist_items_len
    
    def level_order_traversal(self):
        for i in range(1,self.exist_items_len+1):
            print(self.list[i])

    def heapify_tree_insert(self,index,heapType):
        parent_index=int(index/2)
        if index <=1:
            return
        if heapType == 'min':
            if self.list[index] < self.list[parent_index]:
                temp=self.list[index]
                self.list[index]=self.list[parent_index]
                self.list[parent_index]=temp
            self.heapify_tree_insert(parent_index,heapType)
        elif heapType == 'max':
            if self.list[index] > self.list[parent_index]:
                temp=self.list[index]
                self.list[index]=self.list[parent_index]
                self.list[parent_index]=temp
            self.heapify_tree_insert(parent_index,heapType)
    
    def insert(self,value,heapType):
        if self.exist_items_len+1 == self.max_size:
            return False
        self.list[self.exist_items_len+1]=value
        self.exist_items_len+=1
        self.heapify_tree_insert(self.exist_items_len,heapType)
        return True
    
    def heapify_tree_extract(self,index,heapType):
        left_index= index * 2
        right_index=(index * 2) + 1
        swap_child=0
        # Has no children.
        if self.exist_items_len < left_index:
            return
        # Has one left child
        elif self.exist_items_len == left_index:
            if heapType == 'min':
                if self.list[index] > self.list[left_index]:
                    temp=self.list[index]
                    self.list[index]=self.list[left_index]
                    self.list[left_index]=temp
                return
            elif heapType == 'max':  
                if self.list[index] < self.list[left_index]:
                    temp=self.list[index]
                    self.list[index]=self.list[left_index]
                    self.list[left_index]=temp
                return
        # Has tow children
        else:
            if heapType == 'min':
                if self.list[left_index] < self.list[right_index] :
                    swap_child=left_index
                else:
                    swap_child=right_index
                
                if self.list[index] > self.list[swap_child]:
                    temp=self.list[index]
                    self.list[index]=self.list[left_index]
                    self.list[left_index]=temp
                
            elif heapType == 'max':
                if self.list[left_index] > self.list[right_index] :
                    swap_child=left_index
                else:
                    swap_child=right_index
                
                if self.list[index] < self.list[swap_child]:
                    temp=self.list[index]
                    self.list[index]=self.list[left_index]
                    self.list[left_index]=temp
        self.heapify_tree_extract(swap_child,heapType)

    def extract(self,heapType):
        if self.exist_items_len == 0:
            return None
        extracted_node=self.list[1]
        self.list[1]=self.list[self.exist_items_len]
        self.list[self.exist_items_len]=None
        self.exist_items_len-=1
        self.heapify_tree_extract(1,heapType)
        return extracted_node
    
    def delete(self):
        self.list=None

heap=Heap(12)
heap.insert(5,'min')
heap.insert(10,'min')
heap.insert(20,'min')
heap.insert(30,'min')
heap.insert(40,'min')
heap.insert(50,'min')
heap.insert(60,'min')
heap.insert(4,'min')
heap.insert(2,'min')

