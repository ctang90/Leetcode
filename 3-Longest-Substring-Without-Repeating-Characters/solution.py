class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None or s == "":
            return 0
        dictMap = {}
        maxlen = 0
        prevlen = 0
        for i, c in enumerate(s):
            if c in dictMap:
                curlen = min(i - dictMap[c], prevlen + 1)
            else:
                curlen = prevlen + 1
            maxlen = max(maxlen, curlen)
            prevlen = curlen
            dictMap[c] = i
            
        return maxlen
            
            