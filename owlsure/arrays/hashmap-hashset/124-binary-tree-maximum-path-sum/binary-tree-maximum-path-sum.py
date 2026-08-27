# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def path(self, root):
        if root==None: return 0
        left_path_sum = self.path(root.left)
        if left_path_sum<0: left_path_sum = 0
        right_path_sum = self.path(root.right)
        if right_path_sum<0: right_path_sum=0
        x = root.val + left_path_sum + right_path_sum
        self.ans = max(self.ans, x)
        return root.val + max(left_path_sum, right_path_sum)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')
        self.path(root)
        return self.ans
        