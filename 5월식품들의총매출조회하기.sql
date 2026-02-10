-- 코드를 입력하세요
SELECT a.product_id, a.product_name, sum(a.price * b.amount) as total_sales
FROM food_product a join food_order b on a.product_id = b.product_id
WHERE b.produce_date >= '2022-05-01' and b.produce_date <= '2022-05-31'
GROUP BY a.product_id, a.product_name
ORDER BY total_sales DESC, a.product_id;
