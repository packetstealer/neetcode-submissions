class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Remove the placeholders first to maintain the correct length
        del nums1[m:]
        for num in nums2:
            nums1.append(num)
        nums1.sort()