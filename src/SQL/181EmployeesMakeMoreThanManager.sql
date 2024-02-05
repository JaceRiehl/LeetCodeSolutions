-- Write your PostgreSQL query statement below
select e.Name as "Employee"
from Employee e
inner join Employee m on m.id = e.managerId
where e.salary > m.salary