class TrieNode:
    def __init__(self):
        self.children={}
        self.word=None
    def addWord(self,word:str)->None:
        curr=self
        for char in word:
            if char not in curr.children:
                curr.children[char]=TrieNode()
            curr=curr.children[char]
        curr.word=word
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for w in words:
            root.addWord(w)
        ROWS,COLS=len(board),len(board[0])
        res=[]
        def dfs(r:int,c:int,parent:TrieNode):
            char=board[r][c]
            curr=parent.children[char]
            if curr.word:
                res.append(curr.word)
                curr.word=None
            board[r][c]='#'
            for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
                nr,nc=r+dr,c+dc
                if 0<=nr<ROWS and 0<=nc<COLS and board[nr][nc] in curr.children:
                    dfs(nr,nc,curr)
            board[r][c]=char
            if not curr.children:
                del parent.children[char]
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r,c,root)
        return res