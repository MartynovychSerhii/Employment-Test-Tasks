--1.1. The number of created leads per week grouped by course type
select DATE_TRUNC('week', l.created_at) as week,
        c.type as course_type,
        count(*) as new_leads
from  leads as l
join courses as c on l.course_id = c.id
group by week, course_type

--1.2. The number of WON flex leads per country created from 01.01.2024
select country_name,
        count(*) as won_count
from  users as u
join domains as d on u.domain_id = d.id
join leads as l on u.id = l.user_id
join courses as c  on l.course_id = c.id
where created_at >= '01.01.2024'
    and status = 'WON'
    and type = 'FLEX'
group by country_name

--1.3. User email, lead id and lost reason for users who have lost flex leads from 01.07.2024
select email,
        l.id as lead_id,
        lost_reason
from  users as u
join leads as l on u.id = l.user_id
join courses as c on l.course_id = c.id
where status = 'LOST'
    and type = 'FLEX'
    and created_at >= '01.07.2024'





