# https://leetcode.com/problems/swap-nodes-in-pairs/
class Solution:
    def swapPairs(self, head):
        if head:
            if not head.next:
                return head
            one=head
            tow=head.next
            upcome_one=head.next.next
            tow.next=one
            one.next=self.swapPairs(upcome_one)
            return tow
