import heapq
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # track kth smallest distances in a sorted list
        kth_distances = []

        # for each pair of numbers where 0 <= i < j < len(nums)
        for i, a in enumerate(nums):
            for b in nums[i + 1 :]:
                distance = abs(a - b)

                # if kth_distances is not full, insert distance into kth_distances
                if len(kth_distances) < k:
                    heapq.heappush(kth_distances, -distance)
                    continue

                # if distance is larger than or equal to the largest distance in kth_distances, skip
                if distance >= -kth_distances[0]:
                    continue

                # insert distance into kth_distances
                heapq.heapreplace(kth_distances, -distance)

        # return last element in kth_distances
        return -heapq.heappop(kth_distances)
