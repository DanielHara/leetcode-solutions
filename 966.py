# Question 966: https://leetcode.com/problems/vowel-spellchecker/

# Trivial solution, I just did it.

import re

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        unexact_match_wordlist_dict = {}
        capitalise_match_wordlist_dict = {}
        
        word_set = set()

        for index, word in enumerate(wordlist):
            word_set.add(word)

            capitalise_match = word.lower()
            if capitalise_match not in capitalise_match_wordlist_dict:
                capitalise_match_wordlist_dict[capitalise_match] = word
 
            unexact_match_word = re.sub('[aeiouAEIOU]', '*', word.lower(), flags=re.I)

            if unexact_match_word not in unexact_match_wordlist_dict:
                unexact_match_wordlist_dict[unexact_match_word] = word


        answer = []
        for query in queries:
            if query in word_set:
                answer.append(query)
                continue

            index = None

            capitalise_query = query.lower()
            if capitalise_query in capitalise_match_wordlist_dict:
                answer.append(capitalise_match_wordlist_dict[capitalise_query])
                continue
            
            unexact_query = re.sub('[aeiouAEIOU]', '*', query.lower(), flags=re.I)
            if unexact_query in unexact_match_wordlist_dict:
                answer.append(unexact_match_wordlist_dict[unexact_query])
                continue

            answer.append("")

        return answer
