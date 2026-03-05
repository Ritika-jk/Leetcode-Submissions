class Solution(object):
    def minOperations(self, s):
        n = len(s)
        part1 = []
        part2 =[]
        one = False
        for _ in range (n):
            if one :
                part1.append('1')
            else:
                part1.append('0')
            one = not one 
        one = True 
        for _ in range (n):
            if one:
                part2.append ('1')
            else :
                part2.append('0')
            one = not one 

        count1 = 0
        count2 = 0
        for i in range(n):
            if s[i] != part1[i]:
                count1 +=1
            if s[i] != part2[i]:
                count2 +=1
        return min(count1, count2)
        """
        :type s: str
        :rtype: int
        """
        