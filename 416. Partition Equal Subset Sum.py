def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #if the list sum is odd, it can never be divided across 2 sublists
        if sum(nums)%2!=0:
            return False
        
        #setting the target which divides our list into 2 equal list
        target=sum(nums)//2
        #set to avoid duplucations
        dp=set()
        dp.add(0)

        #dp
        """we add the the new number i with each j in dp already and see if they
        achieve targt"""
        for i in nums:
            new_dp=set(dp)
            for j in dp:
                if j+i==target:
                    return True
                if j+i<target:
                    new_dp.add(i+j)
            dp=new_dp
        return False
