# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDepth(self, node):
        if node is None:
            return 0
        return 1 + max(self.getDepth(node.left), self.getDepth(node.right))

    def subtreeWithAllDeepest(self, root):
        if root is None:
            return None

        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)

        if leftDepth == rightDepth:
            return root
        elif rightDepth > leftDepth:
            return self.subtreeWithAllDeepest(root.right)
        else:
            return self.subtreeWithAllDeepest(root.left)
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        