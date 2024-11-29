from collections import defaultdict
# https://leetcode.com/problems/find-center-of-star-graph/
class Solution:
    def findCenter(self, edges):
        if edges[0][0] in edges[1] :
            return edges[0][0]
        else:
            return edges[0][1]



so=Solution()
print(so.findCenter([[1,2],[2,3],[4,2]]))
