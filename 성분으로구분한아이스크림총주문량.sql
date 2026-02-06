-- 코드를 입력하세요
SELECT ingredient_type, sum(total_order) as total_order
FROM first_half f JOIN icecream_info i on f.flavor = i.flavor
GROUP BY i.ingredient_type
order by total_order ASC;
