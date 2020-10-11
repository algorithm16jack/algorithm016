class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(remain, temp):
            if len(remain) < 1:
                res.append(temp)
                return
            for i in range(len(remain)):
                if i < len(remain) - 1:
                    backtrack(remain[:i] + remain[i+1:], temp + [remain[i]])
                else:
                    backtrack(remain[:i], temp + [remain[i]])

        res = []
        backtrack(nums, [])
        
        return res