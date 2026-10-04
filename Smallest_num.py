nums=[20,70,60,10,30]
smaller=nums[0]
for i in range(0,len(nums)):
    if nums[i]<smaller:
        smaller=nums[i]
    
print(smaller)