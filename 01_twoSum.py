# class Solution:
#     def twoSum(self,nums,target):  
#         nums1=[]
#         count=0 
#         for i in range(len(nums)):
#             first=nums[i]
#             for j in range(len(nums)):
#                 count+=1
#                 second=nums[j]
#                 if i!= j :
#                     if (target)==(first+second):
#                         first_idx=nums.index(first)
#                         nums[first_idx]=0
#                         second_idx=nums.index(second)
#                         nums1.append(first_idx)
#                         nums1.append(second_idx)
#                         break
#         nums1=set(nums1)
#         nums1=list(nums1)
#         nums1=[nums1[0],nums1[1]]
#         print(count)
#         return nums1

class Solution:
    def twoSum(self,nums,target):  
        nums1=[0,0]
        count=0
        dict = {key: i for i, key in enumerate(nums)}
        # print(dict)
        for i in range(len(nums)):
            count+=1
            x = nums[i]
            # print(dict.get(target-x))
            index_of_j = dict.get(target-x)
            if index_of_j and i!=index_of_j:
                nums1[0], nums1[1] = i, index_of_j
                break
        print(count)
        return nums1
nums2=Solution()
print(nums2.twoSum([1,2,3,5,7,11,13,17,19],30))
