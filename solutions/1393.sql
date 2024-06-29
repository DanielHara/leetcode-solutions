# Question 1393: https://leetcode.com/problems/capital-gainloss/

# Interesting and easy question, just do it

# Write your MySQL query statement below

SELECT stock_name, (sum_sell_price - sum_buy_price) AS capital_gain_loss FROM (
    (SELECT stock_name, SUM(price) AS sum_buy_price FROM Stocks WHERE operation = 'buy' GROUP BY stock_name) Table1
        LEFT JOIN
    (SELECT stock_name as stock_name_aux, SUM(price) AS sum_sell_price FROM Stocks WHERE operation = 'sell' GROUP BY stock_name) Table2
    ON Table1.stock_name = Table2.stock_name_aux
)

