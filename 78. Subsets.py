class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def fun(i,ds):
            if i==len(nums):
                res.append(list(ds))
                return
            ds.append(nums[i])
            fun(i+1,ds)
            ds.pop()
            fun(i+1,ds)

        res=[]
        ds=[]
        fun(0,ds)
        return res
        
