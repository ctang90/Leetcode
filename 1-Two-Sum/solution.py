class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictMap = {}
        for i, item in enumerate(nums):
            if ( target - item in dictMap.keys()):
                return [dictMap[target - item], i]
            dictMap[item] = i