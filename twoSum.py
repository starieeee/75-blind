class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num = {}
        for i in range(len(nums)):
            current = nums[i]
            complement = target - current
            if complement in num:
               return [num[complement], i]
            num[current] = i
        return []
        
        return num