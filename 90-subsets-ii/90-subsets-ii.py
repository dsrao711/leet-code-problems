class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtracking(i , subsets):
            if(i >= len(nums)):
                res.append(subsets.copy())
                return
            subsets.append(nums[i])
            backtracking(i+1 , subsets)
            subsets.pop()
            while(i+1 < len(nums) and nums[i] == nums[i+1]):
                i += 1
            backtracking(i+1 , subsets)
            
        backtracking(0 , [])
        
        return res