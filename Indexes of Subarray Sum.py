#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        l=0
        r=0
        n=len(arr)
        summ=0
        while r<n:
            summ+=arr[r]
            while summ>target and l<=r:
                    summ-=arr[l]
                    l+=1#shrink the window
            if summ==target:
                return [l+1,r+1]#1 based indexing
            r+=1
        return [-1] 
