"""
    Question 1519: https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

    Kinda frustrating question because you'll need to build the tree from the edges and labels.
    After that, use some DP for the exploring the tree in a decent data structure.
    This question requires more sweat than real brain.
"""

class Node:
    def __init__(self, label, number):
        self.number = number
        self.label = label
        self.children = []

class Solution:
    def depthFirstExplore(self, root, node_number_to_label_frequency_dictionary):
        if root.number in node_number_to_label_frequency_dictionary:
            return node_number_to_label_frequency_dictionary[root.number]

        result = {}
        for char_ord in range(0, ord('z') - ord('a') + 1):
            char = chr(char_ord + ord('a'))
            result[char] = 1 if char == root.label else 0

        for child in root.children:
            child_frequency_dictionary = self.depthFirstExplore(child, node_number_to_label_frequency_dictionary)
            for char_ord in range(0, ord('z') - ord('a') + 1):
                char = chr(char_ord + ord('a'))
                result[char] = result[char] + child_frequency_dictionary[char]
        
        node_number_to_label_frequency_dictionary[root.number] = result
        return result


    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        from_origin_to_destinations = {}
        for [origin, destination] in edges:
            if origin not in from_origin_to_destinations:
                from_origin_to_destinations[origin] = []
            from_origin_to_destinations[origin].append(destination)

            if destination not in from_origin_to_destinations:
                from_origin_to_destinations[destination] = []
            from_origin_to_destinations[destination].append(origin)


        visited_node_numbers = set()
        root = Node(labels[0], 0)
        nodes = [root]

        node_number_to_node_dict = {}
        node_number_to_node_dict[0] = root

        while nodes:
            node = nodes.pop(0)
            if node.number in visited_node_numbers:
                continue

            visited_node_numbers.add(node.number)

            destinations = from_origin_to_destinations.get(node.number, [])
            for destination in destinations:
                if destination not in visited_node_numbers:
                    child = Node(labels[destination], destination)
                    node_number_to_node_dict[destination] = child
                    node.children.append(child)

                    nodes.append(child)

        node_number_to_label_frequency_dictionary = {}

        self.depthFirstExplore(root, node_number_to_label_frequency_dictionary)
        
        result = []
        for node_number in range(0, n):
            result.append(node_number_to_label_frequency_dictionary[node_number][node_number_to_node_dict[node_number].label])

        return result
