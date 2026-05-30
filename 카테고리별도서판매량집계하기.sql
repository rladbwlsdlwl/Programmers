-- 코드를 입력하세요
SELECT category, sum(sales) as total_sales
FROM book join book_sales using(book_id)
WHERE sales_date >= "2022-01-01" and sales_date < "2022-02-01"
GROUP BY category
ORDER BY category asc;
