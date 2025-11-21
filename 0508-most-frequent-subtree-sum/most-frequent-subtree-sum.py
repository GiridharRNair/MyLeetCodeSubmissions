# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        sum_store = defaultdict(int)

        def dfs(node):
            if not node:
                return 0
            
            if not node.left and not node.right:
                sum_store[node.val] += 1
                return node.val

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            sub_tree_sum = node.val + left_sum + right_sum
            sum_store[sub_tree_sum] += 1
            return sub_tree_sum
        
        dfs(root)
        
        sum_store_keys = list(sum_store.keys())
        # print(sum_store)
        max_freq = max(sum_store.values())
        
        res = []
        for key, freq in sum_store.items():
            if freq == max_freq:
                res.append(key)

        return res



            