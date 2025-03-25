# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dia = 0
        def d(node, dia):
            if not node:
                return 0
            
            left = d(node.left, dia)
            right = d(node.right, dia)

            self.max_dia = max(self.max_dia, left + right)

            return max(left, right) + 1
        d(root, 0)
        return self.max_dia

