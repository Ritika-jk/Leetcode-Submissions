# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSubtreeMin(self, node):
        while node is not None and node.left is not None:
            node = node.left
        return node

    def deleteNode(self, root, key):
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Case 1: Node has no children (leaf node)
            if root.left is None and root.right is None:
                return None
            # Case 2A: Node has only right child
            elif root.left is None:
                return root.right
            # Case 2B: Node has only left child
            elif root.right is None:
                return root.left
            # Case 3: Node has both children
            else:
                successor = self.findSubtreeMin(root.right)
                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)
        
        return root
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        