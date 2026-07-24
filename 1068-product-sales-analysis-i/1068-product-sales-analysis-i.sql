# Write your MySQL query statement below
select product_name, year, price from sales s inner join product p on s.product_id=p.product_id 