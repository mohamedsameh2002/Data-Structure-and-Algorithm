class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return None
        seen = set()
        dummy = ListNode(-1)
        dummy.next = head
        prev_node = dummy
        current_node = head
        while current_node:
            if current_node.val in seen:
                prev_node.next = current_node.next
                current_node = current_node.next
            else:
                seen.add(current_node.val)
                prev_node = current_node
                current_node = current_node.next
        return dummy.next
    
    def removeElements(self, head, val):
        if not head:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        prev_node = dummy
        while head:
            if head.val == val:
                prev_node.next = head.next 
            else:
                prev_node=head
            head=head.next
        
        return dummy.next
    



    


node1 = ListNode(1)
node2 = ListNode(6)
node3 = ListNode(2)
node5 = ListNode(6)
node4 = ListNode(3)
node6 = ListNode(10)
node7 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
head = node1

solution = Solution()

new_head = solution.removeElements(head,6)


# current_node = new_head
# while current_node:
#     print(current_node.val, end=' -> ' if current_node.next else '')
#     current_node = current_node.next



#!------------------------------------------------------------------


# https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1, m, nums2, n)  :
        nums1[m:]=nums2
        for i in range(len(nums1)):
            main_vule=i
            for j in range(i+1,len(nums1)):
                if nums1[main_vule] > nums1[j]:
                    main_vule=j
            nums1[main_vule],nums1[i]=nums1[i],nums1[main_vule]
        return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3


#!------------------------------------------------------------------

# https://leetcode.com/problems/single-number/


def single_num(nums:list):
    res=[]
    for _ in range(len(nums)):
        current=nums.pop(0)
        if current not in array and current not in res:
            return current
        res.append(current)
    return False

array=[9,2,8,7,7,9,1,5,4,3,2,1,4,6,9,9,8,8,7,6,4,3,2,1]

