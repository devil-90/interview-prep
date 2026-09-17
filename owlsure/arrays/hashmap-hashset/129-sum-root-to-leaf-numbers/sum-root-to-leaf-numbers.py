# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def dfs(root, count):
            if root is None:
                return 0
            count = count*10 + root.val
            if root.left is None and root.right is None:
                return count

            left_count = dfs(root.left, count)
            right_count = dfs(root.right, count)
            return left_count+right_count
        
        return dfs(root, 0)
        