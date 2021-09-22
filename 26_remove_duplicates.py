class Solution:
    def removeDuplicates(self, nums) -> int:
        i=0
        j=1
        while j < len(nums):
            if nums[i]==nums[j]:
                j+=1
            else:
                nums[i+1]=nums[j]
                i+=1
        return i+1
s=Solution()
s.removeDuplicates([1,1,2,3])


        
