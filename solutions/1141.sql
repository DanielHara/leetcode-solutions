/* Questions 1141: https://leetcode.com/problems/user-activity-for-the-past-30-days-i/

   Trivial question
*/


SELECT COUNT(DISTINCT user_id) as active_users, activity_date as day FROM Activity WHERE activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND '2019-07-27' GROUP BY activity_date HAVING active_users > 0
