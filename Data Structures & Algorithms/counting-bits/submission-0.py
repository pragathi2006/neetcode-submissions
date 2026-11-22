class Solution:
    def countBits(self, n: int) -> List[int]:
        s=[0]
        for i in range(1,n+1):
            a=bin(i)[2:]
            s.append(a.count('1'))
        return s    


        