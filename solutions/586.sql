# Question 586: https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/

# Trivial question

SELECT customer_number FROM Orders GROUP BY customer_number ORDER BY COUNT(order_number) DESC LIMIT 1
