# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        twin_sum = 0
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next

        n = len(arr)
        for i in range(n//2):
            twin_sum = max(twin_sum, arr[i] + arr[n-i-1])

        return twin_sum
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        