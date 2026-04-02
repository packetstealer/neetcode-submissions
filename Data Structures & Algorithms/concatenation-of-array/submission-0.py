class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        numLen = len(nums)
        for x in range(0,numLen):
            nums.append(nums[x])
        return nums
