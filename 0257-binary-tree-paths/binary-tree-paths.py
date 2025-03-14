# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        out = []
        
        def search(node, path):
            if not node:
                return

            path += str(node.val)

            if not node.right and not node.left:
                out.append(path)
                return
            

            search(node.right, path+"->")
        
            search(node.left, path+"->")

        search(root, "")
        return out
        