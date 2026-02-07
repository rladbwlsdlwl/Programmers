-- 코드를 작성해주세요

SELECT id, fish_name, length
FROM fish_info a join fish_name_info b on a.fish_type = b.fish_type
WHERE (a.fish_type, length) in (
    SELECT fish_type, max(length) as length
    FROM fish_info
    GROUP BY fish_type
);
