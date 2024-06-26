"""
Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.
"""

from functools import lru_cache
from typing import List


class Solution:
    @lru_cache(int(1e5))
    @staticmethod
    def calculate_subarrays(length: int) -> int:
        if length == 0:
            return 0

        return length**2 - Solution.calculate_subarrays(length - 1)

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        subarrays = 0  # the number of zero filled subarrays that nums contains

        start, end = 0, 0  # indices that will contain zero-filled runs
        while start < len(nums):
            # scan through nums searching for runs of zeros
            if nums[start] != 0:
                start += 1
                continue

            # assuming nums[start] == 0

            # starting from start, find ending index for this run of zeros
            end = start
            while end < len(nums) and nums[end] == 0:
                end += 1

            # assuming nums[start:end] only contains zeros

            # calculate how many 0 subarrays are in this run and add that to the total
            subarrays += Solution.calculate_subarrays(end - start)

            # advance the start index to the end of the current run
            start = end

        return subarrays  # return the final count
