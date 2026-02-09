# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        nodes = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)         # ⬅️ Left
            nodes.append(node.val)     # ⬆️ Root
            inorder(node.right)        # ➡️ Right

        def build(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            node = TreeNode(nodes[mid])        # ⬆️ Mid becomes root
            node.left = build(start, mid - 1)   # ⬅️ Build left
            node.right = build(mid + 1, end)    # ➡️ Build right
            return node

        inorder(root)
        return build(0, len(nodes) - 1)
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        