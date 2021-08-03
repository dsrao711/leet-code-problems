class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        set_nums = list(set(nums))
        sum_diff = sum(nums) - sum(set_nums)
        len_diff = len(nums) - len(set_nums)
        return (sum_diff // len_diff)