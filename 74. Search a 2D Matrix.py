def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m=len(matrix)
        n=len(matrix[0])
        l=0
        h=m*n-1 #treat matrix as a long flattened array
        while l<=h:
            mid=(l+h)//2
            #2 imp steps
            r=mid//n
            c=mid%n
            if matrix[r][c]==target:
                return True
            elif target<matrix[r][c]:
                h=mid-1
            else:
                l=mid+1
        return False
     
