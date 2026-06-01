-- 코드를 입력하세요
SELECT user_id, nickname, 
    concat(city, " ", street_address1, " ", street_address2) as "전체주소",
    concat(substring(tlno, 1, 3), "-",
           substring(tlno, 4, 4), "-",
           substring(tlno, 8, 4)) as "전화번호"
FROM used_goods_board JOIN used_goods_user on writer_id = user_id
GROUP BY user_id, nickname, street_address1, street_address2, tlno
HAVING count(*) >= 3
ORDER BY user_id desc;


# select writer_id
# from used_goods_board
# group by writer_id
# having count(*) >= 3;
