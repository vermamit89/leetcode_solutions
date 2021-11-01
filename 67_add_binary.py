class Solution:
    def addBinary(self, a: str, b: str) -> str:                             
        deci_a=0
        deci_b=0
        for i in range(1,len(a)+1):
            deci_a+=int(a[-i])*(2**(i-1))
        for j in range(1,len(b)+1):
            deci_b+=int(b[-j])*(2**(j-1))
        deci=deci_a+deci_b
        bnr=''
        while int(deci)>1:
            q=str(int(deci)//2)
            bnr=bnr + str(int(deci)%2)
            deci=q
        bnr=bnr+str(deci)
        bnr=bnr[::-1]
        return bnr   
s=Solution()
print(s.addBinary('11001','1100'))
