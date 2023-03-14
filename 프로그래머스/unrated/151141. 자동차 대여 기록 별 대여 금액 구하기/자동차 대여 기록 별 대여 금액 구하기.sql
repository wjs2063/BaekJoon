-- 코드를 입력하세요
with value as (
SELECT company.CAR_ID,company.CAR_TYPE,company.DAILY_FEE,history.HISTORY_ID,
CASE
WHEN DATEDIFF(history.end_date,history.start_date) + 1 >= 90 THEN "90일 이상"
WHEN DATEDIFF(history.end_date,history.start_date) + 1 >= 30 THEN "30일 이상"
WHEN DATEDIFF(history.end_date,history.start_date) + 1 >= 7 THEN "7일 이상"
ELSE "NO SALES"
END
AS DURATION_TYPE,
DATEDIFF(history.end_date,history.start_date) + 1 AS diff
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY history
join CAR_RENTAL_COMPANY_CAR company on history.CAR_ID = company.CAR_ID
WHERE company.CAR_TYPE = "트럭" 
)

SELECT value.history_id,
CASE 
WHEN value.DURATION_TYPE = "90일 이상" THEN ROUND(value.DAILY_FEE * value.diff * (100 - plan.discount_rate)/100)
WHEN value.DURATION_TYPE = "30일 이상" THEN ROUND(value.DAILY_FEE * value.diff * (100 - plan.discount_rate)/100)
WHEN value.DURATION_TYPE = "7일 이상" THEN ROUND(value.DAILY_FEE * value.diff * (100 - plan.discount_rate)/100)
ELSE value.DAILY_FEE * value.diff 
END AS FEE
FROM value left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN plan
on value.DURATION_TYPE = plan.DURATION_TYPE AND plan.CAR_TYPE = value.CAR_TYPE
ORDER BY FEE DESC ,value.HISTORY_ID DESC 
