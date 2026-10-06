# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        if not root:
            return 0

        stack =[root]
        prev = None

        while stack:
            curr = stack.pop()
            if prev:
                prev.left = None
                prev.right = curr
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
            
            prev = curr
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        