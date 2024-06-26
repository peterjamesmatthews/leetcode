"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two
sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N1 = len(nums1)  # length of nums1
        N2 = len(nums2)  # length of nums2
        if N1 > N2:
            return self.findMedianSortedArrays(
                nums2, nums1
            )  # ensures len(nums1) <= len(nums2)

        N = N1 + N2  # length of merged list
        L = N // 2  # size of merged left partition
        L1 = N1 // 2  # size of nums1's left partition
        maxL1 = N1  # maximum size that L1 may be, will be updated with binary search
        L2 = L - L1  # size of num2's left partition

        while True:
            # figure out which values to perform comparisons with; cleverly handle edge cases with use of +/- infinity

            left1 = (
                nums1[L1 - 1] if L1 - 1 > -1 else float("-infinity")
            )  # max value in L1, or -infinity if L1 is empty
            right1 = (
                nums1[L1] if L1 < N1 else float("infinity")
            )  # min value in R1, or infinity if L1 is N1
            left2 = (
                nums2[L2 - 1] if L2 - 1 > -1 else float("-infinity")
            )  # max value in R2, or -infinity if L2 is empty
            right2 = (
                nums2[L2] if L2 < N2 else float("infinity")
            )  # min value in R2, or infinity if L2 is N2

            # check if L1 is correct
            if left1 <= right2 and left2 <= right1:
                # L1 & L2 are at the correct values
                if N % 2 == 0:
                    # N is even
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    # N is odd
                    return min(right1, right2)

            # make nums1 smaller
            if left1 > right2:
                maxL1 = L1
                L1 = L1 // 2
                L2 = L - L1
                continue

            # make nums1 bigger
            if left2 > right1:
                L1 += max((maxL1 - L1) // 2, 1)
                L2 = L - L1
                continue
