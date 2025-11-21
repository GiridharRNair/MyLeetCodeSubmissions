# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        path_sum = 0
        path = []
        res = []
        def dfs(node):
            nonlocal path, res, path_sum
            if not node:
                return

            if not node.left and not node.right:
                if path_sum + node.val == targetSum:
                    res.append(path + [node.val])
                    return

            path.append(node.val)
            path_sum += node.val

            dfs(node.left)
            dfs(node.right)

            path.pop()
            path_sum -= node.val

        dfs(root)
        return res

                