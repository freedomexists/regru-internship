https://www.hackerrank.com/challenges/placements/problem

select
    s.name
from Students as s
left join Packages as ps on ps.id = s.id
left join (
    select fr.friend_id, fr.id, fs.name, pf.salary from Friends as fr
    left join Packages as pf on pf.id = fr.friend_id
    left join Students as fs on fr.friend_id = fs.id
) as f on f.id = s.id
where f.salary > ps.salary
order by f.salary;
