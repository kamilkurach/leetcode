# 586. Customer Placing the Largest Number of Orders
# Write your MySQL query statement below
SELECT customer_number FROM Orders
WHERE order_number = (SELECT MAX(order_number) FROM Orders)
