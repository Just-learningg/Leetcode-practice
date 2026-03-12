class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        close_to_open = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        stack = []

        for bracket in s:
            if bracket in close_to_open:
                top = stack.pop()
                if close_to_open.get(bracket) != top:
                    return False
            else:
                stack.append(bracket)

        return True