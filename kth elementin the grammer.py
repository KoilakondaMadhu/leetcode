class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def dfs(n,k,rootval):
            if n==1 and k==1:
                return rootval
            
            numNodes=2**(n-1)
            if k<=numNodes/2: #k in left subtree
                nextRootVal = 0 if rootval==0 else 1
                return dfs(n-1,k,nextRootVal)
            else:
                nextRootVal = 1 if rootval==0 else 0
                return dfs(n-1, k-(numNodes/2),nextRootVal)
                
        return dfs(n,k,0)
                
