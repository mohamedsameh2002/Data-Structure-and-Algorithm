# https://leetcode.com/problems/find-mode-in-binary-search-tree/?envType=problem-list-v2&envId=binary-search-tree

from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def __init__(self):
        self.dict = {}
        self.ans=[]
        self.mx=-1
    def solve (self,root):
        if root is None: return
        self.dict[root.val] = self.dict.get(root.val, 0) + 1
        if self.dict[root.val]==self.mx:
            self.ans.append(root.val)
        elif self.dict[root.val]>self.mx:
            self.mx=self.dict[root.val]
            self.ans=[]
            self.ans.append(root.val)

        self.solve(root.left)
        self.solve(root.right)
    def findMode(self, root):
        
        self.solve(root)
        return self.ans





class Solution:
    def findMode(self, root):
        if not root:
            return []

        # قاموس لتتبع تكرارات القيم
        count = defaultdict(int)

        # دالة داخلية لتمرير الشجرة وتسجيل التكرارات
        def inorder(node):
            if not node:
                return
            count[node.val] += 1
            inorder(node.left)
            inorder(node.right)

        # استدعاء دالة التمرير
        inorder(root)

        # إيجاد أعلى تكرار
        max_count = max(count.values())

        # جمع جميع القيم التي لها نفس أعلى تكرار
        modes = [key for key, value in count.items() if value == max_count]

        return modes
        