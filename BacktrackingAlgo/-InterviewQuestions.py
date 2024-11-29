# https://leetcode.com/problems/subsets/
class Solution:
    def subsets(self, nums) :
        res=[]
        subset=[]
        def dfs(current):
            if current == len(nums):
                res.append(subset[:])
                return
            subset.append(nums[current])
            #in order traversal
            dfs(current+1)
            subset.pop()
            dfs(current+1)
        dfs(0)
        return res


#https://leetcode.com/problems/binary-watch/
class Solution:
    def readBinaryWatch(self, turnedOn) :
        hours=[8,4,2,1,0]
        minutes=[32,16,8,4,2,1,0]


"""
base caste = when we arreved at the input numper
"""





so=Solution()
print(bin(30))
