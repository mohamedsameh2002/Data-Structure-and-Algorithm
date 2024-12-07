from collections import defaultdict
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


# https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        n = len(nums)
        return nums[n//2]


so=Solution()
print(so.majorityElement([2,2,1,1,1,2,2]))

