class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a=set(nums)
        b=0
        for i in a:
            count=1
            if i-1 not in a:
                current=i
            else:
                continue    
            while current+1 in a:
                count+=1
                current+=1
            b=max(b,count)
        return b    




        