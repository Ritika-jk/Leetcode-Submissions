class Solution(object):
    def canReach(self, s, minJump, maxJump):
        n = len(s)

        if s[-1] == '1':
            return False

        dp = [False] * n
        dp[0] = True

        reach = 0

        for i in range(1, n):

            if i >= minJump:
                reach += dp[i - minJump]

            if i > maxJump:
                reach -= dp[i - maxJump - 1]

            if reach > 0 and s[i] == '0':
                dp[i] = True

        return dp[-1]
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        