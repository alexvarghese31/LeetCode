        n=len(temperatures)
        res=[0]*n
        stack=[]
        for i in range(n):
            #while stack not empty and ith day has higher temp than top of stack
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev_index=stack.pop()#the index of the day which we need to assign a value
                res[prev_index]=i-prev_index#current ith day - the day whose value has to be assigned
            stack.append(i)#if cooler or stack empty this will be in action
        return res
