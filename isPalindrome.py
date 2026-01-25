class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clear = ""
        for char in s:
            if char.isalnum():
                clear += char.lower()
        return clear == clear[::-1]
        