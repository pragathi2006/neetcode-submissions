class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        sorted_dict=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
        a=[]
        for key,value in sorted_dict.items():
            a.append(key)
            if len(a)==k:
                return a
            
            





        