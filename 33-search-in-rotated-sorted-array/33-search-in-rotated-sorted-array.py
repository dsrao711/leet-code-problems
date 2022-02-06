class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # 1. Check if left is sorted
        # 2. Check if target is present in the left half , 
        # 3. If present , change the high and make the left half as new window , h = m - 1
        # 4. If no , change the window to right half by making lo = m + 1
        # 5. Same process for right 
        
        l = 0
        h = len(nums) - 1
        
        while(l <= h):
            m = (l + h) / 2
            if(nums[m] == target):
                return m
            # Check if left half is sorted
            elif(nums[l] <= nums[m]):
                # Check if target is present in left half
                if(target >= nums[l] and target < nums[m]):
                    h = m - 1
                else:
                    l = m + 1
            # Check if right half is sorted
            elif(nums[m] <= nums[h]):
                # Check if target is present in right half
                if(target > nums[m] and target <= nums[h]):
                    l = m + 1
                else:
                    h = m - 1
        
        return -1
            
                    