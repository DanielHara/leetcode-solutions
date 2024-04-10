# Question 2747: https://leetcode.com/problems/count-zero-request-servers/

"""
    Quite interesting, and not so easy question. Just kept a window of the servers which get requests from [time - x, time].
    My submissions failed twice, because I had iterated though range(0. 10**6), and not through range(min_query, max_query + 1, 1).
"""

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        time_to_server_id = {}
        for [server_id, time] in logs:
            if time not in time_to_server_id:
                time_to_server_id[time] = set()

            time_to_server_id[time].add(server_id)
        
        min_query = min(queries)
        max_query = max(queries)
        
        servers_2_number_of_requests = {}
        for time in range(min_query - x - 1, min_query):
            servers = time_to_server_id.get(time, [])

            for server in servers:
                servers_2_number_of_requests[server] = servers_2_number_of_requests.get(server, 0) + 1
        
        query_time_to_indexes = {}
        for index, query in enumerate(queries):
            if query not in query_time_to_indexes:
                query_time_to_indexes[query] = []
            query_time_to_indexes[query].append(index)
        
        answer = [None for i in range(len(queries))]
        for time in range(min_query, max_query + 1, 1):
            # update
            servers_to_remove = time_to_server_id.get(time - x - 1, [])
            servert_to_add = time_to_server_id.get(time, [])

            for server in servers_to_remove:
                servers_2_number_of_requests[server] = servers_2_number_of_requests.get(server, 0) - 1
                if servers_2_number_of_requests[server] <= 0:
                    del servers_2_number_of_requests[server]
            
            for server in servert_to_add:
                servers_2_number_of_requests[server] = servers_2_number_of_requests.get(server, 0) + 1

            if time in query_time_to_indexes:
                indexes = query_time_to_indexes[time]
                for index in indexes:
                    answer[index] = n - len(servers_2_number_of_requests)
        
        return answer
