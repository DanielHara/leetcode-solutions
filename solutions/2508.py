"""
Question 2508: https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/

Very interesting question. I just mapped the possibilities of how many nodes with an odd degree could happen.

Thinking a bit, if you have 4 nodes with an odd degree, using a greedy approach works!
"""

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        node_2_degree = {}

        for [u, v] in edges:
            if u not in node_2_degree:
                node_2_degree[u] = set()
            node_2_degree[u].add(v)
            
            if v not in node_2_degree:
                node_2_degree[v] = set()
            node_2_degree[v].add(u)
        
        indexes_with_odd_degree = []
        for index, degree_set in node_2_degree.items():
            if len(degree_set) % 2 != 0:
                indexes_with_odd_degree.append(index)
        
        if len(indexes_with_odd_degree) == 0:
            return True

        if len(indexes_with_odd_degree) == 2:
            first_node = indexes_with_odd_degree[0]
            second_node = indexes_with_odd_degree[1]

            if second_node not in node_2_degree[first_node]:
                return True
            
            for degree_set in node_2_degree.values():
                if first_node not in degree_set and second_node not in degree_set and len(degree_set) % 2 == 0:
                    return True
            
            count = 0
            for i in range(1, n + 1):
                if i not in node_2_degree:
                    count = count + 1
            
            if count >= 2:
                return True

            return False

        
        if len(indexes_with_odd_degree) != 4:
            return False
        
        count = 0
        for i in range(0, 4):
            for j in range(0, 4):
                if count >= 2:
                    break

                if i == j:
                    continue
                
                first_node = indexes_with_odd_degree[i]
                second_node = indexes_with_odd_degree[j]

                if len(node_2_degree[first_node]) % 2 != 0  and len(node_2_degree[second_node]) % 2 != 0 and second_node not in node_2_degree[first_node]:
                    node_2_degree[first_node].add(second_node)
                    node_2_degree[second_node].add(first_node)
                    count = count + 1

        for i in range(0, 4):
            if len(node_2_degree[indexes_with_odd_degree[i]]) % 2 != 0:
                return False

        return True
