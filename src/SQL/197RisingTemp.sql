select w.id
from Weather w
join Weather w2 on w.recordDate = DATE_ADD(w2.recorddate, interval 1 day)
where w.temperature > w2.temperature