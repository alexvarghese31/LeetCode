def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d={}
        stack=[] #monotonic stack
        for i in nums2:
            #if stack nont empty and i>stacks top
            while stack and i>stack[-1]:
                smaller=stack.pop()
                d[smaller]=i #d[1]=3; {1:3...}
            #now 3 will be ie i the top of the stack
            stack.append(i)
        #assigns -1 to all those i's in stac which didnot satisfy
        for i in stack:
            d[i]=-1
        res=[]
        #res in the order of num1
        for i in nums1:
            res.append(d[i])
        return res
