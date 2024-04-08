from typing import List


class Solution:
    def twoOutOfThree(
        self,
        nums1: List[int],  # type: ignore
        nums2: List[int],  # type: ignore
        nums3: List[int],  # type: ignore
    ) -> List[int]:
        nums1: set[int] = set(nums1)
        nums2: set[int] = set(nums2)
        nums3: set[int] = set(nums3)

        one_and_two = nums1 & nums2
        two_and_three = nums2 & nums3
        one_and_three = nums1 & nums3

        return list(one_and_two | two_and_three | one_and_three)
