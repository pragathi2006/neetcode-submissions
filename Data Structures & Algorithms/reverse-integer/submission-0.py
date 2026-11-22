class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            sign=1
        else:
            sign=-1
        x=abs(x)
        a=str(x)
        b=list(a)
        c=b[::-1]
        d=''.join(c)
        e=int(d)
        if sign*e>=-2**31 and sign*e<=2**31-1:
            return sign*e
        else:
            return 0           
        