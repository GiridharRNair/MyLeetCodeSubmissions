# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        def get_height(root):
            if not root:
                return 0

            left_height = get_height(root.left)
            right_height = get_height(root.right)

            if right_height < 0 or left_height < 0 or abs(right_height - left_height) > 1:
                return -1

            return max(left_height, right_height) + 1

        return get_height(root) > -1