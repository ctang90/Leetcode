class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numDict = {}
        for i in range(0, len(nums)):
            numDict[nums[i]] = i
        
        for i in range(0, len(nums)):
            other = target - nums[i]
            if ( other in numDict.keys()) and (numDict[other] != i):
                return [i, numDict[other]]
                
            
        