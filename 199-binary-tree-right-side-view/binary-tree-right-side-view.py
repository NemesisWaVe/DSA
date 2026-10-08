# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        queue=deque([root])
        rightSide=[]
        while queue:
            level=[]
            size=len(queue)
            for i in range(size):
                node=queue.popleft()
                if i==size-1:
                    rightSide.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return rightSide
