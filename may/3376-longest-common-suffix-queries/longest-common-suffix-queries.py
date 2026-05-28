class Node:
    def __init__(self):
        self.arr=dict()
        self.ob=-1
        self.mini=float('inf')

class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        trie=Node()
        def insert(i,word):
            temp=trie
            new=len(word)
            if temp.mini>new:
                temp.ob=i
                temp.mini=new
            for w in word:
                ind=ord(w)-ord('a')
                if ind not in temp.arr:
                    temp.arr[ind]=Node()
                temp=temp.arr[ind]
                if new<temp.mini:
                    temp.mini=new
                    temp.ob=i
        
        def find(suf):
            temp=trie
            for w in suf:
                ind=ord(w)-ord('a')
                if ind not in temp.arr:
                    break
                temp=temp.arr[ind]
            return temp.ob

        for i in range(len(wordsContainer)):
            insert(i,wordsContainer[i][::-1])

        res=[]
        for word in wordsQuery:
            res.append(find(word[::-1]))

        return res

        """
        :type wordsContainer: List[str]
        :type wordsQuery: List[str]
        :rtype: List[int]
        """
        