class Solution:
    def isPalindrome(self, s: str) -> bool:
        #newStr = s.replace(" ","").replace("'","").strip(",.?!").lower()
        newStr = ""
        for letter in s.replace(" ","").lower():
            if letter.isalnum():
                newStr += letter
        first = 0
        last = len(newStr) - 1

        for i in range(len(newStr)):
            if newStr[first] == newStr[last]:
                first += 1
                last -= 1
            else:
                return False
        return True

        