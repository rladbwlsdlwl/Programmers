-- 코드를 입력하세요
SELECT car_id
FROM car_rental_company_car a
WHERE a.car_type = '세단' and EXISTS (
    SELECT 1
    FROM car_rental_company_rental_history b
    WHERE a.car_id = b.car_id and b.start_date between '2022-10-01' and '2022-10-31'
)
ORDER BY car_id DESC;


# SELECT distinct a.car_id
# FROM car_rental_company_car a left join car_rental_company_rental_history b using(car_id)
# WHERE a.car_type = '세단' and b.start_date between '2022-10-01' and '2022-10-31'
# ORDER BY a.car_id DESC;
