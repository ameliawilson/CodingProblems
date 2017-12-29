class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = len(set(nums))
        
        return int((sum(nums) - sum(set(nums)))/(n-s))
