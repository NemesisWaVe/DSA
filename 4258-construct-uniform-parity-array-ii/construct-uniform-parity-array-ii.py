class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        firstParity=nums1[0]%2
        if all(x%2==firstParity for x in nums1):
            return True
        return min(nums1)%2!=0