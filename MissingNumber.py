class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        expectNum = n * (n + 1) / 2
        sumNums = sum(nums)
        return expectNum - sumNums
        