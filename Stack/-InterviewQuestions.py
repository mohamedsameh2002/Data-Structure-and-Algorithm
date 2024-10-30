#Three in One:how you colud use a single python list to implement three stacks
# for Stack 1 - [0],[1],[2]----->[0,n/3]
# for Stack 2 - [3],[4],[6]----->[n/3,2n/3]
# for Stack 3 - [7],[8],[9]----->[2n/3,n]

class MultiStack:
    def __init__(self,stack_size) -> None:
        self.number_stacks=3
        self.cust_list= [0] * (stack_size * self.number_stacks)
        self.sizes = [0] * self.number_stacks
        self.stack_size=stack_size

    def is_full(self,stack_num):
        return self.sizes[stack_num] == self.stack_size
    
    def is_empty(self,stack_num):
        return self.sizes[stack_num] == 0
    
    def index_of_top(self,stack_num):
        offset=stack_num * self.stack_size # 0 * 6 = 0,كدا احنا في اول ستاك عشان بدأنا نعد من صفر, دلوقت في الخطوه التانيه هنشوف  في كام عنصر في  اول ستاك
        return offset + self.sizes[stack_num]-1# اربعه بعد عشره هتبقا اربعتاشر ناقص واحد بقت انكس تلاتاشر
    
    def push(self,stack_num,value):
        if self.is_full(stack_num):
            return False
        else:
            self.sizes[stack_num]+=1
            self.cust_list[self.index_of_top(stack_num)]=value

    def pop(self,stack_num):
        if self.is_empty(stack_num):
            return None
        else:
            value=self.cust_list[self.index_of_top(stack_num)]
            self.cust_list[self.index_of_top(stack_num)]=0
            self.sizes[stack_num]-=1
        return value
    
    def peek(self,stack_num):
        if self.is_empty(stack_num):
            return None
        else:
            return self.cust_list[self.index_of_top(stack_num)]




multi_stack=MultiStack(5)

print(multi_stack.index_of_top(1))