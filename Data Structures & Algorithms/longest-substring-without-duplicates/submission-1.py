class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        l=0
        r=0
        d={}
        m=float('-inf')
        while r<len(s):
            if s[r] not in d:
                d[s[r]]=1
            else:
                d[s[r]]+=1
            while d[s[r]]>1:
                d[s[l]]-=1
                l+=1
            m=max(m,r-l+1)
            r+=1
        return m


        