select p.firstName, p.LastName, a.city, a.state
from Person p
left join Address a on a.personId = p.personId