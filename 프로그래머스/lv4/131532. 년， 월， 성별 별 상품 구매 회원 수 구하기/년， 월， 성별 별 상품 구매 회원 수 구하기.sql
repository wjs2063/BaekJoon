-- 코드를 입력하세요
SELECT O.year YEAR,O.month MONTH ,u.GENDER GENDER ,COUNT(DISTINCT u.user_id) USERS 
FROM USER_INFO u join 
(SELECT *,YEAR(o.SALES_DATE) year,MONTH(o.SALES_DATE) month FROM ONLINE_SALE  o)
O on u.user_id = O.user_id
WHERE GENDER is not null
GROUP BY O.year,O.month,u.GENDER 
ORDER BY O.year ASC , O.month ASC, u.GENDER ASC
