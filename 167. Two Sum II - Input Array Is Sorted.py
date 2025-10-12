        l=0
        r=len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]==target:
                return [l+1,r+1] #because it is '1' based indexing
            elif numbers[l]+numbers[r]>target:
                r-=1
            else:
                l+=1
