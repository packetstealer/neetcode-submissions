class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            midpoint = (left + right) // 2
            if nums[midpoint] == target:
                return nums.index(target)
            elif nums[midpoint] < target:
                left = midpoint + 1
            else:
                right = midpoint - 1
        return -1
        