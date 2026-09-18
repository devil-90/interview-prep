# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        min_val = float("-inf")
        max_val = float("inf")

        def check(root, min_val, max_val):
            if root is None:
                return True
            if not min_val< root.val < max_val:
                return False
            
            left_check = check(root.left, min_val, root.val)
            right_check = check(root.right, root.val, max_val)
            return left_check and right_check
        return check(root, min_val, max_val)


        