# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def compare(left_side, right_side):
            if not left_side and not right_side:
                return True
            
            if not left_side  or not  right_side:
                return False
            if left_side.val != right_side.val:
                return False
            return compare(left_side.left,right_side.right) and compare(left_side.right, right_side.left)
            
        return  compare(root.left,root.right)