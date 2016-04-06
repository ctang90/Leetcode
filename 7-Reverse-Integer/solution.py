class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = int(str(abs(x))[::-1])
        res *= cmp(x, 0)
        if (res < - 2 ** 31) or (res >= 2 ** 31 - 1):
            return 0
        return res
            
        
            
            
        
        