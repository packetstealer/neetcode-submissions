class Solution:
    def isValid(self, s: str) -> bool:
        bracketCompare = {
            "{":"}",
            "[":"]",
            "(":")"
        }
        stack = []
        for bracket in s:
            if bracket in bracketCompare.keys():
                stack.append(bracket)
            elif len(stack) == 0 or bracket != bracketCompare[stack.pop()]:
                return False
        return len(stack) == 0

        