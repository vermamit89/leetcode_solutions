class Solution:
    def removeElement(self, nums, val: int) -> int:
        while val in nums:
            nums.remove(val)
        nums.sort()
        return len(nums)
s=Solution()
print(s.removeElement([3,2,2,3],3))
