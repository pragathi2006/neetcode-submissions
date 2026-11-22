class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1    
        l=0
        r=0
        d={}
        count=0
        while r<len(s):
            if s[r] not in d:
                d[s[r]]=1
            else:
                d[s[r]]+=1
            while d[s[r]]>1:
                d[s[l]]-=1
                if d[s[l]]==0:
                    del d[s[l]]
                l+=1
            count=max(count,(r-l)+1)
            r+=1
        return count        



        


        