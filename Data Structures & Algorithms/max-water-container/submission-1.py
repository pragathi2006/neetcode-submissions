class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        a=0
        area=1
        while i<j:
            area=min(heights[i],heights[j])*(j-i)
            a=max(area,a)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return a            
            

                 
           

            