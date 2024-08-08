select u.name, case when sum(r.distance) is null then 0 else sum(r.distance) end as travelled_distance
from Users u 
left join Rides r on r.user_id = u.id
group by u.id, u.name
order by sum(r.distance) desc, u.name asc