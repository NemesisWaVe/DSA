# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        valuesMatch=p.val==q.val
        leftMatch=self.isSameTree(p.left,q.left)
        rightMatch=self.isSameTree(p.right,q.right)
        return valuesMatch and leftMatch and rightMatch
        