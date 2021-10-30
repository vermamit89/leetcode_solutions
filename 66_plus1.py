class Solution:
    def plusOne(self, digits):

        digit_str=str(digits)
        return " ".join(str(int(digit_str.replace('[','').replace(']','').replace(',','').replace(' ',''))+1)).split()
x=Solution()
print(x.plusOne([1,2,3]))