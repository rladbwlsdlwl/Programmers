-- 코드를 입력하세요
# ANIMAL_INS 테이블 기준으로 조인 (입양 보낸 동물이 아닐 경우 NULL 값으로 채워짐)
SELECT ins.name, ins.datetime
FROM animal_ins ins left join animal_outs outs using(animal_id)
WHERE outs.animal_id is null
ORDER BY ins.datetime asc
LIMIT 3;
