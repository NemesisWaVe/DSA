class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        subset=[]
        def dfs(i,curr_target):
            if curr_target==0:
                res.append(subset.copy())
                return
            if curr_target<0 or i>= len(candidates):
                return
            subset.append(candidates[i])
            dfs(i,curr_target-candidates[i])
            subset.pop()
            dfs(i+1,curr_target)
        dfs(0,target)
        return res