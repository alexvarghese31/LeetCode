class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        #Edge Cases
        if sum(nums)<target:
            return 0
        if sum(nums)==target:
            return len(nums)

        l=0
        minlen=float('inf') #Set minlen to a large value at first
        curr=0
        for r in range(len(nums)):
            curr+=nums[r]
            #As long as curr>=target; compute the new subarray len
            while curr>=target:
                minlen=min(minlen,r-l+1)
                #Start shrinking from left till the while loop persists
                curr-=nums[l]
                l+=1
        return minlen
