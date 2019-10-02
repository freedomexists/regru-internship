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


https://www.hackerrank.com/challenges/weather-observation-station-18/problem

SELECT ROUND(ABS(MIN(LAT_N) - MAX(LAT_N)) + ABS(MIN(LONG_W) - MAX(LONG_W)), 4) FROM STATION;

https://www.hackerrank.com/challenges/the-report/problem

SELECT S.Name, G.Grade, S.Marks
FROM Students S INNER JOIN Grades G ON S.Marks BETWEEN G.Min_Mark AND G.Max_Mark
WHERE G.Grade > 7
ORDER BY G.Grade DESC, S.Name ASC;

SELECT null, G.Grade, S.Marks
FROM Students S INNER JOIN Grades G ON S.Marks BETWEEN G.Min_Mark AND G.Max_Mark
WHERE G.Grade <= 7
ORDER BY G.Grade DESC, S.Marks ASC;

https://www.hackerrank.com/challenges/symmetric-pairs/problem

SELECT f1.X, f1.Y FROM Functions f1
INNER JOIN Functions f2 ON f1.X=f2.Y AND f1.Y=f2.X
GROUP BY f1.X, f1.Y
HAVING COUNT(f1.X)>1 or f1.X<f1.Y
ORDER BY f1.X