select s.student_id, s.student_name, ss.subject_name, count(e.student_id) as attended_exams
from Students s
cross join Subjects ss 
left join Examinations e on ss.subject_name = e.subject_name and e.student_id = s.student_id
group by ss.subject_name, s.student_name, s.student_id
order by s.student_id, ss.subject_name