class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        #solution greedy
        right_max = 0
        for i in range(len(nums)):
            if i <= right_max:
                if i + nums[i] > right_max:
                    right_max = i + nums[i]
        
        if right_max >= len(nums) - 1:
            return True
        else:
            return False
