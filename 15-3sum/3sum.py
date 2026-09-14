class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        nums.sort()
        res=[]
        for i in range(0,n):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            f=i+1
            r=n-1
            while f<r:
                threesum=nums[i]+nums[f]+nums[r]
                if threesum>0:
                    r-=1
                elif threesum<0:
                    f+=1
                else:
                    res.append([nums[i],nums[f],nums[r]])
                    f+=1
                    r-=1
                    while f<r and nums[f]==nums[f-1]:
                        f+=1
        return res