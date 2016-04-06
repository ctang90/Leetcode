class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        for row in range(0, numRows):
            rowRes = ""
            index = row
            while index < len(s):
                rowRes = rowRes + s[index]
                if row == 0 or row == numRows - 1:
                    index = index + (2 * numRows - 2)
                else:
                    if len(rowRes) % 2 == 1:
                        index = index + (2 * numRows - 2 - 2 * row)
                    else:
                        index = index + (2 * row)
            res = res + rowRes
                    
        return res
        