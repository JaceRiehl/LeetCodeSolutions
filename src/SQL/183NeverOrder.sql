# Write your MySQL query statement below
select c.Name as "Customers"
from Customers c
left join Orders o on o.customerId = c.Id
where o.id is NULL