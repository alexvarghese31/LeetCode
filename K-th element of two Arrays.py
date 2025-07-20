#User function Template for python3


class Solution:

    def kthElement(self, a, b, k):
        n=len(a)
        m=len(b)
        arr=[0]*(m+n)
        i=0
        j=0
        t=0
        while i<n and j<m:
            if a[i]<=b[j]:
                arr[t]=a[i]
                i+=1
            else:
                arr[t]=b[j]
                j+=1
            t+=1
        while i<n:
            arr[t]=a[i]
            i+=1
            t+=1
        while j<m:
            arr[t]=b[j]
            j+=1
            t+=1
        return arr[k-1]
                
        pass
