class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if target<nums[i]:
                    return i
                elif target>nums[len(nums)-1]:
                    return len(nums)          
s=Solution()
print(s.searchInsert([1,3,5,7],6))