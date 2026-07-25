class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        r=k-1
        b=[]
        while r<len(nums):
            a=nums[l:r+1]
            b.append(max(a))
            l+=1
            r+=1
        return b    


