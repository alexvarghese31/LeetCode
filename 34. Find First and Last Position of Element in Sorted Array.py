def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #fn to help find the leftmost occurrence of target
        def findleft(nums,target):
            l=0
            r=len(nums)-1
            index=-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    index=mid
                    #keep checking for an occurrence toward left, ie drift left
                    r=mid-1
                elif target<=nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            return index

        #fn to help find the leftmost occurrence of target
        def findright(nums,target):
            l=0
            r=len(nums)-1
            index=-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    index=mid
                    #keep checking for an occurrence toward right, ie drift right
                    l=mid+1
                elif target<=nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            return index

        return [findleft(nums,target),findright(nums,target)]
