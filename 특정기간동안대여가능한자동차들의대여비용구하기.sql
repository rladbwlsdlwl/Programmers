# 2022-11-01 ~ 2022-11-30 기간 내에 대여 가능한 차 목록 A 찾기
with A as (
    select * 
    from CAR_RENTAL_COMPANY_CAR
    where car_id  not in (
        select car_id
        from CAR_RENTAL_COMPANY_RENTAL_HISTORY
        where 
            end_date > '2022-11-01' and
            start_date < '2022-12-01'
    ) and (car_type = '세단' or car_type = 'SUV')
)

# 30일 기간동안 할인되는 차의 종류 테이블 B찾기
, B as (
    select * 
    from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    where duration_type = '30일 이상'
)


# A와 B 테이블을 조인 후 할인되는 최종 fee 테이블 C찾기
, C as (
    select car_id, a.car_type, round(daily_fee*30 - daily_fee*30*discount_rate*0.01, 0) as fee
    from A a join B b using (car_type)
)

# 테이블 C 중 50 ~ 200 만원 사이의 값을 가지는 컬럼 반환하기
select *
from C
where fee >= 500000 and fee < 2000000
order by fee desc, car_type, car_id desc;
