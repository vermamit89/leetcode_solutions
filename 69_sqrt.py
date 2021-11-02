class Solution:
    def mySqrt(self, x: int) -> int:
        # x=15
        out=x**0.5
        out=int(out)
        out_lst=str(out).split(sep='.', maxsplit=2)
        return out_lst[0]
s=Solution()
print(s.mySqrt(8))
