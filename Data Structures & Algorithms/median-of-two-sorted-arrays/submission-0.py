class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=[]
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                nums.append(nums1[i])
                i+=1
            else:
                nums.append(nums2[j])
                j+=1
        while i<len(nums1):
            nums.append(nums1[i])
            i+=1
        while j<len(nums2):
            nums.append(nums2[j])
            j+=1

        low=0
        high=len(nums)-1
        mid=(low+high)//2
        if len(nums)&1==1:
            return float(nums[mid])
        else:
            return (nums[mid]+nums[mid+1])/2                     

