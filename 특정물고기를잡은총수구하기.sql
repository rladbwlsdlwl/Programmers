-- 코드를 작성해주세요
SELECT count(*) as fish_count
FROM FISH_INFO f1 join FISH_NAME_INFO f2 using(fish_type)
WHERE f2.fish_name = "BASS" or fish_name = "SNAPPER";
