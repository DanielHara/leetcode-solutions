# Question 1834: https://leetcode.com/problems/single-threaded-cpu/

"""
    A very interesting question, indeed, one of my favourites since a long time!
    Use a heap to save the list of available tasks, and pop an element from the heap to get
    the next task to be processed by the CPU. Create a minimum heap where you'll pop the task
    without lower processing time (and lower index, in case of a tie)
"""

import functools

def compare_tasks(task1: List[List[int]], task2: List[List[int]]) -> int:
    if task1[1] > task2[1]:
        return 1
    if task1[1] < task2[1]:
        return -1
    
    if task1[2] > task2[2]:
        return 1
    
    return -1

key_function = functools.cmp_to_key(compare_tasks)

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for index, task in enumerate(tasks):
            task.append(index)
        
        tasks.sort(key=lambda task: task[0])

        heap = []
        time = tasks[0][0]
        answer = []
        
        i = 0
        while i < len(tasks):
            j = i
            while j < len(tasks) and tasks[j][0] <= time:
                task = tasks[j]
                heapq.heappush(heap, (key_function(task), task))
                j = j + 1

            if i != j or heap:
                if heap:
                    # Process the task
                    task = heapq.heappop(heap)[1]
                    time = time + task[1]
                    answer.append(task[2])
                i = j
            else:
                time = tasks[i][0]
        
        while heap:
            task = heapq.heappop(heap)[1]
            time = time + task[1]
            answer.append(task[2])
        
        return answer
