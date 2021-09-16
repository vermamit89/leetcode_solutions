class Solution:
    def twoSum(self,nums,target):  
        nums1=[] 
        for i in range(len(nums)):
            first=nums[i]
            for j in range(len(nums)):
                second=nums[j]
                if i!= j :
                    if (target)==(first+second):
                        first_idx=nums.index(first)
                        nums[first_idx]=0
                        second_idx=nums.index(second)
                        nums1.append(first_idx)
                        nums1.append(second_idx)
        nums1=set(nums1)
        nums1=list(nums1)
        nums1=[nums1[0],nums1[1]]
        return nums1
nums2=Solution()
print(nums2.twoSum([0,1,2,3,6],6))
