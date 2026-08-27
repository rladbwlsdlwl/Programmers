-- 코드를 입력하세요
SELECT b.author_id, c.author_name, b.category, sum(a.sales*b.price) as sales
FROM book_sales a JOIN book b on a.book_id = b.book_id JOIN author c on b.author_id = c.author_id
WHERE a.sales_date >= "2022-01-01" and a.sales_date < "2022-02-01"
GROUP BY c.author_id, b.category
ORDER BY b.author_id, category desc;
