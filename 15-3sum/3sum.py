class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n= len(nums)
        for i in range(0,n):
            key=nums[i]
            j=i-1
            while j>=0 and nums[j]>key:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=key
        res=[]
        for i in range(n):
            if nums[i]>0:
                break
            if i>0 and nums[i-1]==nums[i]:
                continue
            f=i+1
            r=n-1
            while f<r:
                threeSum=nums[i]+nums[f]+nums[r]
                if threeSum>0:
                    r-=1
                elif threeSum<0:
                    f+=1
                else:
                    res.append([nums[i],nums[f],nums[r]])
                    f+=1
                    r-=1
                    while f<r and nums[f]==nums[f-1]:
                        f+=1
        return res