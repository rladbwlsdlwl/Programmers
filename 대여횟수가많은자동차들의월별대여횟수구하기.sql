# 2022-08 ~ 2022-10 기간 내에 차량 대여 횟수가 5회가 넘는 차량을 찾기
with CAR as (
    select car_id
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where 
        start_date between '2022-08-01' and '2022-10-31'
    group by car_id
    having count(*) >= 5
)

# 월별로 차량 대여 횟수 출력
select month(c1.start_date) as month, c1.car_id, count(*) as records
from CAR_RENTAL_COMPANY_RENTAL_HISTORY c1 join CAR c2 using(car_id)
where 
    start_date between '2022-08-01' and '2022-10-31'
group by month(c1.start_date), c1.car_id
having count(*) > 0
order by month(c1.start_date), c1.car_id desc
