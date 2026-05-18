-- 코드를 입력하세요
# 1. 랭크 함수 사용 (row_number, 중복 허용 안함)
with RN as (
    select *, row_number() OVER (order by views desc) as "rn"
    from used_goods_board
)



# 2. 단일행 서브쿼리 사용
# with a as (
#     SELECT f.board_id, file_id, file_ext, file_name
#     FROM USED_GOODS_BOARD b join USED_GOODS_FILE f on b.board_id = f.board_id
#     WHERE views = (
#         SELECT max(views) as views
#         FROM USED_GOODS_BOARD
#     ) # 단일행 서브쿼리, 최대 조회수가 하나일경우
#     ORDER BY file_id desc
# )


SELECT concat("/home/grep/src/", f.board_id, "/", file_id, file_name, file_ext) as "FILE_PATH"
FROM RN join used_goods_file f using(board_id)
WHERE rn <= 1
ORDER BY file_id desc;
