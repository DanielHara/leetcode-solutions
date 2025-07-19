"""
    Question 636: https://leetcode.com/problems/exclusive-time-of-functions/

    Interesting question! Just store the start timestamps on a stack, creating one stack per functionId.
    When you have an end log, pop a timestamp from the stack the corresponds to that functionId.
    Remember to go through all the stacks you have an increase all of their timestamps with the function duration you just found.
"""


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:        
        answer = [0 for index in range(n)]
        function_id_2_call_stack = {}
        
        for log in logs:
            [function_id_string, log_type, timestamp_string] = log.split(':')
            timestamp = int(timestamp_string)
            function_id = int(function_id_string)

            if log_type == 'start':
                if function_id not in function_id_2_call_stack:
                    function_id_2_call_stack[function_id] = []
                
                function_id_2_call_stack[function_id].append(timestamp)
            else:
                popped_timestamp = function_id_2_call_stack[function_id].pop()
                time_increase = timestamp - popped_timestamp + 1
                answer[function_id] = answer[function_id] + time_increase

                for dummy_function_id in range(n):
                    stack = function_id_2_call_stack.get(dummy_function_id, [])
                    for index in range(len(stack)):
                        stack[index] = stack[index] + time_increase

        return answer
