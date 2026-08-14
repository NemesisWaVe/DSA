class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f=0
        r=len(numbers)-1
        while f!=r:
            currentsum=numbers[f]+numbers[r]
            if currentsum>target:
                r-=1
            elif currentsum<target:
                f+=1
            else:
                return [f+1,r+1]       
        return []