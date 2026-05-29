-- 코드를 작성해주세요

SELECT count(fish_type) as fish_count, max(length) as max_length, fish_type
FROM fish_info 
GROUP BY fish_type
HAVING avg(IFNULL(length, 10)) >= 33
ORDER BY fish_type;
