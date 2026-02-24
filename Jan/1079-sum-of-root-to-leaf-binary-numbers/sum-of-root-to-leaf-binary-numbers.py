# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.val = 0

    def method(self, root, path):
        if not root:
            return

        path.append(str(root.val))

        if not root.left and not root.right:
            self.val += int("".join(path), 2)
        else:
            self.method(root.left, path)
            self.method(root.right, path)

        path.pop()  

    def sumRootToLeaf(self, root):
        self.method(root, [])
        return self.val
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        