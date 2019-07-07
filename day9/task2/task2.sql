SELECT * FROM Salespeople WHERE snum = 1001;
SELECT city, sname, snum, comm FROM Salespeople;
SELECT rating, cname FROM Customers WHERE city = 'SanJose' LIMIT 1;
SELECT DISTINCT snum FROM Orders; -- Не понял о каком "текущем порядке" речь
SELECT * FROM Orders WHERE amt > 1000;
SELECT sname, city FROM Salespeople WHERE city = 'London' AND comm > 0.1;
SELECT * FROM Customers WHERE rating <= 100 AND city <> 'Rome';
SELECT cname FROM Customers c LEFT JOIN Salespeople s ON c.snum = s.snum WHERE s.sname IN ('Peel', 'Motika');
SELECT cname FROM Customers WHERE cname REGEXP'(^[A-G])';
SELECT SUM(amt) AS summ FROM Orders WHERE odate = '2015-03-10'; -- формат даты yyyy-mm-dd поэтому запрос не совсем про третье октября
SELECT DISTINCT COUNT(city) AS city_amount FROM Customers;
SELECT cname FROM Customers WHERE cname LIKE 'G%' ORDER BY cname;
SELECT onum, snum, amt*0.12 AS comm_amt FROM Orders;
SELECT CONCAT(CONCAT("For the city ", city), CONCAT(", the highest rating is: ", rating)) AS city FROM (SELECT city AS city, MAX(rating) AS rating FROM Customers GROUP BY city) AS l;
SELECT cnum, cname, rating FROM Customers ORDER BY rating DESC;
SELECT onum, cname FROM Orders o LEFT JOIN Customers c ON o.cnum = c.cnum;
SELECT onum, sname, cname FROM Orders o LEFT JOIN Salespeople s ON o.snum = s.snum LEFT JOIN Customers c ON o.cnum = c.cnum;
SELECT onum, sname, ROUND(amt*comm, 2) AS comm_amt FROM Orders o LEFT JOIN Salespeople s ON o.snum = s.snum LEFT JOIN Customers c ON o.cnum = c.cnum WHERE c.rating > 100;
SELECT c.city, cname, maxrating FROM Customers AS c JOIN (SELECT city, max(rating) AS maxrating FROM Customers GROUP BY city) AS l ON c.city = l.city AND c.rating = l.maxrating;
--SELECT * FROM Orders o LEFT JOIN Salespeople s ON o.snum = s.snum LEFT JOIN Customers c ON o.cnum = c.cnum WHERE s.city <> c.city;
--SELECT * FROM (SELECT snum, cnum FROM Orders)
SELECT * FROM Salespeople s LEFT JOIN Customers c ON s.city = c.city WHERE (SELECT cnum, snum FROM Orders)
SELECT l.snum, l.sname, COUNT(o.cnum), l.same_city_customer
FROM (SELECT s.snum, s.sname, s.city, COUNT(c.cnum) AS same_city_customer FROM Salespeople s, Customers c WHERE s.city = c.city GROUP BY s.snum, s.sname, s.city) AS l,
     (SELECT s.snum, c.cnum FROM Salespeople s, Customers c WHERE s.city = c.city) AS k,
      Orders o
        WHERE (k.snum, k.cnum) = (o.snum, o.cnum) GROUP BY l.snum, l.sname;


SELECT k.snum, k.sname, COUNT(DISTINCT k.cnum) FROM (SELECT s.snum, sname, c.cnum FROM Salespeople s, Customers c WHERE s.city = c.city) AS k, Orders o
WHERE (k.snum, k.cnum) = (o.snum, o.cnum) GROUP BY k.snum, k.sname;


SELECT l.snum, l.sname
FROM
(SELECT s.snum, s.sname, s.city, COUNT(c.cnum) AS same_city_customer FROM Salespeople s, Customers c WHERE s.city = c.city GROUP BY s.snum, s.sname, s.city) AS count_same_city_customer,
(SELECT k.snum, k.sname, COUNT(DISTINCT k.cnum) AS same_city_deal FROM (SELECT s.snum, sname, c.cnum FROM Salespeople s, Customers c WHERE s.city = c.city) AS k, Orders o
WHERE (k.snum, k.cnum) = (o.snum, o.cnum) GROUP BY k.snum, k.sname) AS count_same_city_deal
WHERE


   SELECT snum, sname
      FROM Salespeople main
      WHERE city IN
        (SELECT city
            FROM Customers inner
            WHERE inner.snum <> main.snum);

















SELECT snum, sname FROM (SELECT s.snum, s.sname, s.city, c.cnum, c.cname FROM Salespeople s, Customers c WHERE s.city = c.city) k
WHERE k.snum IN (
    SELECT DISTINCT l.snum FROM (SELECT s.snum, s.sname, s.city, c.cnum, c.cname FROM Salespeople s, Customers c WHERE s.city = c.city) AS l,
        Orders o
        WHERE l.snum = o.snum AND l.cnum = o.cnum
) AND k.cnum NOT IN (
    SELECT DISTINCT l.cnum FROM (SELECT s.snum, s.sname, s.city, c.cnum, c.cname FROM Salespeople s, Customers c WHERE s.city = c.city) AS l,
        Orders o
        WHERE l.snum = o.snum AND l.cnum = o.cnum
);


SELECT * FROM (SELECT s.snum, s.sname, s.city, c.cnum, c.cname FROM Salespeople s, Customers c WHERE s.city = c.city) AS l,
        Orders o
        WHERE l.snum = o.snum AND l.cnum = o.cnum;
