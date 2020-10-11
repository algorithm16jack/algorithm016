class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(k, current, remain):
            if len(current) == k:
                res.append(current)
                return
            for i in range(len(remain)):
                next_current = current[:]
                next_current.append(remain[i])
                backtrack(k, next_current, remain[i+1:])
   
        backtrack(k, [], range(1, n+1))

        return res
