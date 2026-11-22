class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        output=[]
        for i in range(len(strs)):
            if ''.join(sorted(strs[i])) not in d:
                d[''.join(sorted(strs[i]))]=[strs[i]]
            else:
                d[''.join(sorted(strs[i]))].append(strs[i])
        for j in d.values():
            output.append(j)   
        return output         
       

        

         
        