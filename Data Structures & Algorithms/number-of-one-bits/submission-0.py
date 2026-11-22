class Solution:
    def hammingWeight(self, n: int) -> int:
        a=bin(n)[2:]
        count=0
        for i in range(len(a)):
            if a[i]=='1':
                count+=1
        return count        

        