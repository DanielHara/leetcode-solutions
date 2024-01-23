# Question 833: https://leetcode.com/problems/find-and-replace-in-string/

"""
   Just do it. Not an interesting question, really
"""

class Solution:
    def shouldReplace(self, s: str, start_index: int, source: str):
        if start_index + len(source) - 1 >= len(s):
            return False

        for i in range(len(source)):
            if s[start_index + i] != source[i]:
                return False

        return True
    
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        v = []
        for i in range(len(indices)):
            v.append({
                'index': indices[i],
                'source': sources[i],
                'target': targets[i]
            })
        
        v.sort(key=lambda el: el['index'])

        for i in range(len(v)):
            indices[i] = v[i]['index']
            sources[i] = v[i]['source']
            targets[i] = v[i]['target']

        result_tokens = []

        i = 0
        j = 0
        while i < len(s):
            if j < len(indices) and i == indices[j]:
                if self.shouldReplace(s, i, sources[j]):
                    result_tokens.append(targets[j])
                    i = i + len(sources[j])
                
                j = j + 1
            else:
                result_tokens.append(s[i])
                i = i + 1
        
        return ''.join(result_tokens)
