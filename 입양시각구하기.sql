-- 코드를 입력하세요
# 가상의 hours 테이블 생성
# 0~23의 hour 컬럼을 갖는 테이블
# Recursive를 통한 반복문
with RECURSIVE hours as (
    SELECT 0 as hour
    UNION ALL
    SELECT hour + 1
    FROM hours
    WHERE hour < 23
)


SELECT a.hour, ifnull(b.count, 0) as count
FROM hours a left join 
    (SELECT hour(datetime) as hour, count(animal_id) as count
    FROM animal_outs
    GROUP BY hour(datetime)) b on a.hour = b.hour
ORDER BY a.hour;
