class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j=len(nums)-1
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=[i]
            else:
                d[nums[i]].append(i)   
        nums.sort()
        i=0
        while i<j:
            if nums[i]+nums[j]==target:
                if nums[i]==nums[j]:
                    return sorted(d[nums[i]][:2])
                return sorted([d[nums[i]][0],d[nums[j]][0]])
            elif nums[i]+nums[j]>target:
                j-=1
            else:
                i+=1


               
                
                    



        
        