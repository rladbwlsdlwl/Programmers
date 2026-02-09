-- 코드를 입력하세요
SELECT animal_id, name
FROM animal_outs a
WHERE NOT EXISTS (
    SELECT 1
    FROM animal_ins b
    WHERE a.animal_id = b.animal_id
);

# SELECT a.animal_id, a.name
# FROM animal_outs a left join animal_ins b using(animal_id)
# WHERE b.animal_id IS NULL
