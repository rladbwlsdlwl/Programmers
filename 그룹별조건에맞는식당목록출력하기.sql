-- 코드를 입력하세요
with A as 
(
    SELECT member_id, count(*) as total
    FROM rest_review
    GROUP BY member_id
    ORDER BY total DESC
    LIMIT 1
)


SELECT member_name, review_text, date_format(review_date, '%Y-%m-%d') as review_date
FROM rest_review r join member_profile m on r.member_id = m.member_id
WHERE m.member_id = (
    SELECT member_id
    FROM A
)
ORDER BY review_date ASC, review_text ASC;
