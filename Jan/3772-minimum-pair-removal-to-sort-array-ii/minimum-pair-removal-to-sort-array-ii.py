class ListNode:
    def __init__(self, val = 0, nxt = None, i = 0, prev = None):
        self.val = val
        self.next = nxt
        self.prev = prev
    
    __gt__ = lambda _,__ : 0


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        
        head = ListNode(nums[0])
        cur = head
        pq = []
        wrong = set()
        for i in range(1, n):
            cur.next = ListNode(nums[i])
            heappush(pq, [cur.val + nums[i], i, cur])
            if nums[i-1] > nums[i]:
                wrong.add(cur)
            cur.next.prev, cur = cur, cur.next
        
        cur = head
        c = 0
        popped = set()
        while wrong:
            node = None
            while pq:
                sm, i, cur = heappop(pq)
                if (
                    cur not in popped and 
                    cur.next and 
                    cur.next not in popped and 
                    cur.val + cur.next.val == sm
                ):
                    node = cur
                    node.val = sm
                    break
            if not node: 
                c += 1
                break
            
            popped.add(node.next)
            
            # recompute decreasing pairs
            wrong.discard(node)
            wrong.discard(node.next)
           
            node.next = node.next.next
            if node.next:
                node.next.prev = node
                if node.val > node.next.val:
                    wrong.add(node)
                heappush(pq, [node.val + node.next.val, i, node])


            if node.prev and node.prev not in popped:
                if node.prev.val > node.val:
                    wrong.add(node.prev)
                else:
                    wrong.discard(node.prev)
                heappush(pq, [node.val + node.prev.val, i-1, node.prev])
            c += 1


        return c