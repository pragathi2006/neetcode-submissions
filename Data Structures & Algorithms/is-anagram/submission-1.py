class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d1={}
        d2={}
        for i in range(len(s)):
            if s[i] not in d1:
                d1[s[i]]=1
            else:
                d1[s[i]]+=1
        for i in range(len(t)):
            if t[i] not in d2:
                d2[t[i]]=1
            else:
                d2[t[i]]+=1
        sorted_d1=dict(sorted(d1.items()))
        sorted_d2=dict(sorted(d2.items()))
        if sorted_d1.keys() != sorted_d2.keys():
            return False
        for i in sorted_d1.keys():
            if sorted_d1[i]!=sorted_d2[i]:
                return False
        return True                                 


       