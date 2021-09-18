class Solution:
    def reverse(self, x: int) -> int:
        # if x.bit_length() <=31:
        if -2147483648<=x<=2147483647:
            num_str=str(x)
            isPositive=True
            if x<0:
                isPositive=False       
                num_str=num_str[1:]
            num_str_rev=num_str[::-1]
            if (-2**31)<=int(num_str_rev)<=(2**31-1):
                if isPositive:
                    return int(num_str_rev)
                else:
                    return 0-int(num_str_rev)
            else:
                return 0
#         else:
#             return 0
        
s=Solution()
print(s.reverse(-2147483412))