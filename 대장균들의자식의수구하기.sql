-- 코드를 작성해주세요

SELECT a.id, count(b.id) as child_count
FROM ecoli_data a LEFT JOIN ecoli_data b on a.id = b.parent_id
GROUP BY a.id;
