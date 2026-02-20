class Solution(object):
    def makeLargestSpecial(self, s):

        count =0 
        start =0 
        re=[]
        for i , ch in enumerate (s):
            if ch =='1':
                count += 1
            else :
                count -=1
            if count ==0:
                inner = self.makeLargestSpecial(s[start+1:i])
                re.append("1"+ inner +"0")
                start =i+1
        re.sort(reverse= True)
        return "". join(re)


        """
        :type s: str
        :rtype: str
        """
        