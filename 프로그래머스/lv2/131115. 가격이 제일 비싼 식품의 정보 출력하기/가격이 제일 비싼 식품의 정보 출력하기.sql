-- 코드를 입력하세요
SELECT * 
FROM FOOD_PRODUCT AS f
WHERE f.PRICE = (SELECT MAX(PRICE) AS "PRICE" FROM FOOD_PRODUCT )