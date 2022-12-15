"""
Question 608: https://leetcode.com/problems/tree-node/
"""

"""
Not a difficult question, just write your query and check a specific node is the root (p_id is null), or if it's an
inner node (it's a parent to some other node)
"""

# Write your MySQL query statement below

SELECT id, (IF(p_id IS NULL, 'Root', IF(
    id IN (
        SELECT DISTINCT t1.id
        FROM Tree t1
        JOIN Tree t2 WHERE t1.id = t2.p_id
    ),
    'Inner', 'Leaf'
) ))  AS type FROM Tree
