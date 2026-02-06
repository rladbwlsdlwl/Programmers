-- 코드를 입력하세요
SELECT p.product_code, sum(o.sales_amount) * p.price as sales
FROM product p JOIN offline_sale o ON p.product_id = o.product_id
GROUP BY p.product_code
ORDER BY  sales DESC, product_code ASC;
