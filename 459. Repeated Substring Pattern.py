class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=(s+s)[1:-1] #concatinate s with itself and remove the 1st and the last chars
        return s in st #this will always give the ans
