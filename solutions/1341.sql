# Question 1341: https://leetcode.com/problems/movie-rating/

# This question has no secrets, just hard work :)
# I didnt know that the UNION instruction removes duplicates, and that I had to use UNION ALL instead.

# Write your MySQL query statement below

(
    SELECT user_name AS results FROM (
    (SELECT user_id, COUNT(movie_id) AS number_movies FROM MovieRating GROUP BY user_id) Table1
        LEFT JOIN
    (SELECT name as user_name, user_id FROM Users) Table2
        ON Table1.user_id = Table2.user_id
    ) ORDER BY number_movies DESC, user_name ASC LIMIT 1
)
UNION ALL
(
    SELECT movie_title AS results FROM (
        (SELECT MR1.movie_id, 
            (SUM(MR1.rating) / (SELECT COUNT(MR3.user_id) FROM MovieRating MR3 WHERE MR3.movie_id = MR1.movie_id AND Month(MR3.created_at) = 2 AND Year(MR3.created_at) = 2020)) AS movie_average_rating
        FROM MovieRating MR1 WHERE Month(MR1.created_at) = 2 AND Year(MR1.created_at) = 2020 GROUP BY MR1.movie_id) Table1
        LEFT JOIN
        (SELECT title AS movie_title, movie_id FROM Movies) Table2
        ON Table1.movie_id = Table2.movie_id
    ) ORDER BY movie_average_rating DESC, movie_title ASC LIMIT 1
)
