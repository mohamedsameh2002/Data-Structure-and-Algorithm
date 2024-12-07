class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)
    def __repr__(self):
        return self.__str__()

# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums=sorted(nums)
        d={}
        for i,num in enumerate(sorted_nums):
            if num not in d:
                d[num]=i
        res=[]
        for i in nums:
            res.append(d[i])
        return res


# https://leetcode.com/problems/sort-list/
class Solution:
    def merge(self,left,right):
        dummy=ListNode()
        tail=dummy
        while left and right:
            if left.val < right.val:
                tail.next=left
                left=left.next
            else:
                tail.next=right
                right=right.next
            tail=tail.next
        if left:
            tail.next=left
        if right:
            tail.next=right
        return dummy.next
    
    def sortList(self, head):
        if not head or not head.next:
            return head
        prev=None
        fast,slow=head,head
        while fast and fast.next:
            prev=slow
            fast=fast.next.next
            slow=slow.next
        prev.next=None
        left=self.sortList(head)
        right=self.sortList(slow)
        return self.merge(left,right)




head1=ListNode(val=-1)
head1.next=ListNode(val=5)
# head1.next.next=ListNode(val=3)
# head1.next.next.next=ListNode(val=4)
# head1.next.next.next.next=ListNode(val=0)
# head1.next.next.next.next.next=ListNode(val=2)
# head1.next.next.next.next.next.next=ListNode(val=7)
# head1.next.next.next.next.next.next.next=ListNode(val=8)

so=Solution()
print(so.sortList(head1))