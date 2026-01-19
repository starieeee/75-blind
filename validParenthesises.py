class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        matching = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for char in s:
            if char in matching:
                if not stack:
                    return False
                topElement = stack.pop()
                if topElement != matching[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
        