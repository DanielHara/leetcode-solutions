# Question 126: https://leetcode.com/problems/word-ladder-ii/

"""
    Solve question 127 (https://leetcode.com/problems/word-ladder/) before this one.

    Extend your solution to use a dictionary to store the origins of a word, so that you can go back to it and
    reconstruct the paths.    
"""

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
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
        min_number_of_words = None

        dictionary_word_to_previous_words = {}

        while queue:
            (dequeued_word, number_of_words) = queue.popleft()
            if min_number_of_words is not None and number_of_words > min_number_of_words:
                break

            if dequeued_word == endWord:
                min_number_of_words = number_of_words
            
            if dequeued_word in visited:
                continue

            visited.add(dequeued_word)

            for swap_position in range(len(dequeued_word)):
                chars = [char for char in dequeued_word]
                chars[swap_position] = '_'
                mask = ''.join(chars)
            
                neighbours = dictionary_mask_to_words.get(mask, [])

                for neighbour in neighbours:
                    if neighbour != dequeued_word and neighbour not in visited:
                        if neighbour not in dictionary_word_to_previous_words:
                            dictionary_word_to_previous_words[neighbour] = []
                        
                        if len(dictionary_word_to_previous_words[neighbour]) > 0 and dictionary_word_to_previous_words[neighbour][0]['number_of_words'] > number_of_words:
                            dictionary_word_to_previous_words[neighbour] = []

                        if len(dictionary_word_to_previous_words[neighbour]) == 0 or (number_of_words <= dictionary_word_to_previous_words[neighbour][0]['number_of_words']):
                            dictionary_word_to_previous_words[neighbour].append({
                                'word': dequeued_word,
                                'number_of_words': number_of_words
                            })
                        queue.append((neighbour, number_of_words + 1))

        # Now, process dictionary_word_to_previous_words, from endWord to beginWord
        word = endWord
        paths = []

        return self.DFS(dictionary_word_to_previous_words, endWord, beginWord)
    
    def DFS(self, dictionary_word_to_previous_words, word, beginWord):
        if word == beginWord:
            return [[word]]
        
        neighbours = dictionary_word_to_previous_words.get(word, [])
        paths = []

        for neighbour_object in neighbours:
            neighbour_word = neighbour_object['word']
        
            recursive_paths = self.DFS(dictionary_word_to_previous_words, neighbour_word, beginWord)
            for recursive_path in recursive_paths:
                paths.append(recursive_path + [word])
        
        return paths

