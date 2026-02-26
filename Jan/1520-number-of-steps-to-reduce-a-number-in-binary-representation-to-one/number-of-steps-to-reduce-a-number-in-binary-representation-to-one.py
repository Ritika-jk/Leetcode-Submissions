class Solution(object):
    def numSteps(self, s):
        s = int(s,2)
        steps = 0
        while True:
            if s == 1:
                break
            elif s%2 == 0:
                s = s/2
                steps +=1
            elif s%2 ==1:
                s +=1
                steps+=1
        return steps
        """
        :type s: str
        :rtype: int
        """
        