-- 코드를 입력하세요
SELECT category, price as "max_price", product_name
FROM FOOD_PRODUCT
WHERE (category, price) in (
    SELECT category, max(price) as max_price
    FROM FOOD_PRODUCT
    GROUP BY category
    HAVING category in ("과자", "국", "김치", "식용유")
)
ORDER BY max_price desc;
