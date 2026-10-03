# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        return 1+max(self.depth(root.left),self.depth(root.right))
    def isBalanced(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        diff=self.depth(root.left)-self.depth(root.right)
        if diff>1 or diff<-1:
            return False
        else: return self.isBalanced(root.left) and self.isBalanced(root.right)