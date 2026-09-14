class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_num={}
        for index,num in enumerate(nums):
            complement=target-num
            if complement in dict_num:
                return (dict_num[complement],index)
            dict_num[num]=index