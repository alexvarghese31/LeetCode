    class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=set()#to store the sum of the squares of digits of diff n 
        while n!=1:
            if n in s:#we encounter a cycle(repeating)
                return False#1 will never be formed
            s.add(n)
            #computing sum of sq of digits
            summ=0
            temp=n
            while temp>0:
                r=temp%10
                summ+=r**2
                temp=temp//10
            #new n will be the current s
            n=summ
        return True

        
