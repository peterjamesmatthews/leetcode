import heapq
import math
from typing import Dict, List, Tuple


class Solution:
    @staticmethod
    def dijkstras(source: int, edges: List[List[int]], V: int) -> Dict[int, float]:
        """
        Returns the shortest path from the given source node to all other nodes using Dijkstra's Algorithm.

        Args:
            source (int): The source node.
            edges (List[List[int]]): The edges of a graph each edge is of the form [source, target, weight].
            V (int): The number of nodes in the graph.

        Returns:
            List[int]: A list of shortest distances from the source node to all other nodes.
        """
        # initialize distances from source to each node
        distances = {node + 1: math.inf for node in range(V)}
        distances[source] = 0

        # heap of distances to nodes from source
        nodes_to_visit: List[Tuple[float, int]] = [(0, source)]

        # while there is some node to visit
        while nodes_to_visit:
            # get node closest to source
            _, node = heapq.heappop(nodes_to_visit)

            # get all edges from node to other nodes
            node_edges = list(filter(lambda edge: edge[0] == node, edges))

            # for each edge from node to other target nodes
            for _, target, distance in node_edges:
                # the new distance to target would be current distance plus this edge's distance
                new_distance = distances[node] + distance

                # if the new distance is less than the current distance, use this edge and plan to visit target
                if new_distance < distances[target]:
                    distances[target] = new_distance
                    heapq.heappush(nodes_to_visit, (new_distance, target))

        # return all nodes and their path distances
        return distances

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        min_times = Solution.dijkstras(k, times, n).values()
        max_min_time = max(min_times)
        return int(max_min_time) if max_min_time != math.inf else -1
