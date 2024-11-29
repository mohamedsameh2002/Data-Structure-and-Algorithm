# https://leetcode.com/problems/time-needed-to-buy-tickets/description/
class Solution:
    def timeRequiredToBuy(self, tickets:list, k) :
        time=0
        while k > -1 and tickets[k] > 0:
            time+=1
            if tickets[k] == 1 and k == 0:
                break
            t=tickets.pop(0)
            t-=1
            if t > 0:
                tickets.append(t)
            if k == 0 or k > (len(tickets) -1):
                k =(len(tickets) -1)
            elif k < (len(tickets) -1) or k == (len(tickets) -1):
                k-=1
        return time


# https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution:
    def firstUniqChar(self, s:str) :
        # letterst_list=list(s)
        # for _ in letterst_list:
        #     l=letterst_list.pop(0)
        #     if l not in letterst_list:
        #         return s.index(l)
        #     else:
        #         letterst_list.append(l)
        # return -1
        for i  in s:
            if s.index(i) == s.rindex(i):
                return s.index(i)
        return -1


# https://leetcode.com/problems/implement-queue-using-stacks/
class MyQueue:

    def __init__(self):
        self.q=[]

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        if self.q:
            popped=self.q.pop(0)
            return popped
        return None

    def peek(self) -> int:
        if self.q:
            popped=self.q[0]
            return popped
        return None

    def empty(self) -> bool:
        if self.q:
            return False
        return True

print(Solution().firstUniqChar('aabb'))
