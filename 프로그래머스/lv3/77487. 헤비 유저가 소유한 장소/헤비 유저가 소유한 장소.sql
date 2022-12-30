-- 코드를 입력하세요
SELECT h.ID,h.NAME,h.HOST_ID from PLACES as h ,(select ID,NAME,HOST_ID,COUNT(NAME) as c from PLACES group by HOST_ID) as O where O.c > 1 and h.HOST_ID = O.HOST_ID