class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)
    def __repr__(self):
        return self.__str__()

#https://leetcode.com/problems/valid-parentheses/description
class Solution:
    def isValid(self, s):
        values = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for i in s:
            if i in values:  
                stack.append(i)
            elif i in values.values():  
                if not stack or values[stack.pop()] != i:
                    return False
        return len(stack) == 0


# https://leetcode.com/problems/clear-digits/description/
class Solution:
    def clearDigits(self, s:str):
        stack=[]
        for i in s:
            if stack and i.isdigit():
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)


# https://leetcode.com/problems/crawler-log-folder/description/
class Solution:
    def minOperations(self, logs):
        stack=[]
        for i in logs:
            if i =='./':
                continue
            if stack and i == '../':
                stack.pop()
            elif i != './' and i != '../':
                stack.append(i)
        return len(stack)


# https://leetcode.com/problems/reorder-list/
class Solution:
    def reorderList(self, head) -> None:
        # stack=[]
        # fast,slow,current_node=head,head,head
        # while slow and slow.next:
        #     slow=slow.next
        #     if fast and fast.next:
        #         fast=fast.next.next
        #         if not fast or not fast.next:
        #             fast=None
        #             meddle=slow
        #     if slow and not fast:
        #         stack.append(slow)
        # while current_node and current_node.next and stack:
        #     popped_node=stack.pop()
        #     temp=current_node.next
        #     current_node.next=popped_node
        #     popped_node.next=temp
        #     current_node=current_node.next.next
        #     if current_node == meddle:
        #         popped_node.next.next=None
        #         break
        # return head

        if not head or not head.next:
            return 
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None  
        
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        first, second = head, prev
        
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2


# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/
class Solution:
    def finalPrices(self, prices):
        results=prices[:]
        stack=[]
        for i in range(len(prices)):
            while stack and prices[i] <= prices[stack[-1]]:
                inx=stack.pop()
                results[inx]-=prices[i]
            stack.append(i)
        return results


# https://leetcode.com/problems/implement-stack-using-queues/
class MyStack:

    def __init__(self):
        self.stack=[]

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            poped=self.stack.pop()
            return poped
        return None

    def top(self) -> int:
        if self.stack:
            poped=self.stack[-1]
            return poped
        return None

    def empty(self) -> bool:
        if self.stack:
            return False
        return True

head1=ListNode(val=1)
head1.next=ListNode(val=2)
head1.next.next=ListNode(val=3)
head1.next.next.next=ListNode(val=4)
head1.next.next.next.next=ListNode(val=5)
head1.next.next.next.next.next=ListNode(val=6)
head1.next.next.next.next.next.next=ListNode(val=7)
head1.next.next.next.next.next.next.next=ListNode(val=8)


print(Solution().finalPrices([8,10,15,2,3]))
