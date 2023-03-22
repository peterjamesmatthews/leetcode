from collections import deque
from typing import List, Tuple


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        """
        Given a positive integer `n`, representing `n` cities numbered from `1` to `n` and a two
        dimensional array `roads` where `roads[i] = [a_i, b_i, distance_i]` indicates that there's
        a bidirectional road between cities `a_i` and `b_i` of length `distance_i`, return the
        shortest path between cities `1` and `n`
        """
        # construct a graph to efficiently get all paths that connect to a given city via list indexing
        graph: List[List[Tuple[int, int]]] = [[] for _ in range(n)]
        for road in roads:
            graph[road[0] - 1].append((road[1], road[2]))
            graph[road[1] - 1].append((road[0], road[2]))
        # graph[city - 1] = [..., (neighbor, distance), ...]

        # list to track which cities we've seen `seen[city - 1] == True` means we've seen it, otherwise `False`
        # initializes to [True, False, False, ..., False]
        seen: List[bool] = [True, *[False for _ in range(n - 1)]]

        # queue to efficiently append and pop cities that we will visit during BFS
        # left will be the front of the queue, right will be the back
        will_visit = deque([1], maxlen=n)

        # minimum distance that will be returned, upper-bound of 1e4 is given in the problem description
        min_distance = int(1e4)

        # while there are still cities to visit
        while len(will_visit) > 0:
            # visit the next city
            city = will_visit.popleft()

            # get all paths connected to city
            paths = graph[city - 1]

            # find minimum distance across all paths, mark neighbors for visit
            for path in paths:
                if not seen[path[0] - 1]:  # we haven't visited neighbor yet
                    # mark neighbor as seen
                    seen[path[0] - 1] = True

                    # enqueue neighbor to visit later
                    will_visit.append(path[0])

                # check for smaller distance
                min_distance = min(min_distance, path[1])

        # we've traversed every path connected to cities 1 and n
        return min_distance
