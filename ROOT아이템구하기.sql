-- 코드를 작성해주세요

SELECT item_id, item_name
FROM item_info a
WHERE EXISTS (
    SELECT 1
    FROM item_tree b
    WHERE b.parent_item_id IS NULL and b.item_id = a.item_id
);
