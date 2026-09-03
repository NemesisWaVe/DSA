class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        ROWS,COLS=len(heights),len(heights[0])
        pacificReach=set()
        atlanticReach=set()
        def dfs(r:int,c:int,reachable:set)->None:
            reachable.add((r,c))
            for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
                nr,nc=r+dr,c+dc
                if 0<=nr<ROWS and 0<=nc<COLS:
                    if (nr,nc) in reachable:
                        continue
                    if heights[nr][nc]>=heights[r][c]:
                        dfs(nr,nc,reachable)
        for c in range(COLS):
            dfs(0,c,pacificReach)
        for r in range(ROWS):
            dfs(r,0,pacificReach)
        for c in range(COLS):
            dfs(ROWS-1,c,atlanticReach)
        for r in range(ROWS):
            dfs(r,COLS-1,atlanticReach)
        return list(pacificReach & atlanticReach)
