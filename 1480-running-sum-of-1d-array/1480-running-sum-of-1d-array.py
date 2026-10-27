class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(0,len(nums)):
            if i==0:
                nums[i]=nums[i]
        
            else:
                nums[i]+=nums[i-1]   
        
        return nums

L1=Solution()
print(L1.runningSum([1,2,3,4,5,6,7]))        