# Question 1976: https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

"""
    Very interesting question! I decided to use a modified version of Dijkstra's algorithm: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
"""

class Solution:
    def recursiveCountPaths(self, prev: Dict[int, List[int]], start: int, dp) -> int:
        mod = 10**9 + 7
        
        if start == 0:
            return 1
        
        if start in dp:
            return dp[start]

        result = 0
        nodes = prev[start]
        for node in nodes:
            if node == 0:
                result = (result + 1) % mod
            else:
                result = (result + self.recursiveCountPaths(prev, node, dp)) % mod
        
        dp[start] = result        
        return result
    
    # Just use a modified Djikstra
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        from_neighbour_to_neighbours = {}
        for [first_node, second_node, time] in roads:
            if first_node not in from_neighbour_to_neighbours:
                from_neighbour_to_neighbours[first_node] = []
            from_neighbour_to_neighbours[first_node].append([second_node, time])

            if second_node not in from_neighbour_to_neighbours:
                from_neighbour_to_neighbours[second_node] = []
            from_neighbour_to_neighbours[second_node].append([first_node, time])

        dist = {}
        prev = {}
        Q = set()

        for i in range(n):
            dist[i] = -1
            prev[i] = []
            Q.add(i)
        
        dist[0] = 0
        

        while Q: 
            min_dist = min(map(lambda el: dist[el], filter(lambda el: dist[el] >= 0, Q)))
            array_u = list(filter(lambda el: dist[el] == min_dist, Q))

            for u in array_u:
                Q.remove(u)
                
                for [neighbour, time] in from_neighbour_to_neighbours.get(u, []):
                    alt = dist[u] + time
                    if dist[neighbour] == -1 or alt < dist[neighbour]:
                        dist[neighbour] = alt
                        prev[neighbour] = [u]
                    elif alt == dist[neighbour]:
                        prev[neighbour].append(u)

        dp = {}
        return self.recursiveCountPaths(prev, n - 1, dp)
