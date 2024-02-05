select e.name, b.bonus from Employee e
left join Bonus b on b.empId = e.empId
where b.bonus is NULL or b.bonus < 1000