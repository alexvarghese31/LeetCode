class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i=0 #to keep track of each new char
        k=0 #ptr to edit in the array
        while i<len(chars):
            j=i #ptr to move untill char[i] mismatches
            while j<len(chars) and chars[j]==chars[i]:
                j+=1 #match found, therefore ++
            #mismatch
            chars[k]=chars[i] 
            k+=1
            count=j-i
            if count>1:
                for i in str(count):
                    chars[k]=i
                    k+=1
            i=j
        return k
