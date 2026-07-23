class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        d={}
        maxfreq=0
        length=0
        while r<len(s):
            if s[r] not in d:
                d[s[r]]=1
            else:
                d[s[r]]+=1
            maxfreq=max(maxfreq,d[s[r]])    
            while ((r-l+1)-maxfreq)>k:
                d[s[l]]-=1
                l+=1
            length=max(length,r-l+1)
            r+=1
        return length        



        