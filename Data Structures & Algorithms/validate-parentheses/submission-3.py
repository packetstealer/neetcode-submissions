class Solution:
    def isValid(self, s: str) -> bool:
        strDict = {
            "{":"}",
            "[":"]",
            "(":")"
        }
        stack = []
        for letter in s:
            if letter in strDict.keys():
                stack.append(letter)
            elif len(stack) == 0 or letter != strDict[stack.pop()]:
                return False
        return len(stack) == 0