# Question 127: https://leetcode.com/problems/word-ladder/

"""
    Very interesting question! One less optimized way to solve this question is to build a graph to find which words you can
    reach from a specific word, and use BFS to get the smallest path. As this would take time O(N**2), where N is the number of words,
    this isn't feasible.
    You need to find which words you can reach from a specific word. How can you do it efficiently?
    One way to optimize that is to create masks for each word. For example, for the word "hit", its masks would be "_it", "i_t" and "__t".
    Then, create a dictionary, each key of which is an array of which words you can reach from a specific mask. End up with a data structure like this:

    {
        "_it": ["bit", "hit", "fit"]
    }

    For each word you see in the ladder, calculate all the masks (which is fast because each word has <= 10 characters), and there you have all 
    the words you can reach from that specific word.
    Then do the BFS and you have the answer.
    TADA!
"""

from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)

        dictionary_mask_to_words = {}
        for word in wordList:
            for swap_position in range(len(word)):
                chars = [char for char in word]
                chars[swap_position] = '_'
                mask = ''.join(chars)

                if mask not in dictionary_mask_to_words:
                    dictionary_mask_to_words[mask] = set()
                dictionary_mask_to_words[mask].add(word)


        # Here, do the BFS search
        queue = deque()
        queue.append((beginWord, 1))
        visited = set()

        while queue:
            (dequeued_word, number_of_words) = queue.popleft()
            if dequeued_word == endWord:
                return number_of_words
            
            if dequeued_word in visited:
                continue

            visited.add(dequeued_word)

            for swap_position in range(len(dequeued_word)):
                chars = [char for char in dequeued_word]
                chars[swap_position] = '_'
                mask = ''.join(chars)
            
                neighbours = dictionary_mask_to_words.get(mask, [])

                for neighbour in neighbours:
                    queue.append((neighbour, number_of_words + 1))

        return 0
