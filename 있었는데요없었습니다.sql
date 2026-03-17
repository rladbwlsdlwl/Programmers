-- 코드를 입력하세요
SELECT a.animal_id, a.name
FROM animal_ins a join animal_outs b on a.animal_id = b.animal_id
WHERE a.datetime > b.datetime
ORDER BY a.datetime;
