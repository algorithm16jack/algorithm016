class Solution(object):
    def in_range(self, number, head, tail):
        if number >= head and number <= tail:
            return True
        else:
            return False
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        if target < matrix[0][0]:
            return False
        if target > matrix[-1][-1]:
            return False
        i_head = 0
        i_tail = m - 1
        i_mid = (i_head + i_tail) / 2
        while not self.in_range(target, matrix[i_mid][0], matrix[i_mid][-1]):
            if target > matrix[i_mid][-1]:
                i_head = i_mid + 1
                i_mid = (i_head + i_tail) / 2
            else:
                i_tail = i_mid - 1
                i_mid = (i_head + i_tail) / 2
            if i_head > i_tail:
                return False
        
        i_final = i_mid
        j_head = 0
        j_tail = n - 1
        j_mid = (j_head + j_tail) / 2
        while j_head < j_tail:
            if matrix[i_final][j_mid] == target:
                return True
            elif matrix[i_final][j_mid] < target:
                j_head = j_mid + 1
                j_mid = (j_head + j_tail) / 2
            else:
                j_tail = j_mid - 1
                j_mid = (j_head + j_tail) / 2
        if matrix[i_final][j_mid] == target:
            return True
        else:
            return False