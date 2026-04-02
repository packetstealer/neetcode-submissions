class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums2 = [pow(num,2) for num in nums]
        nums2.sort()
        return nums2
        