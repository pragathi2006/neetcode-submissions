class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        sorted_d=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
        i=0
        a=[]
        for key in sorted_d.keys():
            if i<k:
                a.append(key)
                i+=1
            else:
                break
        return a            

            





        