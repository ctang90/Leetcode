class Solution(object):
    # return 0 if nums2[k - 2 - i] <= nums1[i] && nums2[k - 1 - i)] >= nums1[i]
    # return -1 if both are less than, need to check larger i
    # return 1 if both are greater than, need to check smaller i
    def check(self, nums1, nums2, k, i):
        # if I can find exactly (k - 1 - i) number of  numbers in nums2 that <= nums1[i]
        # find too many,  check smaller i-> return -1
        # find not enough, check larger i-> return 1
        if k - 1 - i < 0:
            return -1
        if k - 1 - i == 0:
            if len(nums2) == 0 or nums2[0] >= nums1[i]:
                return 0
            else:
                return -1
        if k - 1 - i > len(nums2):
            return 1
        if k - 1 - i == len(nums2):
            if nums2[-1] <= nums1[i]:
                return 0
            else:
                return 1
        if nums2[k - 2 - i] > nums1[i]:
            return 1
        if nums2[k - 1 - i] < nums1[i]:
            return -1
        return 0

    def findKth(self, k, nums1, nums2):
        left = 0
        right = len(nums1) - 1
        while left <= right:
            mid = (left + right)/2
            status = self.check(nums1, nums2, k, mid)
            if status == 0:
                return nums1[mid]
            elif status == -1:
                right = mid - 1
            else:
                left = mid + 1

        left = 0
        right = len(nums2) - 1
        while left <= right:
            mid = (left + right)/2
            status = self.check(nums2, nums1, k, mid)
            if status == 0:
                return nums2[mid]
            elif status == -1:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return -1



    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        N = len(nums1) + len(nums2)
        if N % 2 == 1:
            return self.findKth(N/2 + 1, nums1, nums2)
        return ( float(self.findKth(N/2, nums1, nums2)) + float(self.findKth(N/2 + 1, nums1, nums2)))/2
