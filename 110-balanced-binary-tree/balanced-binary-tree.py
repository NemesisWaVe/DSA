# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,node):
        if node is None:
            return (0,True)
        leftDepth,leftBalanced=self.check(node.left)
        rightDepth,rightBalanced=self.check(node.right)
        localBalance=abs(leftDepth-rightDepth)<=1
        subTreeBal=localBalance and leftBalanced and rightBalanced
        depth =1+max(leftDepth,rightDepth)
        return (depth,subTreeBal)
    def isBalanced(self, root: TreeNode | None) -> bool:
        depth,balanced=self.check(root)
        return balanced
        