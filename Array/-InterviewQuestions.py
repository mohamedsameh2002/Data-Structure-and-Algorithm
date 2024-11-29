# https://leetcode.com/problems/maximum-average-subarray-i/
class Solution:
    def findMaxAverage(self, nums:int, k: int):
        fast=0
        slow=0
        sum=0
        res=0
        for _ in range(len(nums)):
            sum+=nums[fast]
            fast+=1
            if fast >= k:
                if res < sum or res == 0:
                    res=sum
                sum-=nums[slow]
                slow+=1
        return res/k



so=Solution()
print(so.findMaxAverage([1,12,-5,-6,50,3],5))

