# Question 1477: https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/

"""
    Just use DP to do the trick
"""

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        S = []

        for num in arr:
            S.append((S[-1] if S else 0) + num)

        dict_S = {}
        for index, s in enumerate(S):
            dict_S[s] = index
        
        T = [None for i in range(len(arr))]
        for i in range(len(arr)):
            # has to search for (target + (S[i - 1] if S else 0))
            searched_index = dict_S.get(target + (S[i - 1] if i > 0 else 0), None)

            if searched_index is not None:
                T[i] = searched_index - i + 1
        
        acc_T = [None for i in range(len(T))]
        for i in range(len(acc_T) - 1, -1, -1):
            ant = None if i == len(acc_T) - 1 else acc_T[i + 1]

            if ant is None:
                acc_T[i] = T[i]
            elif T[i] is not None:
                acc_T[i] = min(T[i], ant)
            else:
                acc_T[i] = ant

        result = None
        for i in range(len(acc_T)):
            if T[i] is None:
                continue

            acc = acc_T[i + T[i]] if (i + T[i] < len(acc_T)) else None

            if acc is not None and T[i] is not None:
                if result is None:
                    result = acc + T[i]
                else:
                    result = min(result, acc + T[i])
        
        return result if result is not None else -1
