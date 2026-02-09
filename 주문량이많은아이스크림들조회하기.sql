-- 코드를 입력하세요
with A as (
    SELECT *
    FROM first_half

    UNION

    SELECT *
    FROM july
)



SELECT flavor
FROM A
GROUP BY flavor
ORDER BY sum(total_order) DESC
LIMIT 3;
