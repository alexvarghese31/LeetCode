class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        l=0
        d={}
        while l+10<=len(s): #Loop will work till the last 10 length DNA
            d[s[l:l+10]]=d.get(s[l:l+10],0)+1
            l+=1

        res=[]
        for i in d:
            if d[i]>1: #All those DNA having count more than 1
                res.append(i)
        
        return res
