    class Solution:
    def longestKSubstr(self, s, k):
        l=0
        r=0
        maxlen=-1
        d={}#to store frq of char
        for r in range(len(s)):
            d[s[r]]=d.get(s[r],0)+1#++freq if dound else set it to 1
            #as long as d has>k chars; --from left
            while len(d)>k:
                d[s[l]]-=1
                if d[s[l]]==0:#means no more of left char; so delete it from d
                    del d[s[l]]
                l+=1
            if len(d)==k:
                maxlen=max(maxlen,r-l+1)
        return maxlen
            
        
        
