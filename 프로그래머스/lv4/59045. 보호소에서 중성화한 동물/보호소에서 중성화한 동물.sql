-- 코드를 입력하세요
SELECT I.ANIMAL_ID,I.ANIMAL_TYPE,I.NAME

FROM ANIMAL_INS I left join ANIMAL_OUTS O on I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.DATETIME <= O.DATETIME AND I.SEX_UPON_INTAKE LIKE "%Intact%" AND O.SEX_UPON_OUTCOME NOT LIKE "%Intact%"