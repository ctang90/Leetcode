class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        step = numRows * 2 - 2
        # first row
        res = s[0::step]
        
        for i in range(1, numRows - 1):
            for j in range(i, len(s), step):
                res += s[j]
                if j + step - 2 * i < len(s):
                    res += s[j + step - 2]
                    
        res += s[numRows-1::step]
                    
        return res
        