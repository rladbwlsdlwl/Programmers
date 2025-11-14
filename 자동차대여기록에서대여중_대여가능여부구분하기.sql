-- 코드를 입력하세요
with RENTAL_NO as (
    SELECT distinct car_id
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where end_date >= '2022-10-16' and start_date <= '2022-10-16'
)

select car_id, "대여중" as AVAILABILITY
from RENTAL_NO

UNION

select distinct car_id, "대여 가능" as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where car_id not in (
    select car_id
    from RENTAL_NO
)

ORDER BY car_id desc;
