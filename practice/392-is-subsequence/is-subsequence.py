class Solution(object):
    def isSubsequence(self, s, t):
        if len(s)==0:
            return True
        s= list(s)
        i=0
        for j in t:
            if i<len(s) and j==s[i]:
                i+=1
        if i== len(s):
            return True
        return False 

        
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        