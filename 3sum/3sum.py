class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        nums.sort()
        for i in range(len(nums)-2):
    
          target = -(nums[i])
          low = i + 1
          high = len(nums)-1
          while low < high:
            sum = nums[low] + nums[high]
            if sum == target:
              res.add((nums[i],nums[low],nums[high]))
              low += 1
            elif sum < target:
              low += 1
            else:
              high -= 1
        return list(res)
