from collections import deque

class Solution:
    def canReach(self, arr, start):
        if arr[start] == 0:
            return True

        q = deque([start])
        visited = [False] * len(arr)
        visited[start] = True

        while q:
            u = q.popleft()

            if arr[u] == 0:
                return True

            left = u - arr[u]
            right = u + arr[u]

            if left >= 0 and not visited[left]:
                visited[left] = True
                q.append(left)

            if right < len(arr) and not visited[right]:
                visited[right] = True
                q.append(right)

        return False