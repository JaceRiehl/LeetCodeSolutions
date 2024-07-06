select customer_number
from Orders o2
group by o2.customer_number
order by count(o2.order_number) desc
limit 1