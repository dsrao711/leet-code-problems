class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i , curr , total):
            # Base condn
            if(total == target):
                res.append(curr.copy())
                return
            if(total > target or i >= len(candidates)):
                return
            
            # Steps for rec
            curr.append(candidates[i])
            # Choice 1
            dfs(i , curr , total + candidates[i])
            # BT
            curr.pop()
            # Choice 2
            dfs(i + 1 , curr , total)
            
        
        dfs(0 , [] , 0)
        
        return res
            