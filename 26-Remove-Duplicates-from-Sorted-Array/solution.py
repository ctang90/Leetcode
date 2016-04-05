class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        update = 0
        for i in range(0, len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[update] = nums[i]
                update = update + 1
        nums[update] = nums[-1]
        return update + 1