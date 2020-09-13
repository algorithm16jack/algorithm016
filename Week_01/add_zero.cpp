class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        head_index = 0
        tail_index = len(nums) - 1

        while head_index < tail_index:
            if nums[head_index] != 0:
                head_index += 1
            else:
                del nums[head_index]
                nums.append(0)
                tail_index -= 1
