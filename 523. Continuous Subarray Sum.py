        rem_map={0:-1}#to store rem at every index(tht no)
        summ=0
        for i,num in enumerate(nums):
            summ+=num
            if k!=0:#k is not 0
                summ=summ%k#rem needed from her to satisfy the condition
            if summ in rem_map:
                if i-rem_map[summ]>=2:#chck for lenght
                    return True
            else:
                rem_map[summ]=i
        return False
