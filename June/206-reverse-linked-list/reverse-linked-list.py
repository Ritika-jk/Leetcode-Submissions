# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):

        # if head is None or head.next is None:
        #     return head
        
        # # Recursively reverse the rest of the list
        # new_head = self.reverseList(head.next)
        
        # # Reverse the current node's pointer
        # head.next.next = head
        # head.next = None
        
        # return new_head

        # a=[]
        # temp = head
        # while temp is not None:
        #     a.append(temp.val)
        #     temp = temp.next
        # temp = head
        # i = len(a)-1
        # while temp is not None:
        #     temp.val = a[i]
        #     i-=1


        #     temp=temp.next
        # return head

        prev = None
        curr = head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev



        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        