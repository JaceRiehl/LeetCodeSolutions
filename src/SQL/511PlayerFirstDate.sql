select a.player_id, min(a.event_date) as first_login
from Activity a
order by a.player_id asc, a.event_date asc