class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=[]
        c=[]
        for i in range(len(strs)):
            a.append("".join(sorted(strs[i])))
        d={}
        for i in range(len(a)):
            if a[i] not in d:
                d[a[i]]=[i]
            else:
                d[a[i]].append(i)
        for key,value in d.items():
            b=[]
            for item in value:
                b.append(strs[item])
            c.append(b)
        return c    

                           
        

         
        