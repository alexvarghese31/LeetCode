class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def fun(ds,freq):
            if len(ds)==len(nums):
                res.append(list(ds))
                return
            for i in range(len(nums)):
                if not freq[i]:
                    #take
                    freq[i]=True
                    ds.append(nums[i])
                    fun(ds,freq)
                    #not take
                    ds.pop()
                    freq[i]=False

        res=[]
        ds=[]
        freq=[False]*len(nums)
        fun(ds,freq)
        return res

        
