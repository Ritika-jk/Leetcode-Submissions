# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):

        curr_lvl = 1
        maxi = float('-inf')
        ans = 1

        queue = deque([root])

        while queue:
            curr_sum = 0
            lvl_size = len(queue)

            for _ in range(lvl_size):
                node = queue.popleft()
                curr_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if curr_sum > maxi:
                maxi = curr_sum
                ans = curr_lvl

            curr_lvl += 1
        
        return ans
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        