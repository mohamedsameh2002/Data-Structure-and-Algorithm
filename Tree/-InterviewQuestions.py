class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)
    def __repr__(self):
        return self.__str__()


# https://leetcode.com/problems/binary-tree-inorder-traversal/
class Solution:
    def inorderTraversal(self, root):
        if root:
            stack=[]
            stack.extend(self.inorderTraversal(root.left))
            stack.append(root.val)
            stack.extend(self.inorderTraversal(root.right))
            return stack
        return []


# https://leetcode.com/problems/same-tree/
class Solution:
    def isSameTree(self, p, q):
        if not q and not p:
            return True
        if not q or not p:
            return False
        if q.val != p.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)


# https://leetcode.com/problems/binary-tree-paths/
class Solution:
    def binaryTreePaths(self, root) :
        all_paths = []
        backtracking = []
        def dfs_pre(root):
            if not root:
                return
            backtracking.append(str(root.val))
            if not root.left and not root.right:
                all_paths.append('->'.join(backtracking))
            
            dfs_pre(root.left)
            dfs_pre(root.right)
            
            backtracking.pop()
        dfs_pre(root)
        return all_paths


# https://leetcode.com/problems/subtree-of-another-tree/
class Solution:
    def isSubtree(self, root, subRoot) :

        def isSameTree(tree1,tree2):
            if not tree1 and not tree2:
                return True
            if not tree1 or not tree2:
                return False
            if tree1.val != tree2.val:
                return False
            left_bransh=isSameTree(tree1.left,tree2.left)
            right_bransh=isSameTree(tree1.right,tree2.right)
            return left_bransh and right_bransh
        
        if not root:
            return False
        
        if isSameTree(root,subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)


# https://leetcode.com/problems/diameter-of-binary-tree/
class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter=0
        def get_hight(node):
            if not node:return 0
            left=get_hight(node.left)
            right=get_hight(node.right)
            self.diameter = max(self.diameter, left + right)
            return 1+ max(left,right)
        get_hight(root)
        return self.diameter


# https://leetcode.com/problems/symmetric-tree/
class Solution:
    def isSymmetric(self, root) :
        if not root:
            return True
        def symmetric_dfs(left,right):
            if not left and not right:
                return True
            if (not left or not right) or left.val != right.val:
                return False
            return symmetric_dfs(left.left,right.right) and symmetric_dfs(left.right,right.left)
        return symmetric_dfs(root.left,root.right)


# https://leetcode.com/problems/maximum-depth-of-binary-tree/
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)
        return 1 +max(left,right)






# root=TreeNode(val=1)
# node_2=TreeNode(val=2)
# node_3=TreeNode(val=3)
# node_4=TreeNode(val=4)
# node_5=TreeNode(val=5)
# node_6=TreeNode(val=6)
# node_7=TreeNode(val=7)
# node_8=TreeNode(val=8)
# node_2j=TreeNode(val=2)
# node_3j=TreeNode(val=3)
# node_4j=TreeNode(val=4)
# node_5j=TreeNode(val=5)
# node_6j=TreeNode(val=6)
# node_7j=TreeNode(val=7)
# node_8j=TreeNode(val=8)
# root.left=node_2
# node_2.left=node_3
# node_3.left=node_5
# node_3.right=node_6
# node_2.right=node_4
# node_4.left=node_7
# node_4.right=node_8
# root.right=node_2j
# node_2j.left=node_4j
# node_4j.left=node_8j
# node_4j.right=node_7j
# node_2j.right=node_3j
# node_3j.left=node_6j
# node_3j.right=node_5j



root=TreeNode(val=1)
node_2=TreeNode(val=2)
node_3=TreeNode(val=3)
node_4=TreeNode(val=4)
node_5=TreeNode(val=5)
node_6=TreeNode(val=6)
node_7=TreeNode(val=7)
node_8=TreeNode(val=8)
node_9=TreeNode(val=9)

root.left=node_2
root.right=node_3
node_2.left=node_4
node_2.right=node_5
node_3.right=node_8
node_5.left=node_6
node_5.right=node_7
node_8.left=node_9


so=Solution()
print(so.maxDepth(root))




















