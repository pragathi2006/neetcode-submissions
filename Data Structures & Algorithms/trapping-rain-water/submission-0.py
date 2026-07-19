class Solution:
    def trap(self, height: List[int]) -> int:
        prefixmax=[0]*len(height)
        suffixmax=[0]*len(height)
        prefixmax[0]=height[0]
        suffixmax[-1]=height[-1]
        for i in range(1,len(height)):
            prefixmax[i]=max(prefixmax[i-1],height[i])
        for i in range(len(height)-2,-1,-1):
            suffixmax[i]=max(suffixmax[i+1],height[i])
        total=0    
        for i in range(len(height)):
            s=min(prefixmax[i],suffixmax[i])-height[i]
            total+=s
        return total    



        