class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        l, r = 0, x
        res = 0
        while l <= r:
            m = (l + r) // 2
            if (m * m) <= x:
                res = m
                l = m + 1
            else:
                r = m - 1
        return res