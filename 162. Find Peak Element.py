def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        h=len(nums)-1
        while l<h:
            mid=(l+h)//2
            if nums[mid]<nums[mid+1]:
                #peak can realistically only occur on the right side of mid
                l=mid+1
            else:
                #it can occur till mid from the left side
                h=mid
        return l
