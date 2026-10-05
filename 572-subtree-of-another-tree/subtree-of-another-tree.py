# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMatching(self,p:TreeNode | None,q:TreeNode | None):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        valMatch=p.val==q.val
        leftMatch=self.isMatching(p.left,q.left)
        rightMatch=self.isMatching(p.right,q.right)
        return valMatch and leftMatch and rightMatch
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if root is None:
            return False
        curr=self.isMatching(root,subRoot)
        left=self.isSubtree(root.left,subRoot)
        right=self.isSubtree(root.right,subRoot)
        return curr or left or right
