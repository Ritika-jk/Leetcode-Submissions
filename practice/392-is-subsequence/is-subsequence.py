class Solution(object):
    def isSubsequence(self, s, t):
        
        s= list(s)
        i=0
        for j in t:
            if i<len(s) and j==s[i]:
                i+=1
        if i== len(s):
            return True
        return False 
        if len(s)==0:
            return True
        
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        