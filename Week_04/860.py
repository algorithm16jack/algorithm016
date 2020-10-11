class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        num_5 = 0
        num_10 = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                num_5 += 1
            if bills[i] == 10:
                if num_5 >= 1:
                    num_5 -= 1
                    num_10 += 1
                else:
                    return False
            if bills[i] == 20:
                if (num_5 >= 1 and num_10 >= 1):
                    num_5 -= 1
                    num_10 -= 1
                else:
                    if (num_5 >= 3):
                        num_5 -= 3
                    else:
                        return False
        return True