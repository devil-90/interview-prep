# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root==None:
            return True
        
        def check(t1, t2):
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            outer_match = check(t1.left, t2.right)
            inner_match = check(t1.right, t2.left)
            return outer_match and inner_match
            
        return check(root.left, root.right)