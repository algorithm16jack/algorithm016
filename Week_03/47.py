class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(remain, temp):
            if len(remain) < 1:
                res.append(tuple(temp))
                return
            for i in range(len(remain)):
                if i < len(remain) - 1:
                    backtrack(remain[:i] + remain[i+1:], temp + [remain[i]])
                else:
                    backtrack(remain[:i], temp + [remain[i]])

        res = []
        backtrack(nums, [])
        res = list(set(res))
        
        return res