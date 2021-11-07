nums=[2,0,2,1,1,0]
i=0
j=len(nums)-1
while i<=j:
    if nums[i]>nums[j]:
        nums[i],nums[j]=nums[j],nums[i]   
        j-=1
    elif i==j:
        i+=1
        j=len(nums)-1
    else:
        j-=1
print(nums)