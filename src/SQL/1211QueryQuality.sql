select q.query_name, 
    round(avg(cast(rating as decimal) / position), 2) as quality,
    round(sum(case when rating < 3 then 1 else 0 end) * 100 / count(*), 2) as poor_query_percentage
from Queries q
where query_name is not null
group by q.query_name