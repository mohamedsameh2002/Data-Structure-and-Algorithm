class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)
    def __repr__(self):
        return self.__str__()

#https://leetcode.com/problems/merge-two-sorted-lists/
class Solution:
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        current_node = head
        
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                current_node.next = list1
                list1 = list1.next
            else:
                current_node.next = list2
                list2 = list2.next
            
            current_node = current_node.next

        if list1 is not None:
            current_node.next = list1
        elif list2 is not None:
            current_node.next = list2
        
        return head.next  


#https://leetcode.com/problems/remove-duplicates-from-sorted-list/
class Solution:
    def deleteDuplicates(self, head):
        current_node = head
        while current_node is not None and current_node.next is not None:
            if current_node.val == current_node.next.val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next 
        return head

#https://leetcode.com/problems/linked-list-cycle/
class Solution:
    def hasCycle(self, head):
        visited_nodes = set()
        current = head
        while current:  
            if current in visited_nodes:  
                return True
            else:
                visited_nodes.add(current)  
            current = current.next
        return False


#https://leetcode.com/problems/remove-linked-list-elements/description/
class Solution:
    def removeElements(self, head, val):
        current=head
        prev=head
        while current and current.next:
            current=current.next
            if current.val == val:
                prev.next=current.next
            else:
                prev=prev.next
        if head and  head.val == val:
            head=head.next
        return head


# https://leetcode.com/problems/palindrome-linked-list/
class Solution:
    def isPalindrome(self, head):
        prev,fast,slow=None,head,head
        while fast and fast.next:
            fast=fast.next.next
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
        if fast:
            slow=slow.next
        while prev and slow:
            if prev.val !=slow.val:
                return False
            prev=prev.next
            slow=slow.next
        return True


#https://leetcode.com/problems/remove-nth-node-from-end-of-list/
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy=ListNode(0,head)
        slow, fast = dummy, dummy
        delay=0
        while fast.next:
            fast=fast.next
            delay+=1
            if delay > n:
                slow=slow.next
        if delay <= n:
            return head.next
        slow.next=slow.next.next
        return head


# https://leetcode.com/problems/partition-list/
class Solution:
    def partition(self, head, x: int) :
        start_node=ListNode(val=0)
        start_node_big=ListNode(val=0)
        small_pointer=start_node
        big_pointer=start_node_big
        while head:
            new_node=ListNode()
            if head.val >= x:
                new_node.val=head.val
                big_pointer.next=new_node
                big_pointer=new_node
            else:
                new_node.val=head.val
                small_pointer.next=new_node
                small_pointer=new_node
            head=head.next
        small_pointer.next=start_node_big.next
        return start_node.next


# https://leetcode.com/problems/add-two-numbers/
class Solution:
    def addTwoNumbers(self, l1, l2):
        curry=0
        dummy=ListNode(0)
        current=dummy
        while l1 or l2 or curry:
            new_node=ListNode()
            results=curry
            if l1:
                results+=l1.val
                l1=l1.next
            if l2:
                results+=l2.val
                l2=l2.next
# if 35
            new_node.val=int(results % 10)#5
            curry=results//10#3

            current.next=new_node
            current=new_node
        return dummy.next


# https://leetcode.com/problems/intersection-of-two-linked-lists/
class Solution:
    def getIntersectionNode(self, headA, headB) :
        l1,l2 = headA, headB
        while l1 != l2:
            l1=l1.next if l1 else headB
            l2=l2.next if l2 else headA
        return l1


head1=ListNode(val=1)
head1.next=ListNode(val=2)
head1.next.next=ListNode(val=3)
head1.next.next.next=ListNode(val=4)
head1.next.next.next.next=ListNode(val=5)
# head1.next.next.next.next.next=ListNode(val=2)
# head1.next.next.next.next.next.next=ListNode(val=7)
# head1.next.next.next.next.next.next.next=ListNode(val=8)


head2=ListNode(val=6)
head2.next=ListNode(val=7)
head2.next.next=ListNode(val=8)
head2.next.next.next=ListNode(val=9)
# head2.next.next.next.next=ListNode(val=4)
# head2.next.next.next.next.next=ListNode(val=5)



so=Solution()
print(so.getIntersectionNode(head1,head2))
# print(Solution().getIntersectionNode(head1,head2))