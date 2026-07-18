class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]*len(nums)
        n=1
        for i in range(len(nums)):
            prefix[i]=n
            n=n*nums[i]

        suffix=[1]*len(nums)
        p=1
        for i in range(len(nums)-1,-1,-1):
            suffix[i]=p
            p=p*nums[i]
        a=[]
        for i in range(len(nums)):
            a.append(suffix[i]*prefix[i])
        return a

        
        
           

        