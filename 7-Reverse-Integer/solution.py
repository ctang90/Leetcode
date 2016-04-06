class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        val = x
        if (val == 0) or (val >= 2 ** 31 - 1) or (val < - 2 ** 31):
            return 0
        sign = (val < 0)
        if val < 0:
            val = -val
        
        # Ignore the 0s in the end
        while val % 10 == 0:
            val /= 10
        
        res = 0
        while val > 0:
            res = res * 10 + val % 10;
            val /= 10
            
        if sign:
            res = - res
            
        if (res >= 2 ** 31 - 1) or (res < - 2 ** 31):
            return 0
        return res
            
        
            
            
        
        