class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):

        import math
        def func(guess,copy_height):
            '''
1. iterate over all workers in the workerTimes list.
2. For each worker with time t, compute the maximum number of height units (k) the worker can remove within the guessed time.
3. Solving this inequality using the quadratic formula allows us to directly compute k
4. The value k represents the maximum number of iterations (height reductions) that the worker can complete within the guessed time.
5. Subtract this value from the remaining copy_height.
6. After processing all workers:
    a. If the remaining height becomes less than or equal to zero, it means the workers can collectively reduce the mountain within the guessed time, so we return True.

    b. Otherwise, the guessed time is insufficient, and we return False.
            '''
            for i in workerTimes:
                x = (2*guess)//i
                k = (-1 + math.sqrt(1 + (4*x))) // 2 

                copy_height -= k
            
            if copy_height <= 0:
                return True
            else:
                return False

        low = 1 
        high = min(workerTimes) * (((mountainHeight) * ((mountainHeight)+1))//2)
        ans = float('inf')
        while low <= high:
            mid = (low+high) // 2
            if func(mid,mountainHeight):
                high = mid - 1 
                ans = min(ans,mid)
            else:
                low = mid + 1
        
        return ans
        """
        :type mountainHeight: int
        :type workerTimes: List[int]
        :rtype: int
        """
        