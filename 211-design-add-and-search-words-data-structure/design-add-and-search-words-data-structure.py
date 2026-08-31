class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        curr=self.root
        for char in word:
            if char not in curr.children:
                curr.children[char]=TrieNode()
            curr=curr.children[char]
        curr.endOfWord=True

    def search(self, word: str) -> bool:
        def dfs(index:int,root:TrieNode)->bool:
            curr=root
            for i in range(index,len(word)):
                char=word[i]
                if char==".":
                    for childNode in curr.children.values():
                        if dfs(i+1,childNode):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr=curr.children[char]
            return curr.endOfWord
        return dfs(0,self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)