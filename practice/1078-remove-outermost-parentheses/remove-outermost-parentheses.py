class Solution(object):
    def removeOuterParentheses(self, s):
        ans = []
        count = 0

        for c in s:
            if c == '(':
                if count > 0:
                    ans.append(c)
                count += 1
            else:
                count -= 1
                if count > 0:
                    ans.append(c)

        return "".join(ans)
        
        """
        :type s: str
        :rtype: str
        """
        